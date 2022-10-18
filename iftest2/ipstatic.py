#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | IPv4 Testing with if """

def main():
    ipchk= "192.168.0.1"

    # a string tests as True
    if ipchk:
        print("Looks like the IP address was set: " + ipchk)

main()
