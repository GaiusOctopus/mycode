#!/usr/bin/python3
""" TLG NDE Python | LAncheta | Astronauts using request """

import requests

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    groundctrl = requests.get(MAJORTOM)

    helmetson = groundctrl.json()

    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

    for iss in helmetson["people"]:
        print(iss["name"] + " on the " + iss["craft"]) 

if __name__ == "__main__":
    main()
