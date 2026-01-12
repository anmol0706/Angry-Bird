# 🚀 How to Build APK on Windows - Complete Guide

## ⚠️ Important: APK Building Requires Linux

**Buildozer** (the tool that creates APKs) only works on **Linux**. But don't worry! You have **3 options** to build your APK:

---

## 📋 **Option 1: Use WSL2 (Windows Subsystem for Linux)** ⭐ RECOMMENDED

This lets you run Linux on Windows without a virtual machine!

### **Step 1: Install WSL2**

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

**Then restart your computer.**

After restart, WSL will complete installation and ask you to:
- Create a username (lowercase, no spaces)
- Create a password

### **Step 2: Update WSL2**

After installation, open PowerShell and run:

```powershell
wsl --update
wsl --set-default-version 2
```

### **Step 3: Open WSL Terminal**

You can open WSL by:
- Searching "Ubuntu" in Start Menu, OR
- Running `wsl` in PowerShell

### **Step 4: Navigate to Your Project**

In WSL terminal:

```bash
cd /mnt/c/Users/anmol/Documents/eventdhara/akash/flappy_bird_game
```

### **Step 5: Make Setup Script Executable**

```bash
chmod +x setup_linux.sh
```

### **Step 6: Run Setup (15-20 minutes)**

```bash
./setup_linux.sh
```

This will install:
- Python packages (Kivy, Buildozer, Cython)
- Android build tools
- All dependencies

**Note:** It will ask for your password (the one you set during WSL installation).

### **Step 7: Build APK (30-60 minutes first time)**

After setup completes:

```bash
./build_apk.sh
```

**What happens:**
- Downloads Android SDK (~500 MB)
- Downloads Android NDK (~500 MB)
- Compiles Python for Android
- Packages your game as APK

**First build:** 30-60 minutes
**Subsequent builds:** 2-5 minutes

### **Step 8: Find Your APK**

After successful build:

```bash
ls -lh bin/*.apk
```

Your APK will be:
```
bin/flappybird-1.0-arm64-v8a-debug.apk
```

### **Step 9: Copy APK to Windows**

```bash
# Copy to Desktop
cp bin/*.apk /mnt/c/Users/anmol/Desktop/
```

Now you can transfer it to your Android phone!

### **Step 10: Install on Android**

1. Transfer APK to your phone (USB, email, cloud)
2. Open the APK file on phone
3. Allow "Install from unknown sources" if asked
4. Install and enjoy!

---

## 📋 **Option 2: Use GitHub Actions (Cloud Building)** ☁️ FREE

Build APK automatically in the cloud without installing anything!

### **How it works:**
1. Push your code to GitHub
2. GitHub builds APK automatically
3. Download ready APK

### **Setup:**

**1. Create `.github/workflows/build-apk.yml`:**

```yaml
name: Build APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install -y openjdk-17-jdk
        pip install buildozer cython
    
    - name: Build APK
      run: |
        buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: flappy-bird-apk
        path: bin/*.apk
```

**2. Push to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

**3. Download APK:**
- Go to GitHub → Actions tab
- Click on the workflow run
- Download the APK artifact

**Pros:**
- ✅ No local setup needed
- ✅ Free
- ✅ Automated

**Cons:**
- ❌ Requires GitHub account
- ❌ Takes 20-30 minutes per build

---

## 📋 **Option 3: Use Linux Virtual Machine**

If WSL doesn't work, use a Linux VM:

### **Method A: VirtualBox**
1. Download [VirtualBox](https://www.virtualbox.org/)
2. Download [Ubuntu ISO](https://ubuntu.com/download)
3. Create Ubuntu VM
4. Follow `setup_linux.sh` instructions

### **Method B: Docker**
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. Run Linux container
3. Mount your project folder
4. Build inside container

---

## 🔥 **Quick Troubleshooting**

### WSL Installation Issues

**Error: "WSL not enabled"**
```powershell
# Enable WSL feature
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# Enable Virtual Machine Platform
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Restart computer
```

**Error: "No distribution installed"**
```powershell
wsl --install -d Ubuntu
```

**WSL commands hang or slow:**
```powershell
# Restart WSL
wsl --shutdown
wsl
```

### Build Errors in WSL

**Error: "buildozer: command not found"**
```bash
pip3 install --user buildozer
export PATH=$PATH:~/.local/bin
```

**Error: "Permission denied"**
```bash
chmod +x setup_linux.sh
chmod +x build_apk.sh
```

**Error: "Java not found"**
```bash
sudo apt install openjdk-17-jdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```

**Error during build:**
```bash
# Clean and retry
buildozer android clean
rm -rf .buildozer
./build_apk.sh
```

---

## 📊 **Comparison Table**

| Method | Time | Difficulty | Cost | Best For |
|--------|------|------------|------|----------|
| **WSL2** | 1-2 hours | Medium | Free | Most users |
| **GitHub Actions** | 30 min | Easy | Free | Quick builds |
| **VirtualBox** | 2-3 hours | Hard | Free | If WSL fails |
| **Docker** | 1-2 hours | Hard | Free | Advanced users |

---

## 🎯 **Recommended Path for You**

Based on your Windows system, I recommend:

### **1. Try WSL2 First (Best option)**

```powershell
# PowerShell as Administrator
wsl --install
# Restart computer
# Then follow steps in Option 1
```

### **2. If WSL doesn't work, use GitHub Actions**

Fast, easy, and cloud-based!

---

## 💡 **Pro Tips**

1. **First APK build is SLOW** (30-60 min) - this is normal! ☕
2. **Subsequent builds are FAST** (2-5 min) ⚡
3. **Don't cancel the first build** - let it complete
4. **Use WiFi with good speed** - downloads ~1 GB of tools
5. **Keep your computer plugged in** - building uses CPU

---

## 📱 **After Building APK**

### **Testing the APK:**

1. **Enable Developer Mode** on Android:
   - Settings → About Phone
   - Tap "Build Number" 7 times

2. **Enable USB Debugging**:
   - Settings → Developer Options
   - Enable "USB Debugging"

3. **Install:**
   - Transfer APK to phone
   - Tap to install
   - Allow "Unknown sources"

### **Sharing the APK:**

- ✅ Share via email
- ✅ Upload to Google Drive
- ✅ Share via WhatsApp/Telegram
- ✅ Publish to Google Play Store (requires $25 fee)

---

## 🚀 **What to Do NOW**

### **Choose Your Method:**

#### **Method 1: WSL2 (Recommended)**
```powershell
# Open PowerShell as Administrator
wsl --install
# Restart computer
```

#### **Method 2: GitHub Actions**
```powershell
# Create GitHub repo
# Push your code
# Enable Actions
# Download APK
```

---

## 📞 **Need Help?**

If you're stuck:

1. **Check error messages** carefully
2. **Try Google/ChatGPT** with the exact error
3. **Clean and rebuild**: `buildozer android clean`
4. **Check disk space**: Need ~5 GB free

---

## ✅ **Success Checklist**

Before building, ensure:
- [ ] WSL2 installed (or GitHub repo ready)
- [ ] Internet connection is stable
- [ ] At least 5 GB free disk space
- [ ] `main.py` exists in project folder
- [ ] `buildozer.spec` exists
- [ ] Icon.png exists (optional but nice)

---

## 🎉 **After You Build**

Once you have the APK:

1. ✅ Test on your Android device
2. ✅ Share with friends and family
3. ✅ Customize game further
4. ✅ Consider publishing to Play Store

---

**Choose your method above and let's build that APK! 🚀📱**

**Questions? Check the troubleshooting section or README_APK.md for more details.**

---

**Good luck! You're almost there! 🎮🐦**
