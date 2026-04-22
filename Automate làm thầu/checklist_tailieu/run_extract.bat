@echo off
chcp 65001 >nul
echo ========================================================
echo TOOL EXTRACT CHECKLIST RFP
echo ========================================================
echo.
set PYTHONIOENCODING=utf-8
python extract_checklist.py
echo.
pause
