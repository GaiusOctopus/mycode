#!/usr/bin/env python3
"""TLG NDE Python | LAncheta | CHALLENGE - Using Lists"""

def main():

    heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

    # PART 1
    # Print out your favorite character fromt his list! The output would look something like:
    # My favorite character is Black Panther!
    
    print(f"My favorite character is {heroes[2]}!")

    # PART 2
    # Ask the user to pick a number between 1 and 100.
    # Convert the input into an integer.

    pick= int(input("Pick a number between 1 and 100\n"))

    # PART 3
    # Check out https://docs.python.org/3/library/functions.html or go to Google.
    # Use a built-in function to find which integer in nums is the biggest.
    # Then, print out that number!

    nums= [1, -5, 56, 987, 0]

    print(max(nums))

main()

