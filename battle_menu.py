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
import style


def battle_screen():
    os.system('clear')

    user_input = 0

    try:

                
        while user_input != 5:

            if character_creation.player.battle_won == 3:
                os.system('clear')
                
                delay.print_delay(f"{style.default}Congratulation's you've defeated all of the opponent's and are crowned {style.defbu}World Champion!!\n")
                delay.print_delay(f"\n{style.default}Press enter to return to the locker room")
                input()

         
            os.system('clear')

            delay.print_delay(f"{style.default}Welcome to the locker room {character_creation.player.first_name}!\n")
            delay.print_delay("\nHere you will be able to prepare for your upcoming match\n")
            time.sleep(0.75)

            delay.print_delay("\nWithin the locker room you can:\n")
            time.sleep(0.75)

            delay.print_pause(f"\n{style.inp}[1]{style.default} View your upcoming opponent")
            delay.print_pause(f"{style.inp}[2] {style.default}View your fighter details")
            delay.print_pause(f"{style.inp}[3] {style.default}Upgrade fighter stats")
            delay.print_pause(f"{style.inp}[4] {style.default}Go to Battle!")
            delay.print_pause(f"{style.inp}[5] {style.default}Back to main menu\n")

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
                print(f"{style.err}That is an invalid selection. Please enter a number between 1 and 3{style.default}")
    
    
    
    except NameError:
        print(f"{style.err}You haven't created a fighter yet!")
        print("Please return to the main menu to create a new fighter")

        input(f"\nPress Enter to return back to the battle menu{style.default}")

        os.system('clear')

    except AttributeError:
        print(f"{style.err}You haven't created a fighter yet!")
        print("Please return to the main menu to create a new fighter")

        input(f"\nPress Enter to return back to the battle menu{style.default}")

        os.system('clear')
    


    