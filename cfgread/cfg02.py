#!/usr/bin/python3
""" TLG NDE Python | LAncheta """

def main():
    
    configfile = open("vlanconfig.cfg", "r")

    configblog = configfile.read()

    configlist = configblog.splitlines()

    print(configlist)

    configfile.close()

main()
