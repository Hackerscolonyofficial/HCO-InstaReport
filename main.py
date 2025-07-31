import os
import time

# Clear the terminal
os.system("clear")

# Display HCO License Banner
print("\033[91m")
print("╔════════════════════════════════════════════╗")
print("║      🔒 HCO-INSTAREPORT TOOL               ║")
print("║  Protected by Hackers Colony License       ║")
print("║  Unauthorized Copying is Strictly Forbidden║")
print("╚════════════════════════════════════════════╝")
print("\033[0m")
time.sleep(1)

# Main Menu Function
def main_menu():
    while True:
        print("\n\033[96m=== HCO-InstaReport Menu ===\033[0m")
        print("1. Report Instagram Account")
        print("2. Report Instagram Post")
        print("3. Report Instagram Story")
        print("4. Report Instagram Comment")
        print("5. Exit")

        choice = input("\n\033[93m[+] Choose an option (1-5): \033[0m")

        if choice == '1':
            report_account()
        elif choice == '2':
            report_post()
        elif choice == '3':
            report_story()
        elif choice == '4':
            report_comment()
        elif choice == '5':
            print("\n\033[91m[!] Exiting HCO-InstaReport. Stay ethical.\033[0m")
            break
        else:
            print("\033[91m[!] Invalid choice. Please enter 1-5.\033[0m")

# Simulated Report Functions

def report_account():
    username = input("\nEnter Instagram username to report: @")
    reason = input("Reason for report (e.g., fake, spam, harassment): ")
    print("\033[92m\n[*] Reporting account...\033[0m")
    time.sleep(2)
    print(f"\033[92m[✓] Account @{username} reported for '{reason}' (simulation).\033[0m")

def report_post():
    link = input("\nEnter Instagram post URL: ")
    reason = input("Reason for report: ")
    print("\033[92m\n[*] Reporting post...\033[0m")
    time.sleep(2)
    print(f"\033[92m[✓] Post {link} reported for '{reason}' (simulation).\033[0m")

def report_story():
    username = input("\nEnter Instagram username whose story to report: @")
    reason = input("Reason for report: ")
    print("\033[92m\n[*] Reporting story...\033[0m")
    time.sleep(2)
    print(f"\033[92m[✓] Story from @{username} reported for '{reason}' (simulation).\033[0m")

def report_comment():
    comment = input("\nEnter Instagram comment text or URL: ")
    reason = input("Reason for report: ")
    print("\033[92m\n[*] Reporting comment...\033[0m")
    time.sleep(2)
    print(f"\033[92m[✓] Comment '{comment}' reported for '{reason}' (simulation).\033[0m")

# Start the program
if __name__ == "__main__":
    main_menu()
