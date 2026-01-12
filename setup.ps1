# ====================================
# Flappy Bird - Quick Setup Script
# ====================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Flappy Bird - Setup & Installation   " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "[1/4] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Install Kivy
Write-Host "`n[2/4] Installing Kivy..." -ForegroundColor Yellow
Write-Host "This may take a few minutes..." -ForegroundColor Gray
pip install kivy | Out-Host

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Kivy installed successfully!" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to install Kivy" -ForegroundColor Red
    exit 1
}

# Check for main.py
Write-Host "`n[3/4] Verifying game files..." -ForegroundColor Yellow
if (Test-Path "main.py") {
    Write-Host "✓ main.py found" -ForegroundColor Green
} else {
    Write-Host "! main.py not found, copying from flappy_bird_kivy.py..." -ForegroundColor Yellow
    Copy-Item "flappy_bird_kivy.py" "main.py"
    Write-Host "✓ main.py created" -ForegroundColor Green
}

# Create launcher script
Write-Host "`n[4/4] Creating launcher..." -ForegroundColor Yellow
$launcherContent = @"
Write-Host "Starting Flappy Bird..." -ForegroundColor Cyan
python main.py
"@
Set-Content -Path "play.ps1" -Value $launcherContent
Write-Host "✓ Launcher created (play.ps1)" -ForegroundColor Green

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "         Setup Complete! 🎮            " -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To play on Windows:" -ForegroundColor White
Write-Host "  1. Run: " -NoNewline -ForegroundColor White
Write-Host "python main.py" -ForegroundColor Yellow
Write-Host "  OR" -ForegroundColor White
Write-Host "  2. Run: " -NoNewline -ForegroundColor White
Write-Host ".\play.ps1" -ForegroundColor Yellow
Write-Host ""

Write-Host "To build APK for Android:" -ForegroundColor White
Write-Host "  • You need Linux or WSL2" -ForegroundColor Gray
Write-Host "  • See README_APK.md for instructions" -ForegroundColor Gray
Write-Host ""

# Ask to run
Write-Host "Would you like to test the game now? (Y/N): " -ForegroundColor Cyan -NoNewline
$response = Read-Host
if ($response -eq 'Y' -or $response -eq 'y') {
    Write-Host "`nStarting game..." -ForegroundColor Green
    python main.py
}
