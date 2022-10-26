#!/usr/bin/python3
""" TLG NDE Python | LAncheta """

def main():

    with open("vlanconfig.cfg", "r") as configfile:
        configlist = configfile.readlines()
        configfile.seek(0, 0)
        lines = len(configfile.readlines())

    for x in configlist:
        print(x.strip())

    print(f"\nTotal number of lines: {lines}\n")

main()
