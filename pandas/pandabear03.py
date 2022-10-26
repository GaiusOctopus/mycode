#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | Combining Data with Panda """

import pandas as pd

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    print(ciscocsv.head())

    ciscodf = pd.concat([ciscocsv, ciscojson])

    print(ciscodf)

if __name__ == "__main__":
    main()
