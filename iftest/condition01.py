#!/usr/bin/env python3
"""" TLG NDE Python | LAncheta | Testing "if" conditionals """

def main():

    ## Collect input from the user
    hostname= input("What value should we set for hostname? ==> ")
    
    ## use the lower method to test if input value matches expected value
    if hostname.lower()== "mtg":
        print("The hostname was found to be mtg")
        print("Hostname matches expected config")

    ## Always print out to the user
    print("Exiting the script")

main()
