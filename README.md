GhostRAT-Lite 👻

APT1 (Unit 61398) Adversary Emulation C2 Framework
Developed for Operation GhostUnit — ST6049CEM Managing Red Teams and Pen Tests
Softwarica College of IT & E-Commerce | Coventry University
Student: Aabishkar Roka | ID: 230476


⚠️ Disclaimer
This tool was developed strictly for educational purposes as part of an academic red team simulation exercise. All testing was conducted within an isolated VirtualBox lab environment with no connection to live systems or real networks. The author does not condone or support any malicious use of this software. Use only in controlled, authorised lab environments.

📋 Overview
GhostRAT-Lite is a lightweight Python-based Command and Control (C2) framework developed to emulate the operational behaviour of APT1's historically documented backdoors specifically WEBC2 and POISONIVY. The framework was built as part of Operation GhostUnit, a structured adversary emulation exercise mapped entirely to the MITRE ATT&CK Enterprise Framework.
The key design goal of GhostRAT-Lite is to disguise all C2 traffic as normal web activity HTTP GET requests are disguised as jQuery library fetches, and command results are returned via endpoints mimicking Google Analytics calls. This replicates the exact communication pattern documented in the Mandiant APT1 Intelligence Report (2013).

🔧 Installation & Setup
Requirements

Kali Linux (Attacker)
Windows 10 Pro (Victim)
VirtualBox Host-Only Network
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


👨‍💻 Author
Aabishkar Roka
Student ID: 230476
Module: ST6049CEM — Managing Red Teams and Pen Tests
Softwarica College of IT & E-Commerce | Coventry University
Module Leader: Nirmal Dahal
