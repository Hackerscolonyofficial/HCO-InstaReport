#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

clear
echo -e "${YELLOW}[!] This tool is not free. Redirecting to YouTube...${NC}"
sleep 3
xdg-open "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"

echo
read -p "$(echo -e ${CYAN}After subscribing, press ENTER to continue...${NC})"

# Clear and show box
clear
echo
echo -e "${RED}╔════════════════════════════════════════════╗"
echo -e "${RED}║            ${GREEN}HCO InstaReport by Azhar${RED}            ║"
echo -e "${RED}╚════════════════════════════════════════════╝${NC}"
echo

# Run main tool
python main.py
