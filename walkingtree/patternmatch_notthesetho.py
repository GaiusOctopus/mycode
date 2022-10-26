#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | OS Directory Except """

import os
import fnmatch

EXCLUDE = ["/usr/", "/home", "/var"]

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE:
            dirs[:] = []
            files[:] = []
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))

        return result

def main():
    lookfor = input("What pattern am I looking for (e.g.: *.txt or *.cfg)? --> ")
    lookwhere = input("What is the path in which I should search? --> ")
    print("Results: ", find(lookfor, lookwhere))

main()
