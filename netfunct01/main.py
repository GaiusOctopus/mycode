#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | Functions """

import json

# function to push commands
def commandpush(devicecmd):
    for ip in devicecmd.keys():
        print(f'Handshaking. .. ... connecting with {ip}')
        for mycmds in devicecmd[ip]:
            print (f'Attempting to send command --> {mycmds}')
    return None

def devicereboot(devicecmd):
    for ip in devicecmd.keys():
        print(f'Connecting to.. {ip}')
        print("REBOOTING NOW!")
    return None

def main():
    """ called at runtime """
    devicecmd = {"10.1.0.1": ["interface eth1/2", "no shutdown"], "10.2.0.1": 
    ["interface eth1/1", "shutdown"], "10.3.0.1": ["interface eth1/5", "no shutdown"]}

    print("Welcome to the network device command pusher")

    print("\nData set found\n")

    commandpush(devicecmd)
    devicereboot(devicecmd)

main()
