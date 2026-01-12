# 🚀 Quick Start Guide - Flappy Bird Mobile

## 📱 What You Got

✅ **Improved Flappy Bird game** - Mobile-ready version
✅ **APK build system** - For Android devices  
✅ **Cross-platform support** - Works on Windows, Linux, Android
✅ **Professional visuals** - Enhanced graphics and UI
✅ **Touch controls** - Optimized for mobile

---

## ⚡ Quick Start (Choose Your Path)

### Option 1: Test on Windows (Right Now!)

```powershell
# Run the setup script
.\setup.ps1
```

This will:
- Install Kivy
- Verify files
- Let you test the game immediately

**OR** manually:
```powershell
pip install kivy
python main.py
```

---

### Option 2: Build APK for Android (Requires Linux/WSL)

#### Step 1: Enable WSL2 (if on Windows)
```powershell
# Run as Administrator
wsl --install
# Restart computer
```

#### Step 2: Open WSL and Navigate
```bash
cd /mnt/c/Users/anmol/Documents/eventdhara/akash/flappy_bird_game
```

#### Step 3: Run Setup
```bash
chmod +x setup_linux.sh
./setup_linux.sh
```

#### Step 4: Build APK
```bash
./build_apk.sh
```

**APK will be created in:** `bin/flappybird-1.0-arm64-v8a-debug.apk`

---

## 📋 Files Overview

| File | Purpose |
|------|---------|
| `main.py` | **Main game file** (Kivy version) |
| `flappy_bird_kivy.py` | Same as main.py (backup) |
| `flappy_bird.py` | Original tkinter version |
| `buildozer.spec` | APK build configuration |
| `setup.ps1` | **Windows setup script** |
| `setup_linux.sh` | **Linux/WSL setup script** |
| `README_APK.md` | **Detailed APK building guide** |
| `IMPROVEMENTS.md` | Feature comparison |

---

## 🎮 How to Play

### On PC:
- **Click** or **Spacebar** to jump
- Avoid pipes
- Score points by passing pipes

### On Mobile (APK):
- **Tap screen** to jump
- Avoid pipes
- Get medals based on score:
  - 🏆 Gold: 20+ points
  - 🥈 Silver: 10+ points  
  - 🥉 Bronze: 5+ points

---

## 🛠️ Troubleshooting

### "python: command not found"
```bash
# Install Python 3
# Windows: Download from python.org
# Linux: sudo apt install python3
```

### "kivy not found"
```bash
pip install kivy
```

### "buildozer not found" (Linux only)
```bash
pip3 install buildozer
```

### WSL2 issues
```powershell
# Update WSL
wsl --update
wsl --set-default-version 2
```

---

## 📚 Need More Help?

1. **Testing on PC**: See `README_APK.md` → "Testing on PC" section
2. **Building APK**: See `README_APK.md` → "Building the APK" section  
3. **Improvements made**: See `IMPROVEMENTS.md`
4. **Customization**: See `README_APK.md` → "Customization" section

---

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Test on Windows | **2 minutes** |
| Setup WSL2 | **10 minutes** |
| Install dependencies | **15 minutes** |
| First APK build | **30-60 minutes** |
| Rebuild APK | **2-5 minutes** |

---

## 🎯 Recommended Path

### For Beginners:
1. ✅ Test on Windows first (`.\setup.ps1`)
2. ✅ Play and understand the game
3. ✅ Then try APK building (if needed)

### For Advanced Users:
1. ✅ Direct APK build on Linux/WSL
2. ✅ Customize game settings
3. ✅ Build and test on Android device

---

## 📦 What's Included

```
flappy_bird_game/
├── 🎮 Game Files
│   ├── main.py                  # Main game (Kivy)
│   ├── flappy_bird_kivy.py      # Backup
│   └── flappy_bird.py           # Original (tkinter)
│
├── 📱 APK Building
│   ├── buildozer.spec           # APK config
│   ├── setup_linux.sh           # Linux setup
│   └── build_apk.sh             # Created by setup
│
├── 🖥️ Windows Testing
│   └── setup.ps1                # Windows setup
│
├── 📝 Documentation
│   ├── QUICKSTART.md            # This file
│   ├── README_APK.md            # Detailed guide
│   └── IMPROVEMENTS.md          # Feature list
│
└── 🎨 Assets
    ├── image.png                # Bird image
    └── angry-birds-drill...mp3  # Music
```

---

## 🚀 Let's Start!

**Choose one:**

### → Test on Windows NOW:
```powershell
.\setup.ps1
```

### → Build APK for Android:
```bash
# In WSL/Linux
./setup_linux.sh
```

### → Manual Quick Test:
```bash
pip install kivy
python main.py
```

---

## 💡 Pro Tips

1. **Test first** on PC before building APK
2. **First APK build takes long** (30-60 min) - be patient!
3. **Subsequent builds** are much faster (2-5 min)
4. **Clean builds** if you get errors: `buildozer android clean`
5. **Customize** game difficulty in `main.py`

---

## ✨ Next Steps After Setup

1. ✅ Play the game
2. ✅ Customize colors, difficulty
3. ✅ Add your own bird image
4. ✅ Change background music
5. ✅ Build APK and share with friends!

---

## 🤝 Support

If stuck:
1. Check error messages carefully
2. Review README_APK.md troubleshooting section
3. Ensure Python 3.8+ installed
4. Verify you're in correct directory

---

**Ready? Let's Go! 🎮🚀**

*Choose your path above and start playing or building!*
