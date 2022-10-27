#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | Network Interfaces """

import netifaces

print(netifaces.interfaces())


i  = input(f'Enter the name of {i}')
print(f'Enter the interface name>> ')
print('\n****** details of interface - ' + i + ' ******')
print('MAC: ', end='') # This print statement will always print MAC without an end of line
print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
