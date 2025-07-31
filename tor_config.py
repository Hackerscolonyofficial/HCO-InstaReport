from stem import Signal
from stem.control import Controller

def renew_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='hco123')  # Change to your TOR password if different
            controller.signal(Signal.NEWNYM)
            print("[*] TOR IP rotated successfully.")
    except Exception as e:
        print(f"[!] Failed to rotate TOR IP: {e}")
