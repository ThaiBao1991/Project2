@echo off
chcp 65001 >nul
title JobDetail Intelligence Hub
echo ===================================================
echo   Khoi dong JobDetail Intelligence Hub...
echo ===================================================
python "%~dp0JobDetailApp.py"
pause
