# Character creation
import os
import time

from classes import Character
from classes import Opponent
import opponents
import character_creation
import battle
import upgrade_stats
import delay


def battle_screen():
    os.system('clear')

    user_input = 0

    try:

                
        while user_input != 5:

            if character_creation.player.battle_won == 3:
                os.system('clear')
                
                delay.print_delay("Congratulation's you've defeated all of the opponent's and are crowned World Champion!!\n")
                delay.print_delay("\nPress enter to return to the locker room")
                input()

         
            os.system('clear')

            delay.print_delay(f"Welcome to the locker room {character_creation.player.first_name}!\n")
            delay.print_delay("\nHere you will be able to prepare for your upcoming match\n")
            time.sleep(0.75)

            delay.print_delay("\nWithin the locker room you can:\n")
            time.sleep(0.75)

            delay.print_pause("\n[1] View your upcoming opponent")
            delay.print_pause("[2] View your fighter details")
            delay.print_pause("[3] Upgrade fighter stats")
            delay.print_pause("[4] Go to Battle!")
            delay.print_pause("[5] Back to main menu\n")

            delay.print_delay("\nPlease input a number out of the above options to continue: ")
            user_input = int(input())

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
    


    