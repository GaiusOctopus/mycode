#!/usr/bin/python3
""" TLG NDE Python | LAncheta | Using getpass """

# A simple Python program to demonstrate  getpass.getpass() to read password 
import getpass 

def main():
    p = getpass.getpass() 
    print("Password entered:", p)
    
if __name__ == "__main__":
    main()
