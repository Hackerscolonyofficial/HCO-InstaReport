#!/data/data/com.termux/files/usr/bin/bash

# Clear screen
clear

# Show HCO License Protection Banner
echo -e "\e[1;91m"
echo "╔════════════════════════════════════════════╗"
echo "║      🔒 HCO-INSTAREPORT TOOL               ║"
echo "║  Protected by Hackers Colony License       ║"
echo "║  Unauthorized Copying is Strictly Forbidden║"
echo "╚════════════════════════════════════════════╝"
echo -e "\e[0m"
sleep 2

# Display Not Free Message
echo -e "\e[1;91m[!] WARNING: This tool is not free to use.\e[0m"
echo -e "\e[1;92m[*] Redirecting you to our official YouTube channel...\e[0m"
sleep 2

# Auto-redirect to YouTube channel
am start https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya > /dev/null 2>&1
sleep 1

# Ask user to continue after subscribing
echo ""
read -p $'\e[1;93m[+] After subscribing, press ENTER to continue...\e[0m'

# Final confirmation message
echo -e "\n\e[1;94m[*] Thank you for your support!\e[0m"
echo -e "\e[1;92m[*] Starting the HCO-InstaReport tool now...\e[0m"
sleep 1

# Run the main Python script
python main.py
