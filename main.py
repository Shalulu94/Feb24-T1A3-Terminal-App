import random
import time
import os

def print_pause(message):
    print(message)
    time.sleep(1)

# Welcome introductory text
print_pause("Welcome to Fight Night!")
print_pause("You are about to enter a boxing tournament with the chance to be crowned the World Boxing Champion!!")
print_pause("You will compete in three consecutive matches")
print_pause("Defeat all 3 opponents and be crowned the champion!\n")

# os.system('clear')

# Enter the Main menu
def main_menu():
     
    user_input = 0
    print("Please input a selection out of the below options to continue:\n")

    while user_input != 4:
        try:
            
            print("1. Create a new fighter")
            print("2. Enter the Tournament")
            print("3. View fighter details")
            print("4. Exit Game")

            user_input = int(input())
            
            
            if user_input == 1:
                print("Take user to character creation screen")
            elif user_input == 2:
                print("Take user to pre-battle menu")
            elif user_input == 3:
                print("Take user to view fighter details")
            elif user_input == 4:
                print("Thank you for playing!")
                break
            else:
                print("That is an invalid selection. Please enter a number between 1 and 3")

        except ValueError:
            print("That's not a number. Please enter a number between 1 and 3")
    

main_menu()