import os
import time

from classes import Character
import delay
import style


def character_create():

    try:
        os.system("clear")

        delay.print_delay(f"{style.default}Welcome to the fighter creation menu\n")
        delay.print_delay(
            "\nHere you will be able to create a new fighter to compete with in the boxing championship!\n"
        )
        time.sleep(0.75)

        delay.print_delay(
            f"\nPlease enter your fighter's {style.inp}first name:{style.default} "
        )
        player_firstname = input()

        delay.print_delay(
            f"Please enter your fighter's {style.inp}last name:{style.default} "
        )
        player_lastname = input()

        delay.print_delay(
            f"Please enter your fighter's {style.inp}nickname:{style.default} "
        )
        player_alias = input()

        delay.print_delay(
            "\nYour fighting style dictates your fighter's strength in the ring."
        )
        delay.print_delay("\nThere are three fighting styles to choose from:\n")
        time.sleep(0.75)

        delay.print_pause(
            f"\n{style.inp}[1]{style.defb} Aggressive{style.default} - Your fighter will deal more damage with their attacks "
        )
        delay.print_pause(
            f"{style.inp}[2]{style.defb} Defensive{style.default} - Your fighter will take less damage on successful blocks"
        )
        delay.print_pause(
            f"{style.inp}[3]{style.defb} Tanky{style.default} - Your fighter has a higher health pool\n"
        )

        delay.print_delay(
            "\nPlease enter in the number corresponding to the fighting style you want to adopt: "
        )
        player_fight_style = int(input())

        global player
        player = Character(
            player_firstname, player_lastname, player_alias, player_fight_style
        )

        delay.print_delay(f"\nYour fighter's name is: {style.bold}{player.full_name}")
        delay.print_delay(
            f"\n{style.default}Your fighting style is: {style.bold}{player.fight_style_name}"
        )
        delay.print_delay(
            f"\n{style.default}Your attack is: {style.bold}{player.attack}"
        )
        delay.print_delay(
            f"\n{style.default}Your defence is: {style.bold}{player.defence}"
        )
        delay.print_delay(
            f"\n{style.default}Your total HP is: {style.bold}{player.hp}\n"
        )

        delay.print_pause(
            f"\n{style.default}Press Enter to return back to the main menu"
        )
        input()

        os.system("clear")

    except ValueError:
        print(
            f"\n{style.err}That's an invalid selection. You are required to input a number between 1 and 3 to select your fighting style."
        )

        input("\nCharacter creation will need to restart. Press enter to continue")

        character_create()


def character_details():
    try:
        os.system("clear")

        delay.print_delay(f"\nYour fighter's name is: {style.bold}{player.full_name}")
        delay.print_delay(
            f"\n{style.default}Your fighting style is: {style.bold}{player.fight_style_name}"
        )
        delay.print_delay(
            f"\n{style.default}Your attack is: {style.bold}{player.attack}"
        )
        delay.print_delay(
            f"\n{style.default}Your defence is: {style.bold}{player.defence}"
        )
        delay.print_delay(
            f"\n{style.default}Your total HP is: {style.bold}{player.hp}\n"
        )
        delay.print_delay(
            f"\n{style.default}Available Stat points: {style.bold}{player.statpoints}\n"
        )

        input(f"\n{style.default}Press Enter to return back to the main menu")
        os.system("clear")

    except NameError:
        print(
            f"{style.err}You have not created a fighter yet! Please create a new fighter from the main menu"
        )
        input("\nPress Enter to return back to the main menu")

        os.system("clear")
