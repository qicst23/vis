@echo off
echo ========================================
echo Amgen Drug Explorer - Demo Server
echo ========================================
echo.
echo Starting server on http://localhost:8002
echo Press Ctrl+C to stop the server
echo.
python application.py --host 0.0.0.0 --port 8002
pause

