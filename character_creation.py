from classes import Character
import os


def character_create():
    
    try:
        os.system('clear')
        print("Welcome to the fighter creation menu\n")
        print("Here you will be able to create a new fighter to compete with in the boxing championship!\n")


        player_firstname = input("Please enter your fighter's first name: ")
        player_lastname = input("Please enter your fighter's last name: ")
        player_alias = input("Please enter your fighter's nickname: ")

        print("\nYour fighting style dictates your fighter's strength in the ring.")
        print("There are three fighting styles to choose from:")
        print("\n1. Aggressive - Your fighter will deal more damage with their attacks ")
        print("2. Defensive - Your fighter will take less damage on successful blocks")
        print("3. Tanky - Your fighter has a higher health pool\n")

        player_fight_style = int(input("Please enter in the number corresponding to the fighting style you want to adopt: "))

        global player 
        player = Character(player_firstname, player_lastname, player_alias, player_fight_style)

            
        print(f"\nYour fighter's name is: {player.full_name}")
        print(f"\nYour fighting style is: {player.fight_style_name}")
        print(f"Your attack is: {player.attack}")
        print(f"Your defence is: {player.defence}")
        print(f"Your total HP is: {player.hp}")

        input("\nPress Enter to return back to the main menu")

        os.system('clear')

    except ValueError:
        print("\nThat's an invalid selection. You are required to input a number between 1 and 3 to select your fighting style.")

        input("\nCharacter creation will need to restart. Press enter to continue")

        character_create()


def character_details():
    try:
        os.system('clear')
        print(f"\nYour fighter's name is: {player.full_name}")
        print(f"\nYour fighting style is: {player.fight_style_name}")
        print(f"Your attack is: {player.attack}")
        print(f"Your defence is: {player.defence}")
        print(f"Your total HP is: {player.hp}")
        print(f"Available Stat points: {player.statpoints}\n")

        input("\nPress Enter to return back to the main menu")
        os.system('clear')

    except NameError:
        print("You have not created a fighter yet! Please create a new fighter from the main menu")
        input("\nPress Enter to return back to the main menu")

        os.system('clear')