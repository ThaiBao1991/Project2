@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"
title TransferDocument - Dich Tai Lieu Office sang Tieng Viet (Arial)

set "PYTHON_CMD="
python --version >nul 2>&1 && set "PYTHON_CMD=python"
if not defined PYTHON_CMD py -3 --version >nul 2>&1 && set "PYTHON_CMD=py -3"
if not defined PYTHON_CMD py --version >nul 2>&1 && set "PYTHON_CMD=py"

if not defined PYTHON_CMD goto :NO_PYTHON

%PYTHON_CMD% "%~dp0app_gui.py"
set "EXIT_CODE=%ERRORLEVEL%"

if "%EXIT_CODE%"=="0" exit /b 0
if "%EXIT_CODE%"=="2" exit /b 0

echo.
echo [LOI] Ung dung thoat voi ma loi: %EXIT_CODE%
pause
exit /b %EXIT_CODE%

:NO_PYTHON
echo [LOI] Khong tim thay Python tren may. Vui long cai Python 3.10+ truoc.
pause
exit /b 1
