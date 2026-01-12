# Flappy Bird - Mobile Version (APK Ready)

## 🎮 Game Improvements

### New Features:
1. **Kivy Framework** - Cross-platform compatibility (Android, iOS, Windows, macOS, Linux)
2. **Touch Controls** - Optimized for mobile devices
3. **Better Physics** - Smoother gameplay with improved gravity and jump mechanics
4. **Enhanced Visuals** - Modern graphics with 3D pipe effects
5. **Medal System** - Gold, Silver, Bronze medals based on score
6. **High Score Tracking** - Persistent best score display
7. **Restart Button** - Easy game restart with visual button
8. **Background Music** - Optional audio support
9. **Full Screen Mode** - Immersive gaming experience
10. **Portrait Orientation** - Optimized for mobile devices

---

## 📱 Building APK for Android

### Prerequisites:
1. **Linux System** (Ubuntu/Debian recommended) OR **WSL2 on Windows**
2. **Python 3.8+** installed
3. **Buildozer** (for APK building)

### Installation Steps:

#### On Linux/WSL:

```bash
# 1. Install system dependencies
sudo apt update
sudo apt install -y python3-pip build-essential git python3 python3-dev \
    ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev \
    libgstreamer1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good

# 2. Install Java (required for Android SDK)
sudo apt install -y openjdk-17-jdk

# 3. Install Cython and Buildozer
pip3 install --upgrade cython
pip3 install --upgrade buildozer

# 4. Install Kivy (for testing on PC)
pip3 install kivy[base]
```

#### On Windows (Without APK Building):

```powershell
# Install Kivy only (for testing)
pip install kivy
```

---

## 🚀 Building the APK

### Step 1: Navigate to Project Directory
```bash
cd /path/to/flappy_bird_game
```

### Step 2: Rename the Kivy file to main.py
```bash
cp flappy_bird_kivy.py main.py
```

### Step 3: Build APK (First time - will take 30-60 minutes)
```bash
buildozer -v android debug
```

### Step 4: Find Your APK
After building successfully, your APK will be in:
```
bin/flappybird-1.0-arm64-v8a-debug.apk
```

### Step 5: Install on Android Device
```bash
# Connect your Android device via USB (enable USB debugging)
buildozer android deploy run

# OR manually transfer the APK to your phone and install
```

---

## 🎯 Testing on PC (Before Building APK)

### Test the Kivy version on your computer:

```bash
python flappy_bird_kivy.py
```

This will open a window where you can test the game with mouse clicks.

---

## 🔧 Troubleshooting

### Issue 1: Buildozer not found
```bash
pip3 install --user buildozer
# Add ~/.local/bin to PATH
export PATH=$PATH:~/.local/bin
```

### Issue 2: Build fails due to permissions
```bash
# Don't run as root. If needed:
buildozer android clean
buildozer -v android debug
```

### Issue 3: Java not found
```bash
# Install Java
sudo apt install openjdk-17-jdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```

### Issue 4: NDK/SDK issues
```bash
# Clean and rebuild
buildozer android clean
rm -rf .buildozer
buildozer -v android debug
```

---

## 📝 Customization

### Change App Icon:
1. Create a PNG icon (512x512 recommended)
2. Save as `icon.png` in the project folder
3. Uncomment in `buildozer.spec`:
   ```
   icon.filename = %(source.dir)s/icon.png
   ```

### Change Splash Screen:
1. Create a PNG splash (1280x720 recommended)
2. Save as `presplash.png`
3. Uncomment in `buildozer.spec`:
   ```
   presplash.filename = %(source.dir)s/presplash.png
   ```

### Adjust Game Difficulty:
Edit `flappy_bird_kivy.py`:
- `self.pipe_speed = 3` (increase for harder)
- `self.pipe_gap = 200` (decrease for harder)
- `self.gravity = 0.5` (increase for more challenging)

---

## 🎨 Game Controls

- **Tap Screen** - Jump
- **Tap "Restart"** - Start new game after game over

---

## 📦 File Structure

```
flappy_bird_game/
├── flappy_bird.py              # Original tkinter version
├── flappy_bird_kivy.py         # New Kivy version (mobile-ready)
├── main.py                     # Copy of kivy version for buildozer
├── buildozer.spec              # APK build configuration
├── image.png                   # Bird sprite (optional)
├── angry-birds-drill-128...mp3 # Background music (optional)
└── README_APK.md              # This file
```

---

## ✨ Key Improvements Over Original

| Feature | Original (tkinter) | New (Kivy) |
|---------|-------------------|------------|
| Mobile Support | ❌ No | ✅ Yes |
| Touch Controls | ❌ No | ✅ Yes |
| APK Export | ❌ No | ✅ Yes |
| Cross-Platform | 🟡 Desktop only | ✅ All platforms |
| Performance | 🟡 Good | ✅ Excellent |
| Responsive | ❌ Fixed size | ✅ Adaptive |

---

## 🌍 Platform Support

- ✅ **Android** (APK)
- ✅ **iOS** (with appropriate tools)
- ✅ **Windows**
- ✅ **macOS**
- ✅ **Linux**

---

## 📄 License

Free to use and modify for educational purposes.

---

## 🤝 Contributing

Feel free to improve the game and share your modifications!

**Happy Gaming! 🎮🐦**
