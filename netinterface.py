#!/usr/bin/env python3
""" Docstring """

import netifaces

# print(type(netifaces.interface()))

netread = netifaces.interfaces()

for i in netread:
    print('\n**********Details of Interface - ' + i + ' ***********')
    try:
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
