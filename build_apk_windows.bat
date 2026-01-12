@echo off
echo ========================================
echo   Flappy Bird - APK Builder for Windows
echo ========================================
echo.

REM Check if WSL is installed
echo [1/3] Checking WSL installation...
wsl --version >nul 2>&1
if %errorlevel% == 0 (
    echo [OK] WSL is installed!
    goto :check_distribution
) else (
    echo [!] WSL is not installed.
    echo.
    echo Would you like to install WSL now?
    echo This requires administrator privileges and a restart.
    echo.
    choice /C YN /N /M "Install WSL? (Y/N): "
    if errorlevel 2 goto :no_wsl
    if errorlevel 1 goto :install_wsl
)

:install_wsl
echo.
echo Installing WSL...
echo Please run this script as Administrator!
echo.
echo After installation, your computer will restart.
echo.
pause
wsl --install
echo.
echo ========================================
echo   Installation Started!
echo ========================================
echo.
echo Your computer will restart soon.
echo After restart, open this script again.
echo.
pause
exit

:check_distribution
echo [2/3] Checking WSL distribution...
wsl -l -v >nul 2>&1
if %errorlevel% == 0 (
    echo [OK] WSL distribution installed!
    goto :build_apk
) else (
    echo [!] No WSL distribution found.
    echo Installing Ubuntu...
    wsl --install -d Ubuntu
    echo.
    echo Please complete Ubuntu setup, then run this script again.
    pause
    exit
)

:build_apk
echo [3/3] Starting APK build process...
echo.
echo Opening WSL terminal...
echo You will need to run these commands in WSL:
echo.
echo   cd /mnt/c/Users/anmol/Documents/eventdhara/akash/flappy_bird_game
echo   chmod +x setup_linux.sh
echo   ./setup_linux.sh
echo   ./build_apk.sh
echo.
echo ========================================
echo   Opening WSL...
echo ========================================
echo.
pause

REM Open WSL and navigate to project
wsl -d Ubuntu -e bash -c "cd /mnt/c/Users/anmol/Documents/eventdhara/akash/flappy_bird_game && bash"

goto :end

:no_wsl
echo.
echo ========================================
echo   Alternative Options:
echo ========================================
echo.
echo 1. Use GitHub Actions for cloud building
echo    - See BUILD_APK_WINDOWS.md for instructions
echo.
echo 2. Use a Linux Virtual Machine
echo    - Install VirtualBox + Ubuntu
echo.
echo 3. Test the game on Windows instead
echo    - Run: pip install kivy
echo    - Then: python main.py
echo.
pause
goto :end

:end
echo.
echo Thank you for using Flappy Bird APK Builder!
echo For more help, see BUILD_APK_WINDOWS.md
echo.
pause
