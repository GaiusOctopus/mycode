#!/usr/bin/env python3
""" TLG NDE Python | LAncheta - larryancheta@duck.com |
    Python Project """

import socket
import sys

def connect_to_ip(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return sock
    except Exception:
        return None

def scan_port(ip, port, timeout):
    socket.setdefaulttimeout(timeout)
    sock = connect_to_ip(ip, port)

    if sock:
        print(f'Able to connect to: {0}:{1}').format(ip, port)
        sock.close()
    else:
        print(f'Unable to connect to: {0:1}').format(ip, port)

def main():
    # Get IP / domain from user
    ip_domain = input("Please enter a valid IP address or domain name >> ")
    while ip_domain() == "":
        try:
            ip_domain = input("Please enter a valid IP address or domain name")
            print(f"You entered >> {ip_domain}")
        except: 
            print(f'You must specify a host!')
        

    # Get port range from user
    port = input('Enter the port range (example: 22-110) >> ')
    if port == "":
        print(f'You must specify a port range!')
        sys.exit(0)

    timeout = input(f'Specify timeout (default = 5) >> ')
    if not timeout:
        timeout = 5

    port_range = port.split("-")

    # Get IP address if host name is a domain
    try:
        ip = socket.gethostname(ip_domain)
    except Exception:
        print(f'Unable to resolve the domain')
        sys.exit(1)

    # if user only entered one port, program will only scan one port
    # otherwise, scan the range
    if len(port_range) < 2:
        scan_port(ip, int(port), int(timeout))
    else:
        for port in range(int(port_range[0]), int(port_range[1]+1)):
            scan_port(ip, int(port), int(timeout))

main()
