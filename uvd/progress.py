import shutil
import sys
import time
from .utils import format_size, format_time, print_colored
start_time = None
_PANEL_LINES = 9

def _line(n):
    h = shutil.get_terminal_size().lines
    return f"\033[{h - _PANEL_LINES + n};0H"

def fancy_progress_hook(d):
    global start_time
    if d['status'] == 'downloading':
        if start_time is None:
            start_time = time.time()
        total  = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
        loaded = d.get('downloaded_bytes', 0)
        speed  = d.get('speed', 0) or 0
        eta    = d.get('eta', 0) or 0
        percent = 0 if total == 0 else loaded / total * 100
        bar_len = 12
        filled  = max(1, int(bar_len * percent // 100))
        bar     = "⬢" * filled + "⬡" * (bar_len - filled)
        done_str  = format_size(loaded)
        total_str = format_size(total)
        speed_str = format_size(speed) + "/s"
        elapsed   = int(time.time() - start_time)
        total_est = int(elapsed / max(percent, 0.001) * 100) if percent else 0
        remain    = format_time(eta)
        
        # Enhanced status messages
        status_msg = "Downloading Video" if d.get('vcodec') != "none" else "Extracting Audio"
        panel = (
            f"{_line(0)}1. {d.get('filename','Download')[:50]}\n"
            f"{_line(1)}Task By yt-dlp (#ID429367486)\n"
            f"{_line(2)}┟ [{bar}] {percent:5.2f}%\n"
            f"{_line(3)}┠ Processed → {done_str} of {total_str}\n"
            f"{_line(4)}┠ Status → {status_msg}\n"
            f"{_line(5)}┠ Speed → {speed_str}\n"
            f"{_line(6)}┠ Time → {format_time(elapsed)} of {format_time(total_est)} ({remain})\n"
            f"{_line(7)}┠ Engine → yt-dlp ┖ Out Mode → #Local"
        )
        sys.stdout.write(panel)
        sys.stdout.flush()
    elif d['status'] == 'finished':
        # Clear progress panel
        blank = " " * shutil.get_terminal_size().columns
        for i in range(_PANEL_LINES):
            sys.stdout.write(_line(i) + blank)
        sys.stdout.write(_line(0))
        print_colored("✅ Download completed!", "OKGREEN")
        start_time = None
