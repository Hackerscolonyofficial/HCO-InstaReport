# ⚫ HCO-InstaReport

**HCO-InstaReport by Azhar**  
A powerful Termux-based tool to gather publicly available reports on any Instagram username using TOR and export logs easily.

---

## 📸 Features

- Username-based Instagram reporting
- Uses TOR for anonymity
- Clean CLI interface
- Auto logs export
- YouTube subscription check with redirect
- Fully Termux-compatible

---

## 🚀 Installation

```bash
pkg update && pkg upgrade
pkg install git tor python -y
git clone https://github.com/YourUsername/HCO-InstaReport
cd HCO-InstaReport
pip install -r requirements.txt
bash start.sh
```

---

## 📦 Requirements

- Python 3
- Tor installed and working
- Termux environment

---

## 🧠 How it Works

1. Redirects to YouTube for channel subscription
2. User confirms by pressing ENTER
3. Tool starts with banner: **HCO Insta Report by Azhar**
4. User enters Instagram username
5. Tool fetches report data
6. Report is exported as a `.txt` log file

---

## 📁 Folder Structure

```
HCO-InstaReport/
│
├── start.sh
├── main.py
├── insta_report.py
├── tor_config/
│   └── torrc
├── requirements.txt
└── README.md
```

---

## 📜 Example Output

```
[*] Starting Tor service...
[*] Connecting to Instagram...
[+] Target: @username
[+] Followers: 2.3M
[+] Following: 1
[+] Bio: Public Figure | Artist
[+] Posts: 56
[✓] Report exported: logs/username_report.txt
```

---

## 📺 YouTube Subscription Notice

> ⚠️ This tool is free but requires a **YouTube subscription** to continue.
After launching, you will be redirected to:  
**[Hackers Colony Tech YouTube Channel](https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya)**  
After subscribing, press `ENTER` to start using the tool.

---

## 🧑‍💻 Author

**Code by Azhar**  
🚩 Instagram: [@hackers_colony_official](https://www.instagram.com/hackers_colony_official)  
💬 Telegram: [HackersColony](https://t.me/hackersColony)  
🌐 Website: [HackersColony](https://hackerscolonyofficial.blogspot.com/?m=1)

---

## 📢 Disclaimer

This tool is created strictly for **educational purposes** and **ethical use only**.  
The author is **not responsible** for any misuse.

> “Hack the planet, but respect the rules.”
