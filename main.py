# Sys imports
import random
import os
import time

# Local imports
from classes import Character
import character_creation
import battle_menu
import delay
import style



# Welcome introductory text

os.system('clear')

delay.print_delay(f"{style.default}Welcome to {style.b_und}Fight Night!{style.default}\n")
time.sleep(0.75)
delay.print_delay(f"\nYou are about to enter a boxing tournament with the chance to be crowned the {style.b_und}World Boxing Champion!!{style.default}\n")
time.sleep(0.5)
delay.print_delay(f"\nYou will compete in three consecutive matches.\n")
time.sleep(0.5)
delay.print_delay(f"\nDefeat all 3 opponents and be crowned the champion!\n")

time.sleep(1.5)

# os.system('clear')

# Enter the Main menu

def main_menu():
     
    user_input = 0
    

    while user_input != 4:
        try:
            
            delay.print_delay(f"{style.default}\nPlease input a number out of the below options to continue:\n")
            time.sleep(0.75)
            delay.print_pause(f"\n{style.inp}[1]{style.default} Create a new fighter")
            delay.print_pause(f"{style.inp}[2]{style.default} Enter the Tournament")
            delay.print_pause(f"{style.inp}[3]{style.default} View fighter details")
            delay.print_pause(f"{style.inp}[4]{style.default} Exit Game")            

            user_input = int(input())
            
            
            if user_input == 1:
                character_creation.character_create()
            elif user_input == 2:
                battle_menu.battle_screen()
            elif user_input == 3:
                character_creation.character_details()
            elif user_input == 4:
                print("Thank you for playing!")
                break
            else:
                print(f"{style.err}That is an invalid selection. Please enter a number between 1 and 4")

        except ValueError:
            print(f"{style.err}That's an invalid selection. Please enter a number between 1 and 4\n")
    

main_menu()