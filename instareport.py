import requests
import time
import os
import socks
import socket
from stem import Signal
from stem.control import Controller
from tor_config import renew_tor_ip

# Set SOCKS proxy for TOR
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

# Banner
def banner():
    os.system("clear")
    print("\033[1;91m")
    print("════════════════════════════════════════")
    print("        HCO-InstaReport by Azhar")
    print("════════════════════════════════════════")
    print("\033[1;92m[+] Tool to report fake Instagram accounts")
    print("\033[1;91m[+] Powered by TOR for anonymity")
    print("\033[0m")

# Report logic
def send_report(username):
    url = "https://www.instagram.com/users/report/"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-CSRFToken": "dummy",  # Optional for simulation
    }

    data = {
        "username": username,
        "reason": "It's pretending to be someone else",  # Static reason for now
    }

    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        if response.status_code == 200:
            print(f"\033[92m[✓] Report sent successfully to @{username}\033[0m")
        else:
            print(f"\033[91m[✗] Failed to report @{username} – Code {response.status_code}\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Error: {e}\033[0m")

# Main function
def main():
    banner()
    username = input("\n\033[1;92mEnter Instagram username to report: \033[0m@")
    reports = int(input("\033[1;92mHow many times to report? \033[0m"))

    print("\n\033[1;93m[!] Starting TOR-based Instagram reporting...\033[0m\n")
    time.sleep(1)

    for i in range(1, reports + 1):
        send_report(username)
        time.sleep(2)

        if i % 5 == 0:
            print("\033[94m[*] Rotating IP using TOR...\033[0m")
            renew_tor_ip()
            time.sleep(3)

    print("\n\033[1;92m[✓] Done reporting. Stay ethical.\033[0m")

if __name__ == "__main__":
    main()
