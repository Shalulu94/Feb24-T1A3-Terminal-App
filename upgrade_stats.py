from classes import Character
from classes import Opponent
import character_creation
import os

def upgrades():
   

    while character_creation.player.statpoints > 0:
        os.system('clear')

        print("Welcome to the upgrade menu")
        print("\nHere you will be able to spend available stat points to upgrade your fighter's stats")
        print(f"you currently have {character_creation.player.statpoints} available to use")
        print("\nPlease select from the following options:")
        print("1. Allocate stat points")
        print("2. View your fighter details")
        print("3. Return to previous menu")

        user_input = int(input("\nPlease input your selection between 1 and 3:\n"))

        if user_input == 1:
            
            os.system('clear')

            print("Please choose which stat you would like to upgrade:\n")
            print("[Attack] - Each additional point increases Attack by 25")
            print("[Defence] - Each additional point increases Defence by 25")
            print("[HP] - Each additional point increases HP by 150")

            upgrade_input = input("\nPlease type in which stat you would like to upgrade: ")
            upgrade_input_low = upgrade_input.lower()

            if upgrade_input_low == "attack":
                character_creation.player.attack += 25
                character_creation.player.statpoints -= 1
                print("\nAttack successfully upgraded!")
                input("\nPress Enter to return")

            elif upgrade_input_low == "defence":
                character_creation.player.defence += 25
                character_creation.player.statpoints -= 1
                print("\nDefence successfully upgraded!")
                input("\nPress Enter to return")

            elif upgrade_input_low == "hp":
                character_creation.player.hp += 25
                character_creation.player.statpoints -= 1
                print("\nHP successfully upgraded!")
                input("\nPress Enter to return")

            else:
                print("That is an invalid selection. Please type in your selection from the above fighter stats")

                user_input = 1

                input("Press Enter to try again")
                
        elif user_input == 2:
            character_creation.character_details()

        elif user_input == 3:
            break

        else:
            print("That's an invalid selection.")

            input("Press Enter to try again")

    if character_creation.player.statpoints == 0:
        os.system('clear')
    
        print("Welcome to the upgrade menu")
        print("\nHere you will be able to spend available stat points to upgrade your fighter's stats")
        print("\nYou currently do not have any statpoints available to spend")

        input("\nPress Enter to return to previous menu")
            

                             


    