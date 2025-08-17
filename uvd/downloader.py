import os
from yt_dlp import YoutubeDL
from .utils import print_colored
from .progress import fancy_progress_hook
from .config import OUTPUT_DIR

def list_formats(info):
    formats = info.get("formats", [])
    print_colored("\n🎥 Available Formats:", 'OKGREEN')
    print_colored(f"{'ID':<6} {'Res':<8} {'FPS':<4} {'Size':<10} {'Ext'}", 'OKCYAN')
    valid = []
    from .utils import format_size
    for f in formats:
        if f.get("vcodec") != "none":
            h = f.get("height", "?")
            fps = f.get("fps", "?")
            size = format_size(f.get("filesize") or f.get("filesize_approx"))
            print(f"{f['format_id']:<6} {str(h)+'p':<8} {str(fps):<4} {size:<10} {f.get('ext','?')}")
            valid.append(f['format_id'])
    return valid

def list_audio_formats(info):
    formats = info.get("formats", [])
    print_colored("\n🟢 Available Audio Formats:", 'OKGREEN')
    print_colored(f"{'ID':<6} {'ABR':<8} {'Size':<10} {'Ext'}", 'OKCYAN')
    valid = []
    from .utils import format_size
    for f in formats:
        if f.get("acodec") != "none" and (f.get("vcodec") == "none" or f.get("height") is None):
            abr = f.get("abr", "?")
            size = format_size(f.get("filesize") or f.get("filesize_approx"))
            print(f"{f['format_id']:<6} {str(abr)+'kbps':<8} {size:<10} {f.get('ext','?')}")
            valid.append(f['format_id'])
    return valid

def download_from_url(url, mode="video"):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    base_opts = {
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'progress_hooks': [fancy_progress_hook],
        'quiet': True,
        'no_warnings': True,
        'noprogress': True
    }

    try:
        with YoutubeDL(base_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', '?')
            
            print_colored(f"\n📺 Title: {title}", 'OKGREEN')
            
            if mode == "audio":
                formats = list_audio_formats(info)
                if not formats:
                    print("⚠ No audio formats available.")
                    return
                choice = input("\n🎯 Enter audio format ID (or Enter for best audio): ").strip()
                base_opts['format'] = choice if choice and choice in formats else "bestaudio"
            else:
                formats = list_formats(info)
                if not formats:
                    print("⚠ No video formats available.")
                    return
                choice = input("\n🎯 Enter format ID (or press Enter for best): ").strip()
                base_opts['format'] = choice if choice and choice in formats else 'bestvideo+bestaudio/best'
                
        with YoutubeDL(base_opts) as ydl:
            ydl.download([url])
            
    except Exception as e:
        print_colored(f"\nError: {e}", 'FAIL')
