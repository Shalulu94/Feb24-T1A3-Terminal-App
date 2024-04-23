# Character creation
from classes import Character
from classes import Opponent
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
        print(f"\nYour fighting style is: {player.fight_style}")
        print(f"Your attack is: {player.attack}")
        print(f"Your defence is: {player.defence}")
        print(f"Your total HP is: {player.hp}")

        input("\nPress Enter to return back to the main menu")

        os.system('clear')

    except ValueError:
        print("\nThat's an invalid selection. You are required to input a number between 1 and 3 to select your fighting style.")

        input("\nCharacter creation will need to restart. Press enter to continue")

        character_create()

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

def opponent():

    print("Hello")

    global sandy
    sandy = Opponent("Sandy", "Huynh", "Luxury", 80, 40, 500)

    global pimmsy
    pimmsy = Opponent("Pimmsy", "Huynh", "Big Dog", 125, 50, 1500)

    global sally
    sally = Opponent("Sally", "Huynh", "The Baker", 100, 50, 800)

    global jager
    jager = Opponent("Jager", "Huynh", "Sleepy", 100, 80, 800)

    os.system('clear')

    try:
        while player.battle_won < 4:
            if player.battle_won == 0:

                print(f"Your next opponent will be {sandy.opp_full_name}!")
                print(f"\n{sandy.opp_full_name}'s stats are as below:")
                print(f"\nAttack: {sandy.opp_attack}")
                print(f"Defence: {sandy.opp_defence}")
                print(f"Hp: {sandy.opp_hp}")   

            elif player.battle_won == 1:
                print(f"Your next opponent will be {sally.opp_full_name}!")
                print(f"\n{sally.opp_full_name}'s stats are as below:")
                print(f"\nAttack: {sally.opp_attack}")
                print(f"Defence: {sally.opp_defence}")
                print(f"Hp: {sally.opp_hp}")   
            
            else:
                print(f"Your next opponent will be {pimmsy.opp_full_name}!")
                print(f"\n{pimmsy.opp_full_name}'s stats are as below:")
                print(f"\nAttack: {pimmsy.opp_attack}")
                print(f"Defence: {pimmsy.opp_defence}")
                print(f"Hp: {pimmsy.opp_hp}")   
            
            input("\nPress enter to return to Battle menu")

            os.system('clear')

            break

    except: print("Something went wrong")


def battle_menu():
    os.system('clear')

    user_input = 0

    try:

                
        while user_input != 5:

            print(f"Welcome to the locker room {player.first_name}!")
            print("\nHere you will be able to prepare for your upcoming match")
            print("\nWithin the locker room you can:")
            print("\n1. View your upcoming opponent")
            print("2. View your fighter stats")
            print("3. Upgrade figher stats")
            print("4. Go to Battle!")
            print("5. Back to main menu")


            user_input = int(input("Please input a number out of the below options to continue: "))

            if user_input == 1:
                opponent()
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
    


    