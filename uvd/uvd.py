#!/usr/bin/env python3
from .utils import print_colored
from .downloader import download_from_url

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

def main():
    display_banner()
    while True:
        print_colored("\n🌐 Supported Platforms:", 'OKGREEN')
        print_colored("1. YouTube Video", 'OKCYAN')
        print_colored("2. YouTube Music/Audio", 'OKCYAN')
        print_colored("3. Facebook (Video)", 'OKCYAN')
        print_colored("4. Instagram (Video)", 'OKCYAN')
        print_colored("5. X (Twitter) (Video)", 'OKCYAN')
        print_colored("6. Exit", 'OKCYAN')
        choice = input("\nSelect platform (1-6): ").strip()
        if choice == '1':
            download_from_url(input("🔗 Enter YouTube URL: ").strip(), mode="video")
        elif choice == '2':
            download_from_url(input("🔗 Enter YouTube/Music URL: ").strip(), mode="audio")
        elif choice == '3':
            download_from_url(input("🔗 Enter Facebook URL: ").strip(), mode="video")
        elif choice == '4':
            download_from_url(input("🔗 Enter Instagram URL: ").strip(), mode="video")
        elif choice == '5':
            download_from_url(input("🔗 Enter Twitter/X URL: ").strip(), mode="video")
        elif choice == '6':
            print_colored("Exiting...", 'OKCYAN')
            break
        else:
            print_colored("Invalid choice.", 'FAIL')

if __name__ == "__main__":
    main()
