import getmac
import subprocess
import serial
import time
uno = serial.Serial('/dev/ttyACM0', 9600)

macs = []

def monitor():
    for variant in range(19, 21):
        dest = "192.168.1." + str(variant)
        presence = subprocess.call(['ping', '-c', '1', dest])
        if presence == 0:
            mac = getmac.get_mac_address(ip=dest)
            macs.append(mac)
            print(macs)
def activate():
    uno.write(b'1')
def deactivate():
    uno.write(b'0')

while True:
    flag = 0
    monitor()
    print(macs)
    auth = '70:bb:e9:15:2d:11'

    for mac in macs:
        if str(mac) == str(auth):
            flag = 1
            break

    macs.clear()

    print('Gotha Flag' + str(flag))
    if flag==1:
        activate()
    if flag==0:
        deactivate()

# while True:
#     res = subprocess.call(['ping', '-c', '1', '192.168.1.3'])
#     print(res)
#     print(getmac.get_mac_address(interface='enp8s0', ip='192.168.1.3', network_request=True))
