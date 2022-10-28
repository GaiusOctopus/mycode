#!/usr/bin/env python3
""" TLG NDE Python | LAncheta - larryancheta@duck.com |
    Python Project """

import socket

def connect_to_ip(ip, port):
    if sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM):
        return sock
    else:
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
    while True:
        ip_domain = input("\nPlease enter a valid IP address or domain name --> ")
        
        if ip_domain == "":
            print(f"\nYou must specify a host!")
            continue
        else:
            print(f"\nYou entered --> {ip_domain}")
            break

    # Get port range from user
    while True:
        port = input("\nEnter the port range (example: 22-110) --> ")
        if port == "":
            print(f"\nYou must specify a port range!")
            continue
        else:
            print(f"\nYou entered --> {port}")
            break

    port_range = port.split("-")

    # Get IP address if host name is a domain
    
    ip = ip_domain

    if:
        ip = socket.gethostname(ip_domain)
    else:
        print(f'Unable to resolve the domain')

    # if user only entered one port, program will only scan one port
    # otherwise, scan the range
    if len(port_range) < 2:
        scan_port(ip, port, timeout)
    else:
        for port in range(int(port_range[0]), int(port_range[1])):
            scan_port(ip, port, timeout)

main()
