#!/bin/bash

# ====================================
# Flappy Bird - APK Build Script
# For Linux/WSL2
# ====================================

echo "========================================"
echo "  Flappy Bird - APK Builder Setup      "
echo "========================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo -e "${RED}✗ This script requires Linux or WSL2${NC}"
    echo -e "${YELLOW}  For Windows, use setup.ps1 to test the game${NC}"
    exit 1
fi

# Update system
echo -e "${YELLOW}[1/6] Updating system packages...${NC}"
sudo apt update

# Install system dependencies
echo -e "${YELLOW}[2/6] Installing system dependencies...${NC}"
echo -e "${CYAN}This may take 10-15 minutes...${NC}"
sudo apt install -y python3-pip build-essential git python3 python3-dev \
    ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev \
    libgstreamer1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
    autoconf automake libtool

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ System dependencies installed${NC}"
else
    echo -e "${RED}✗ Failed to install system dependencies${NC}"
    exit 1
fi

# Install Java
echo -e "${YELLOW}[3/6] Installing Java JDK...${NC}"
sudo apt install -y openjdk-17-jdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
echo -e "${GREEN}✓ Java installed${NC}"

# Install Python packages
echo -e "${YELLOW}[4/6] Installing Python packages...${NC}"
pip3 install --upgrade pip
pip3 install --upgrade cython
pip3 install --upgrade buildozer
pip3 install kivy

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Python packages installed${NC}"
else
    echo -e "${RED}✗ Failed to install Python packages${NC}"
    exit 1
fi

# Verify main.py exists
echo -e "${YELLOW}[5/6] Verifying game files...${NC}"
if [ -f "main.py" ]; then
    echo -e "${GREEN}✓ main.py found${NC}"
else
    if [ -f "flappy_bird_kivy.py" ]; then
        cp flappy_bird_kivy.py main.py
        echo -e "${GREEN}✓ main.py created from flappy_bird_kivy.py${NC}"
    else
        echo -e "${RED}✗ No game files found!${NC}"
        exit 1
    fi
fi

# Create build script
echo -e "${YELLOW}[6/6] Creating build script...${NC}"
cat > build_apk.sh << 'EOF'
#!/bin/bash

echo "========================================"
echo "     Building Flappy Bird APK...       "
echo "========================================"
echo ""
echo "This will take 30-60 minutes on first build..."
echo ""

# Clean previous builds (optional)
read -p "Clean previous builds? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Cleaning..."
    buildozer android clean
    rm -rf .buildozer
fi

# Build APK
echo "Building APK..."
buildozer -v android debug

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "      ✓ APK Built Successfully!        "
    echo "========================================"
    echo ""
    echo "APK Location:"
    ls -lh bin/*.apk
    echo ""
    echo "To install on device:"
    echo "  1. Connect Android device via USB"
    echo "  2. Enable USB debugging"
    echo "  3. Run: buildozer android deploy run"
    echo ""
else
    echo ""
    echo "✗ Build failed. Check errors above."
    exit 1
fi
EOF

chmod +x build_apk.sh
echo -e "${GREEN}✓ Build script created (build_apk.sh)${NC}"

# Summary
echo ""
echo "========================================"
echo -e "${GREEN}      Setup Complete! 🎮               ${NC}"
echo "========================================"
echo ""
echo -e "${CYAN}Next steps:${NC}"
echo ""
echo -e "1. ${YELLOW}Test the game:${NC}"
echo "   python3 main.py"
echo ""
echo -e "2. ${YELLOW}Build APK:${NC}"
echo "   ./build_apk.sh"
echo ""
echo -e "3. ${YELLOW}Install on device:${NC}"
echo "   buildozer android deploy run"
echo ""

# Ask to test
read -p "Would you like to test the game now? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "Starting game..."
    python3 main.py
fi
