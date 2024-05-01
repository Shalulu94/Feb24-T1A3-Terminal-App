# Sys imports
import random
import os
import time
from colored import Fore, Back, Style

# Local imports
from classes import Character
import character_creation
import battle_menu
import delay



# Welcome introductory text

os.system('clear')

delay.print_delay(f"{Fore.magenta}Welcome to {Style.bold}{Style.underline}Fight Night!{Style.reset}\n")
time.sleep(0.75)
delay.print_delay(f"{Fore.magenta}\nYou are about to enter a boxing tournament with the chance to be crowned the {Style.bold}{Style.underline}{Style.blink}World Boxing Champion!!{Style.reset}\n")
time.sleep(0.5)
delay.print_delay(f"{Fore.magenta}\nYou will compete in three consecutive matches.\n")
time.sleep(0.5)
delay.print_delay(f"\nDefeat all 3 opponents and be crowned the champion!\n")

time.sleep(1.5)

# os.system('clear')

# Enter the Main menu

def main_menu():
     
    user_input = 0
    

    while user_input != 4:
        try:
            
            delay.print_delay("\nPlease input a number out of the below options to continue:\n")
            time.sleep(0.75)
            delay.print_pause(f"\n{Fore.cyan}[1]{Style.reset} Create a new fighter")
            delay.print_pause(f"{Fore.cyan}[2]{Fore.magenta} Enter the Tournament")
            delay.print_pause(f"{Fore.cyan}[3] View fighter details")
            delay.print_pause(f"{Fore.cyan}[4] Exit Game")            

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
                print("That is an invalid selection. Please enter a number between 1 and 4")

        except ValueError:
            print("That's an invalid selection. Please enter a number between 1 and 4\n")
    

main_menu()