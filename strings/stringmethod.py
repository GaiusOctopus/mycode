#!/usr/bin/env python3
"""TLG NDE Python | LAncheta
    String Method"""

def main():
    """ Runtime Code"""

    lilstring = "Alta3 Research offers classes on Python coding"
    newlist = lilstring.split(" ")
    print (newlist)

    myiplist = ["192", "168", "0", "12"]
    singleip = ".".join(myiplist)
    print(singleip)

main()

