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
    print("\n1. Aggressive - Your fighter will deal more damage with their attacks ")
    print("2. Defensive - Your fighter will take less damage on successful blocks")
    print("3. Tanky - Your fighter has a higher health pool\n")

    player_fight_style = int(input("Please enter in the number corresponding to the fighting style you want to adopt: "))

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

def battle_menu():
    os.system('clear')
    try:

        print(f"Welcome to the locker room! {player.first_name}")
        print("Here you will be able to prepare for your upcoming match")
        print("Within the locker room you can:")
        print("1. View your upcoming opponent")
        print("2. View your fighter stats")
        print("3. Upgrade figher stats")
        print("4. Go to Battle!")
        print("5. Back to main menu")
        
        while user_input != 4:

            user_input = int(input("Please input a number out of the below options to continue: "))

            if user_input == 1:
                print("view upcoming opponent screen")
            elif user_input == 2:
                character_details()
            elif user_input == 3:
                print("View character upgrade screen")
            elif user_input == 4:
                print("Take to skill upgrade screen")
            elif user_input == 5: 
                break
            else:
                print("That is an invalid selection. Please enter a number between 1 and 3")
    
    
    
    except NameError:
        print("You haven't created a fighter yet!")
        print("Please return to the main menu to create a new fighter")

        input("\nPress Enter to return back to the battle menu")

        os.system('clear')

    

    



    








