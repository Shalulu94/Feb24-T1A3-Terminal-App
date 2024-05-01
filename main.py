# Sys imports
import random
import time
import os

# Local imports
from classes import Character
import character_creation
import battle_menu

# Delay print text
def print_pause(message):
    print(message)
    time.sleep(0.5)

# Welcome introductory text
print_pause("Welcome to Fight Night!")
print_pause("You are about to enter a boxing tournament with the chance to be crowned the World Boxing Champion!!")
print_pause("You will compete in three consecutive matches")
print_pause("Defeat all 3 opponents and be crowned the champion!\n")

# os.system('clear')

# Enter the Main menu

def main_menu():
     
    user_input = 0
    

    while user_input != 4:
        try:
            print("Please input a number out of the below options to continue:\n")
            print("1. Create a new fighter")
            print("2. Enter the Tournament")
            print("3. View fighter details")
            print("4. Exit Game")            

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
            print("That's an invalid selection. Please enter a number between 1 and 4")
    

main_menu()