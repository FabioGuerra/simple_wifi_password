#!/usr/bin/env python3

import subprocess
import re

print("\n[+] Search for wifi passwords (Linux OS)")
print("[+] SSID: PASS\n")

path = "/etc/NetworkManager/system-connections"

wifi = subprocess.getoutput("cd " + path + " && ls")
wifi_ssid = re.compile("[a-z0-9A-Z -_]+.nmconnection") # search for ssid RE

wifi_dump = wifi_ssid.findall(wifi)
wifi_pass = {} 

for ssid in wifi_dump:
    
    str_ssid = ssid.replace(" ", "\ ")
    full_path = path + "/" + str_ssid
   
    CMD  = "cat " + full_path +  "|" + "grep " + "psk=" 
    
    # cat /etc/NetworkManager/system-connections/{ssid}.nmconnection | grep psk=
    
    password = subprocess.getoutput(CMD)

    str_ssid = str_ssid.replace("\ ", " ")
    str_ssid = str_ssid.replace(".nmconnection", "")
    wifi_pass[str_ssid] = password.replace("psk=", "")
    print("{0}: {1}".format(str_ssid, wifi_pass[str_ssid]))


print()

