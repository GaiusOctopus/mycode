#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | Working with APIs """

import requests

def main():
      
    """ runtime code """
    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    print(dir(resp))

if __name__ == "__main__":
    main()
