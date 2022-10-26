#!/usr/bin/python3
"""" TLG NDE Pythong | LAncheta | Looping with 'for' Challenge! """

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
   
    type(farms)
    NE_farm= farms[0]["agriculture"]
    W_farm= farms[1]["agriculture"]
    SE_farm= farms[2]["agriculture"]
    vegetables=["carrots", "celery"]

    for x in NE_farm:
        print(f"The NE farm has {x}.")
    
    print("\n\nLet's find out what other farms have.\n")

    for farm in farms:
        print("-", farm["name"])
    farm_choice= input("\nPick a farm!\n\n")

    for farm in farms:
        if farm["name"].lower() == farm_choice.lower():
            for items in farm["agriculture"]:
                print(items)
                
    print("\nLet's find out what animals each farm has.\n")

    for farm in farms:
        print("-", farm["name"]
    farm_animals= input("\nPick a farm!\n")

    for farm in farms:
        if farm["name"].lower == farm_animals.lower():
            for items in farm["agriculture"]:
                if items not in vegetables:
                    print(items)    

main()  
