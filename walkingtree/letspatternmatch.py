#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | OS Pattern Search """

import os, fnmatch

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))

    return result

lookfor = input("What pattern am I looking for (e.g.: *.txt or *.cfg)? --> ")
lookwhere = input("What is the path in which I should search? --> ")

print(find(lookfor, lookwhere))
