#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | Moving and Renaming Files and Folders """

import shutil # shell utilities will be used to move files
import os     # provides access to low level os operations (agnostic to flavor of OS)

def main():
    """called at runtime"""

    os.chdir("/home/student/mycode/") # move into this working directory

    shutil.move("raynor.obj", "ceph_storage") # try movng the file raynor.obj into ceph_storage/ dir

    # program will pause while we accept input
    xname= input("What is the new name for the kerrigan.obj? --> ") # collect string input from the user

    shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname) # moving kerrigan.obj into
                                                                      # ceph_storage/ with new name

main()
