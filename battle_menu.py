# Character creation
from classes import Character
from classes import Opponent
import opponents
import character_creation
import os
import battle
import upgrade_stats


def battle_screen():
    os.system('clear')

    user_input = 0

    if character_creation.player.battle_won > 0 and character_creation.player.battle_won <4:

        print("Congratulation's on your win!")
        print("\nYou've been awarded 3 stat points to upgrade your fighter")
        print("You can spend these stat points by visiting the upgrade menu from the locker room")

        input("\nPress Enter to return to the locker room")


    elif character_creation.player.battle_won == 4:
        print("Congratulation's you've defeated all of the opponent's and are crowned World Champion!!")

        input("\nPress enter to return to the locker room")

    else:
        pass
        
    

    try:

                
        while user_input != 5:

            os.system('clear')

            print(f"Welcome to the locker room {character_creation.player.first_name}!")
            print("\nHere you will be able to prepare for your upcoming match")
            print("\nWithin the locker room you can:")
            print("\n1. View your upcoming opponent")
            print("2. View your fighter details")
            print("3. Upgrade figher stats")
            print("4. Go to Battle!")
            print("5. Back to main menu")


            user_input = int(input("Please input a number out of the below options to continue: "))

            if user_input == 1:
                opponents.opponent()
            elif user_input == 2:
                character_creation.character_details()
            elif user_input == 3:
                upgrade_stats.upgrades()
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
    


    