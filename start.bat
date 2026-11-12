@echo off
chcp 65001 >nul
cd /d %~dp0
echo [1/2] Building index ...
python tools\build_index.py
echo.
echo [2/2] Starting local server ...
python tools\serve.py
pause
