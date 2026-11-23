# -*- coding: utf-8 -*-
"""
policy_manager.py - Quản lý phiên 1 lần/ngày, Chế độ B (sai mật khẩu quá N lần tự hủy),
và Chế độ Hẹn giờ xóa (Scheduled Wipe / Countdown).
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


@dataclass
class PolicyState:
    # Chính sách phiên mở khóa: "daily" (1 lần/ngày đến 00:00) hoặc "hours" (tự khóa sau X giờ)
    session_mode: str = "daily"
    session_timeout_hours: float = 1.0

    # Chế độ B: Tự động hủy khi nhập sai mật khẩu quá N lần
    auto_wipe_on_fail: bool = False
    max_failed_attempts: int = 5
    failed_attempts: int = 0

    # Chế độ Hẹn giờ xóa
    scheduled_wipe_enabled: bool = False
    scheduled_wipe_at: Optional[str] = None  # ISO format: YYYY-MM-DD HH:MM:SS (local time)
    scheduled_wipe_label: str = ""

    # Trạng thái đã bị tự hủy
    last_wipe_reason: str = ""
    last_wipe_at: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "PolicyState":
        mode = str(d.get("session_mode", "daily"))
        if mode not in ("daily", "hours"):
            mode = "daily"
        try:
            timeout_h = float(d.get("session_timeout_hours", 1.0))
            if timeout_h <= 0:
                timeout_h = 1.0
        except Exception:
            timeout_h = 1.0
        return cls(
            session_mode=mode,
            session_timeout_hours=timeout_h,
            auto_wipe_on_fail=bool(d.get("auto_wipe_on_fail", False)),
            max_failed_attempts=max(1, int(d.get("max_failed_attempts", 5))),
            failed_attempts=max(0, int(d.get("failed_attempts", 0))),
            scheduled_wipe_enabled=bool(d.get("scheduled_wipe_enabled", False)),
            scheduled_wipe_at=d.get("scheduled_wipe_at") or None,
            scheduled_wipe_label=str(d.get("scheduled_wipe_label", "")),
            last_wipe_reason=str(d.get("last_wipe_reason", "")),
            last_wipe_at=str(d.get("last_wipe_at", "")),
        )


class PolicyManager:
    """Quản lý chính sách bảo mật & phiên đăng nhập (1 lần/ngày hoặc tự khóa theo giờ)."""

    TIME_FMT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, vault_dir: Path):
        self.vault_dir = vault_dir
        self.state_path = vault_dir / "policy_state.json"
        self.state = PolicyState()
        self._unlocked_date: Optional[str] = None
        self._unlocked_at: Optional[datetime] = None
        self.load()

    def load(self) -> None:
        if not self.state_path.exists():
            self.state = PolicyState()
            return
        try:
            raw = json.loads(self.state_path.read_text(encoding="utf-8"))
            self.state = PolicyState.from_dict(raw)
        except Exception:
            self.state = PolicyState()

    def save(self) -> None:
        self.vault_dir.mkdir(parents=True, exist_ok=True)
        tmp = self.state_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(self.state.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp, self.state_path)

    # --- Phiên mở khóa (1 lần/ngày hoặc tự khóa sau X giờ) ---
    @staticmethod
    def today_str(now: Optional[datetime] = None) -> str:
        dt = now or datetime.now()
        return dt.strftime("%Y-%m-%d")

    def configure_session_policy(self, mode: str, timeout_hours: float = 1.0) -> None:
        if mode not in ("daily", "hours"):
            raise ValueError("Chế độ tự khóa không hợp lệ.")
        if mode == "hours" and timeout_hours <= 0:
            raise ValueError("Số giờ tự khóa phải lớn hơn 0.")
        self.state.session_mode = mode
        self.state.session_timeout_hours = float(timeout_hours)
        self.save()

    def mark_unlocked_today(self, now: Optional[datetime] = None) -> None:
        dt = now or datetime.now()
        self._unlocked_date = self.today_str(dt)
        self._unlocked_at = dt
        if self.state.failed_attempts != 0:
            self.state.failed_attempts = 0
            self.save()

    def mark_locked(self) -> None:
        self._unlocked_date = None
        self._unlocked_at = None

    def is_session_expired(self, now: Optional[datetime] = None) -> bool:
        """
        Kiểm tra phiên mở khóa đã hết hạn chưa:
        - Chế độ "hours": hết hạn sau `session_timeout_hours` giờ kể từ lúc mở khóa.
        - Chế độ "daily": hết hạn khi sang ngày mới (00:00).
        """
        if self._unlocked_date is None or self._unlocked_at is None:
            return False
        cur = now or datetime.now()
        if self.state.session_mode == "hours":
            elapsed = (cur - self._unlocked_at).total_seconds()
            return elapsed >= self.state.session_timeout_hours * 3600.0
        return self.today_str(cur) != self._unlocked_date

    def session_expire_reason(self) -> str:
        if self.state.session_mode == "hours":
            h = self.state.session_timeout_hours
            h_str = f"{int(h)}" if h == int(h) else f"{h:g}"
            return f"Đã hết thời gian phiên ({h_str} giờ) — tự động khóa Vault."
        return "Đã sang ngày mới (00:00) — tự động khóa Vault."

    def session_status_str(self, now: Optional[datetime] = None) -> str:
        if self._unlocked_date is None or self._unlocked_at is None:
            return "Đang khóa"
        cur = now or datetime.now()
        if self.state.session_mode == "hours":
            expire_at = self._unlocked_at + timedelta(hours=self.state.session_timeout_hours)
            diff = max(0, int((expire_at - cur).total_seconds()))
            hrs, rem = divmod(diff, 3600)
            mins, secs = divmod(rem, 60)
            return f"Tự khóa sau: {hrs:02d}:{mins:02d}:{secs:02d}"
        return f"Phiên hôm nay: {self._unlocked_date} (khóa lúc 00:00)"

    @property
    def unlocked_date(self) -> Optional[str]:
        return self._unlocked_date

    # --- Chế độ B: Sai mật khẩu quá N lần ---
    def configure_fail_wipe(self, enabled: bool, max_attempts: int) -> None:
        self.state.auto_wipe_on_fail = bool(enabled)
        self.state.max_failed_attempts = max(1, min(50, int(max_attempts)))
        self.state.failed_attempts = 0
        self.save()

    def record_failed_attempt(self) -> tuple[int, int, bool]:
        """
        Ghi nhận 1 lần nhập sai mật khẩu.
        Trả về: (số_lần_đã_sai, ngưỡng_tối_đa, có_phải_kích_hoạt_xóa_ngay_không)
        """
        self.state.failed_attempts += 1
        self.save()
        should_wipe = (
            self.state.auto_wipe_on_fail
            and self.state.failed_attempts >= self.state.max_failed_attempts
        )
        return self.state.failed_attempts, self.state.max_failed_attempts, should_wipe

    # --- Chế độ Hẹn giờ xóa ---
    def set_scheduled_wipe_at(self, target_dt: datetime, label: str = "") -> None:
        self.state.scheduled_wipe_enabled = True
        self.state.scheduled_wipe_at = target_dt.strftime(self.TIME_FMT)
        self.state.scheduled_wipe_label = label or f"Hẹn xóa lúc {self.state.scheduled_wipe_at}"
        self.save()

    def set_scheduled_wipe_countdown(self, hours: float = 0, minutes: float = 0, days: float = 0) -> datetime:
        delta = timedelta(days=days, hours=hours, minutes=minutes)
        if delta.total_seconds() <= 0:
            raise ValueError("Thời gian đếm ngược phải lớn hơn 0.")
        target = datetime.now() + delta
        self.set_scheduled_wipe_at(target, label=f"Đếm ngược -> {target.strftime(self.TIME_FMT)}")
        return target

    def disable_scheduled_wipe(self) -> None:
        self.state.scheduled_wipe_enabled = False
        self.state.scheduled_wipe_at = None
        self.state.scheduled_wipe_label = ""
        self.save()

    def get_scheduled_wipe_dt(self) -> Optional[datetime]:
        if not self.state.scheduled_wipe_enabled or not self.state.scheduled_wipe_at:
            return None
        try:
            return datetime.strptime(self.state.scheduled_wipe_at, self.TIME_FMT)
        except Exception:
            return None

    def is_scheduled_wipe_due(self, now: Optional[datetime] = None) -> bool:
        target = self.get_scheduled_wipe_dt()
        if target is None:
            return False
        cur = now or datetime.now()
        return cur >= target

    def remaining_until_wipe_str(self, now: Optional[datetime] = None) -> str:
        target = self.get_scheduled_wipe_dt()
        if target is None:
            return "Đang tắt"
        cur = now or datetime.now()
        diff = int((target - cur).total_seconds())
        if diff <= 0:
            return "ĐẾN HẠN XÓA!"
        days, rem = divmod(diff, 86400)
        hours, rem = divmod(rem, 3600)
        mins, secs = divmod(rem, 60)
        if days > 0:
            return f"Còn {days} ngày {hours:02d}:{mins:02d}:{secs:02d}"
        return f"Còn {hours:02d}:{mins:02d}:{secs:02d}"

    def record_wipe_executed(self, reason: str, now: Optional[datetime] = None) -> None:
        dt = now or datetime.now()
        self.state.failed_attempts = 0
        self.state.scheduled_wipe_enabled = False
        self.state.scheduled_wipe_at = None
        self.state.scheduled_wipe_label = ""
        self.state.last_wipe_reason = reason
        self.state.last_wipe_at = dt.strftime(self.TIME_FMT)
        self._unlocked_date = None
        self.save()
