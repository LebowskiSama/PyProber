import os
import time
import getmac
import serial # To interface with Uno board
from subprocess import Popen, DEVNULL # Popen to ping parallelly
from tabulate import tabulate

uno = serial.Serial('/dev/ttyACM0', 9600) # Interface Uno

p = {} # ip process dictionary
devices = [] # to store mac addresses present

def monitor():
    
    for n in range(2, 50):

        ip = "192.168.1.%d" % n
        p[ip] = Popen(["ping", "-n", "-w5", "-c3", ip], stdout=DEVNULL)

    while p: # Perform while the pinging process is active
        for ip, proc in p.items():
            if proc.poll() is not None:
                del p[ip] # Remove the ip from the dict to continue the while forward
                if proc.returncode == 0:
                    devices.append([ip, getmac.get_mac_address(ip=ip)])# Fetch and append mac addresses of devices present in localnet
                break

    # Tabulate the data
    print(tabulate(devices, headers=["IP", "MAC"], tablefmt="pretty"))

    
def activate():
    uno.write(b'1')
def deactivate():
    uno.write(b'0')

while True:

    flag = 0
    monitor()

    auth = ['70:bb:e9:15:2d:11']

    for device in devices:
        for mac in auth:
            if str(device[1]) == mac:
                valid = device[1]
                flag = 1
                break

    devices.clear()

    if flag==1:
        activate()
        print(valid + " is present. Unlocked.")

    if flag==0:
        deactivate()
        print("No devices found, Locked")