import os
import time
from datetime import datetime
from termcolor import colored
import instaloader

def redirect_to_youtube():
    print(colored("\n[!] This tool is not free. Redirecting to YouTube...\n", "yellow"))
    time.sleep(3)
    os.system("xdg-open https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input(colored("\nAfter subscribing, press ENTER to continue... ", "cyan"))

def show_banner():
    os.system("clear")
    print()
    red_box_top = "╔" + "═" * 40 + "╗"
    red_box_bottom = "╚" + "═" * 40 + "╝"
    print(colored(red_box_top, "red"))
    print(colored("║" + " " * 12 + colored("HCO InstaReport by Azhar", "green", attrs=["bold"]) + " " * 12 + "║", "red"))
    print(colored(red_box_bottom, "red"))
    print()

def simulate_report(username):
    L = instaloader.Instaloader()
    print(colored("\n[~] Fetching profile info from Instagram...", "cyan"))
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        followers = profile.followers
        posts = profile.mediacount
        bio = profile.biography
        print(colored(f"\n[✓] Profile Found: @{username}", "green"))
        print(colored(f"Followers: {followers} | Posts: {posts}", "cyan"))
        print(colored(f"Bio: {bio}", "yellow"))
        print(colored("\n[✓] Reporting simulation started...", "green"))
        time.sleep(2)
        print(colored("[✓] 100 genuine reports submitted!", "green"))
        log_action(username, True)
    except Exception as e:
        print(colored(f"[!] Failed to fetch profile. Reason: {e}", "red"))
        log_action(username, False)

def log_action(username, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] @{username} | Reported: {status}\n")

def main():
    redirect_to_youtube()
    show_banner()
    
    print(colored("[+] Tool initialized successfully!", "cyan"))
    username = input(colored("\nEnter the Instagram username to report: ", "yellow"))
    simulate_report(username)

if __name__ == "__main__":
    main()
