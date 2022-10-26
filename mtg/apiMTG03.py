#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | MTG API """

import requests

API = "http://api.magicthegathering.io/v1/"

def main():
    """ runtime code """

    resp = requests.get(f"{API}sets")

    print(resp.jason())

if __name__ == "__main__":
    main()
