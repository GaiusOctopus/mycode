#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | NASA API #3 """

import requests

NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def returncreds():

    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def main():

    nasacreds = returncreds()
    
    startdate = input(f"Enter a start date >> ")
    print(f"Start date is >> ")
    enddate = input(f"Enter an optional end date >> ")
    print(f"End date is >> ")

    neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)

    neodata = neowrequest.json()

    print(neodata)

if __name__ == "__main__":
    main()
