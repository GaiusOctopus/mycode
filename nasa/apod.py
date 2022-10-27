#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | NASA API """

import urllib.request
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():

    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    nasacreds = "api_key=" + nasacreds.strip("\n")

    date = input(f'Enter date for that day\'s APOD [YYYY-MM-DD]>> ')
    print(f'\nLooking up APOD from {date}... ... ...\n')
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds + "&date=" + date)

    apodread = apodurlobj.read()

    apod = json.loads(apodread.decode("utf-8"))

    print("\n\nConverted Python data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

if __name__ == "__main__":
    main()
