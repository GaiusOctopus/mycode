#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | Network Interfaces """

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
