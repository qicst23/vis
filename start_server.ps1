# Amgen Drug Explorer - Demo Server
Write-Host "========================================"
Write-Host "Amgen Drug Explorer - Demo Server"
Write-Host "========================================"
Write-Host ""
Write-Host "Starting server on http://localhost:8002"
Write-Host "Press Ctrl+C to stop the server"
Write-Host ""

# Check if Python is installed
try {
    python --version
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH"
    Write-Host "Please install Python 3.8+ from https://www.python.org/downloads/"
    Read-Host "Press Enter to exit"
    exit 1
}

# Install requirements if needed
Write-Host "Checking dependencies..."
pip install -r requirements.txt --quiet

# Start the server
python application.py --host 0.0.0.0 --port 8002

