# Character creation
from classes import Character
import os

def character_create():
    os.system('clear')
    print("Welcome to the fighter creation menu\n")
    print("Here you will be able to create a new fighter to compete with in the boxing championship!\n")


    player_firstname = input("Please enter your fighter's first name: ")
    player_lastname = input("Please enter your fighter's last name: ")
    player_alias = input("Please enter your fighter's nickname: ")

    print("\nYour fighting style dictates your fighter's strength in the ring.")
    print("There are three fighting styles to choose from:")
    print("\nAggressive - Your fighter will deal more damage with their attacks ")
    print("Defensive - Your fighter will take less damage on successful blocks")
    print("Tanky - Your fighter has a higher health pool\n")

    player_fight_style = input("Please choose your fighting style from the above options: ")

    global player 
    player = Character(player_firstname, player_lastname, player_alias, player_fight_style)

        
    print(f"\nYour fighter's name is: {player.first_name} \"{player.alias}\" {player.last_name}")
    print(f"\nYour fighting style is: {player.fight_style}")
    print(f"Your attack is: {player.attack}")
    print(f"Your defence is: {player.defence}")
    print(f"Your total HP is: {player.hp}")

    input("\nPress Enter to return back to the main menu")

    os.system('clear')

# global player = Character(player_firstname, player_lastname, player_alias, player_fight_style)

def character_details():
    try:
        os.system('clear')
        print(f"\nYour fighter's name is: {player.first_name} \"{player.alias}\" {player.last_name}")
        print(f"\nYour fighting style is: {player.fight_style}")
        print(f"Your attack is: {player.attack}")
        print(f"Your defence is: {player.defence}")
        print(f"Your total HP is: {player.hp}\n")

        input("\nPress Enter to return back to the main menu")
        os.system('clear')
    except NameError:
        print("You have not created a fighter yet! Please create a new fighter from the main menu")
        input("\nPress Enter to return back to the main menu")

        os.system('clear')


    








