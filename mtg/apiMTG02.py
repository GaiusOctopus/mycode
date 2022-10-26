#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | MTG API """

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    """ runtime code """
    resp = requests.get(f"{API}sets")

    print(dir(resp))

if __name__ == "__main__":
    main()
