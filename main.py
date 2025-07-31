import os
import time
import requests
from stem import Signal
from stem.control import Controller

def renew_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="hco1234")
        controller.signal(Signal.NEWNYM)

def send_report(username):
    url = "https://www.instagram.com/users/report/"
    headers = {
        "User-Agent": "Mozilla/5.0",
    }
    data = {
        "report_type": "It's pretending to be someone else",
        "scammer": username
    }
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        if response.status_code == 200:
            print(f"\033[92m[+] Report sent for: {username}\033[0m")
        else:
            print(f"\033[91m[-] Failed to report {username}\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Error: {str(e)}\033[0m")

def main():
    os.system("tor &")
    time.sleep(5)

    username = input("\033[96mEnter the scam/fake Instagram username: \033[0m")
    reports = int(input("Number of reports to send: "))
    ip_change_interval = 5

    for i in range(reports):
        send_report(username)
        if (i + 1) % ip_change_interval == 0:
            print("\033[93m[*] Changing IP using TOR...\033[0m")
            renew_ip()
            time.sleep(8)

    print("\n\033[1;92m[✓] All reports completed.\033[0m")

if __name__ == "__main__":
    main()
