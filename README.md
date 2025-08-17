# Universal-Video-Downloader
Universal Video &amp; Music Downloader - Fast, and cross-platform tool for Android (Termux), Linux &amp; Windows. Supports HD video, music downloads, quality selection, and built-in converter.

## • Features
- Supports multiple platforms (YouTube, Facebook, Instagram, Twitter/X)
- Fancy terminal progress bar
- Choose specific formats (video/audio)
- Auto-organized downloads

## 📦 Installation
```bash
git clone https://github.com/Koustubh12345/Universal-Video-Downloader-.git
cd Universal-Video-Downloader-
pip install -r requirements.txt

# Platform-Specific Instructions

## For Termux (Android)
```bash
# Update package lists
pkg update

# Install required packages
pkg install python ffmpeg

# Run the downloader
bash start.sh
```

### For Linux (Ubuntu/Debian)
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install python3 ffmpeg

# Run the downloader
bash start.sh
```

### For Windows
```powershell
# Install Python and FFmpeg first
# Then open Command Prompt/Terminal and run:
pip install -r requirements.txt
python -m uvd.uvd
```

### For macOS
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# Install dependencies
brew install python ffmpeg

# Run the downloader
bash start.sh
```

---

The downloader supports high-speed downloads (up to 100 MB/s) and provides detailed progress information during downloads.
