#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | NASA API #2  """

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def returncreds():
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()

    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def main():
    nasacreds = returncreds()
    
    # date = input("What day would you like to see the APOD of?\n[YYYY-MM-DD]\n> ")
    
    apodresp = requests.get(NASAAPI + nasacreds)
    
    apod = apodresp.json()

    print(apod)
    print(type(apod))

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()
