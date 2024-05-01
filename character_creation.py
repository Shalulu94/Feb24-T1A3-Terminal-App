import os
import time

from classes import Character
import delay



def character_create():
    
    try:
        os.system('clear')

        delay.print_delay("Welcome to the fighter creation menu\n")
        delay.print_delay("Here you will be able to create a new fighter to compete with in the boxing championship!\n")
        time.sleep(0.75)


        delay.print_delay("Please enter your fighter's first name: ")
        player_firstname = input()

        delay.print_delay("Please enter your fighter's last name: ")
        player_lastname = input()

        delay.print_delay("Please enter your fighter's nickname: ")
        player_alias = input()

        delay.print_delay("\nYour fighting style dictates your fighter's strength in the ring.")
        delay.print_delay("\nThere are three fighting styles to choose from:\n")
        time.sleep(0.75)

        delay.print_pause("\n[1] Aggressive - Your fighter will deal more damage with their attacks ")
        delay.print_pause("[2] Defensive - Your fighter will take less damage on successful blocks")
        delay.print_pause("[3] Tanky - Your fighter has a higher health pool\n")

        delay.print_delay("\nPlease enter in the number corresponding to the fighting style you want to adopt: ")
        player_fight_style = int(input())

        global player 
        player = Character(player_firstname, player_lastname, player_alias, player_fight_style)

            
        delay.print_delay(f"\nYour fighter's name is: {player.full_name}")
        delay.print_delay(f"\nYour fighting style is: {player.fight_style_name}")
        delay.print_delay(f"\nYour attack is: {player.attack}")
        delay.print_delay(f"\nYour defence is: {player.defence}")
        delay.print_delay(f"\nYour total HP is: {player.hp}\n")

        delay.print_pause("\nPress Enter to return back to the main menu")
        input()

        os.system('clear')

    except ValueError:
        print("\nThat's an invalid selection. You are required to input a number between 1 and 3 to select your fighting style.")

        input("\nCharacter creation will need to restart. Press enter to continue")

        character_create()


def character_details():
    try:
        os.system('clear')

        delay.print_delay(f"\nYour fighter's name is: {player.full_name}")
        delay.print_delay(f"\nYour fighting style is: {player.fight_style_name}")
        delay.print_delay(f"\nYour attack is: {player.attack}")
        delay.print_delay(f"\nYour defence is: {player.defence}")
        delay.print_delay(f"\nYour total HP is: {player.hp}")
        delay.print_delay(f"\nAvailable Stat points: {player.statpoints}\n")

        input("\nPress Enter to return back to the main menu")
        os.system('clear')

    except NameError:
        print("You have not created a fighter yet! Please create a new fighter from the main menu")
        input("\nPress Enter to return back to the main menu")

        os.system('clear')