import os
from .config import COLORS

def print_colored(text, color="ENDC"):
    print(f"{COLORS.get(color, '')}{text}{COLORS['ENDC']}")

def format_size(b):
    if not b:
        return "?"
    for unit in ['B', 'KB', 'MB', 'GB']:
        if b < 1024:
            return f"{b:.1f}{unit}"
        b /= 1024
    return f"{b:.1f}TB"

def format_time(seconds):
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}h{m:02d}m{s:02d}s" if h else f"{m}m{s:02d}s"

def display_banner():
    banner = r"""
 _____                   _                     _
|_   _|__ _ __  ___  ___(_)_ __ ___   ___   __| |___
  | |/ _ \ '_ \/ __|/ _ \ | '_ ` _ \ / _ \ / _` / __|
  | |  __/ | | \__ \  __/ | | | | | | (_) | (_| \__ \
  |_|\___|_| |_|___/\___|_|_| |_| |_|\___/ \__,_|___/
    """
    print_colored(banner, 'HEADER')
    print_colored("Universal Video Downloader v4.1", 'OKCYAN')