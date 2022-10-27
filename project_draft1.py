#!/usr/bin/env python3
""" TLG NDE Python | LAncheta - larryancheta@duck.com |
    Python Project """

import socket

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

    while True:
        timeout = input(f"\nSpecify timeout (default = 5) --> ")
        if timeout == "":
            print(f"System will use default timeout of 5")
            break
        else:
            print(f"You entered --> {timeout}")
            break

    port_range = port.split("-")

    # Get IP address if host name is a domain
    try:
        ip = socket.gethostname(ip_domain)
    except Exception:
        print(f'Unable to resolve the domain')

    # if user only entered one port, program will only scan one port
    # otherwise, scan the range
    if len(port_range) < 2:
        scan_port(ip, port, timeout)
    else:
        for port in range(port_range[0], port_range[1]+1):
            scan_port(ip, port, timeout)

main()
