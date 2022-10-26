#!/usr/bin/env python3
""" TLG NDE Python | LAncheta | Using Classes """

from cheatdicechallenge import *

def main():

    swapper = Cheat_Swapper()

    loaded_dice = Cheat_Loaded_Dice()

    weighted_dice = Cheat_Weighted()

    swapper_score = 0
    loaded_dice_score = 0
    weighted_dice_score = 0

    number_of_games = 100000
    game_number = 0

    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()
        weighted_dice.roll()

        swapper.cheat()
        loaded_dice.cheat()
        weighted_dice.roll()

        if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) == sum(swapper.get_dice()) == sum(weighted_dice.get_dice()):
            pass
        elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) > sum(weighted_dice.get_dice()):
            swapper_score += 1
        elif sum(loaded_dice.get_dice()) > sum(swapper.get_dice()) and sum(loaded_dice.get_dice()) > sum(weighted_dice.get_dice()):
            loaded_dice += 1
        else:
            weighted_dice_score += 1
        game_number += 1

    print("Simulation complete")
    print("===================")
    print("Final scores")
    print("===================")
    print(f'Swapper won: {swapper_score}')
    print(f'Loaded Dice won: {loaded_dice_score}')
    print(f'Weighted Dice won: {weighted_dice_score}')

    if swapper_score == loaded_dice_score and swapper_score == weighted_dice_score:
        print("Game was drawn")
    elif swapper_score > loaded_dice_score and swapper_score > weighted_dice_score:
        print("Swapper won most games")
    elif loaded_dice_score > swapper_score and loaded_score > weighted_dice_score:
        print("Loaded Dice won most games")
    else:
        print("Weighted Dice won most games")

if __name__ == "__main__":
    main()
