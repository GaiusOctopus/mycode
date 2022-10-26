#!/usr/bin/python3
""" TLG NDE Python | LAncheta | Read from Files """

def main():
    
    ## create file object in read mode
    configfile = open("vlanconfig.cfg", "r")

    ## display file to the scree -.read()
    print(configfile.read())

    ## close file
    configfile.close()

    ## recreate file object to explore new method
    configfile = open("vlanconfig.cfg", "r")

    ## make a list of file lines - .readlines()
    configlist = configfile.readlines()
    print(configlist)

    ## iterate through configlist
    for x in configlist:
        print(x.strip())

    configfile.close()

main()
