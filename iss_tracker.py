#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | ISS Tracker using API """

import requests
import datetime

def main():
    iss_api = requests.get("http://api.open-notify.org/iss-now.json").json()

    print(iss_api)
    print(type(iss_api))
    
    ts = iss_api["timestamp"]        
    lon = iss_api["iss_position"]["longitude"]
    lat = iss_api["iss_position"]["latitude"]
    
    time = datetime.datetime.fromtimestamp(ts)

    print(f"\n\n< CURRENT POSITION OF THE ISS AS OF {time} >\n Longitude: {lon}\n Latitude: {lat}\n")

main()
