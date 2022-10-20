#!/usr/bin/python3
""" TLG NDE Python | LAncheta | Parsing Log Files """

def main():
    
    # parse keystone_common.wsgi and return number of failed login attempts
    loginfail = 0 # counter for fails
    # open the file for reading

    keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")
    keystone_file_lines = keystone_file.readlines()

    for x in keystone_file_lines:
        if "- - - - -] Authorization failed" in x:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
    print("The number of failed login attempts is ", loginfail)
    keystone_file.close() # close the open file

main()
