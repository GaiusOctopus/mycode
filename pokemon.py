#!/usr/bin/env python3
""" TLG NDE Python | LAncheta |
    Practice With API Slicing - Pokemon Edition """

import requests
import wget

def main():
    pokenum = input("Pick a number between 1 and 151!\n> ")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi)
    print(type(pokeapi))

    print(f'{pokeapi["sprites"]["front_default"]}\n')
    imgurl = pokeapi["sprites"]["front_default"]
    wget.download(imgurl, "home/student/static/")

    for moves in pokeapi:
        print(moves["move"]["name"])

    games = 0
    for games in pokeapi["game_indices"]:
        games += 1
    print(f"This pokemon has appeared in {games} games!")

main()   
