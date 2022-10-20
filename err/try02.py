#!/usr/bin/python3
""" TLG NDE Python | LAncheta | try and except 2 """

def main():
    
    while True:
        try:
            print("Let's divite x by y!")
            x = int(input("What is the integer value of x? "))
            y = int(input("What is the integer value of y? "))
            print("the value of x/y: ", x/y)
        except ZeroDivisionError as zerr:
            print("Handling run-time error:", zerr)
        # general error handling
        # a practical use might be exceptions we haven't designed solution foryet
        except Exception as err:
            # sys.exc_info returns a 3 tuple with info about the exception handled
            print("We did not anticipate that: ", err)

main()
    
