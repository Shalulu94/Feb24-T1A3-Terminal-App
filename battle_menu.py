# Character creation
from classes import Character
from classes import Opponent
import opponents
import character_creation
import os
import battle


def battle_screen():
    os.system('clear')

    user_input = 0

    try:

                
        while user_input != 5:

            print(f"Welcome to the locker room {character_creation.player.first_name}!")
            print("\nHere you will be able to prepare for your upcoming match")
            print("\nWithin the locker room you can:")
            print("\n1. View your upcoming opponent")
            print("2. View your fighter stats")
            print("3. Upgrade figher stats")
            print("4. Go to Battle!")
            print("5. Back to main menu")


            user_input = int(input("Please input a number out of the below options to continue: "))

            if user_input == 1:
                opponents.opponent()
            elif user_input == 2:
                character_creation.character_details()
            elif user_input == 3:
                print("View character upgrade screen")
            elif user_input == 4:
                battle.battle_sim()
            elif user_input == 5: 
                os.system('clear')
                break
            else:
                print("That is an invalid selection. Please enter a number between 1 and 3")
    
    
    
    except NameError:
        print("You haven't created a fighter yet!")
        print("Please return to the main menu to create a new fighter")

        input("\nPress Enter to return back to the battle menu")

        os.system('clear')
    


    