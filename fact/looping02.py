#!/usr/bin/python3
"""" TLG NDE Pythong | LAncheta | Using for, range(), and with """

def main():
    
    # open file in read mode
    dnsfile = open("dnsservers.txt", "r")

    # create list of lines
    dnslist = dnsfile.readlines()

    # loop over lines
    for svr in dnslist:
        # print and end without a newline
        print(svr, end="") # the line we read ALREADY contains a \n (newline)

    # close the file (we created the list of lines)
    dnsfile.close() # best practice to close your file

main()
