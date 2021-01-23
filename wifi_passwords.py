import os
import subprocess

path = "/etc/NetworkManager/system-connections"
os.chdir(path)
wifi_list = os.listdir()

wifi_pass = {}

for wifi in wifi_list:
  
    wifi_path = wifi.replace(" ", "\ ")
    ssid = subprocess.getoutput("cat " + wifi_path + " | " + "grep ssid=")
    psk = subprocess.getoutput("cat " + wifi_path + " | " + "grep psk=")
    wifi_pass[ssid.replace("ssid=","")] = psk.replace("psk=","")


for chaves in wifi_pass.keys():
    print("{0} : {1}".format(chaves, wifi_pass[chaves]))
