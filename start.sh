#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\e[91m"
figlet "HCO-InstaReport"
echo -e "\e[0m"
echo
echo -e "\e[92mThis tool is not free. Redirecting to YouTube in 10s...\e[0m"
sleep 10
termux-open-url https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya
read -p "Press ENTER to continue..."

clear
echo -e "\e[41m\e[92m"
figlet "HCO-InstaReport"
echo -e "\e[0m"
echo -e "\e[1;91mDeveloped by Azhar | Hackers Colony Official\e[0m"
echo

python main.py
