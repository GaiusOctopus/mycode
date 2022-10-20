#!/usr/bin/python3
""" NDE TLG Python | LAncheta | Using for, range(), and with #2 """

def main():
    with open("dnsservers.txt", "r") as dnsfile:
        # indent to keep the dnsfile object open
        # create a list of lines
        dnslist = dnsfile.readlines()
        # loop over lines
        for svr in dnslist:
            # print and end without a newline
            print(svr, end="")

        # no need to close our file - closed automatically

main()
