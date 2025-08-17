![Tensei](uvd/Tensei.jpg)
# Universal-Video-Downloader
Universal Video &amp; Music Downloader - Fast, and cross-platform tool for Android (Termux), Linux &amp; Windows. Supports HD video, music downloads, quality selection, and built-in converter.

## • Features
- Supports multiple platforms (YouTube, Facebook, Instagram, Twitter/X)
- Fancy terminal progress bar
- Choose specific formats
- Auto-organized downloads

## 📦 Installation
```bash
git clone https://github.com/Koustubh12345/Universal-Video-Downloader.git
cd Universal-Video-Downloader
pip install -r requirements.txt
```

### For Termux (Android)
```bash
pkg update

pkg install python ffmpeg

bash start.sh
```

### For Linux (Ubuntu/Debian)
```bash
sudo apt-get update

sudo apt-get install python3 ffmpeg

bash start.sh
```

### For Windows
```powershell
pip install -r requirements.txt

python -m uvd.uvd
```

### For macOS
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

brew install python ffmpeg

bash start.sh
```

---

The downloader supports high-speed downloads (up to 100 MB/s) and provides detailed progress information during downloads.
