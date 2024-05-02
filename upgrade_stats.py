from classes import Character
from classes import Opponent
import character_creation
import os
import time
import delay
import style


def upgrades():
   
    try:
        while character_creation.player.statpoints > 0:
            os.system('clear')

            delay.print_delay(f"{style.default}Welcome to the upgrade menu\n")
            delay.print_delay("\nHere you will be able to spend available stat points to upgrade your fighter's stats\n")
            delay.print_delay(f"You currently have {style.bold}{character_creation.player.statpoints}{style.default} available stat points to use\n")
            delay.print_delay("\nPlease select from the following options:")
            delay.print_pause(f"\n{style.inp}[1]{style.default} Allocate stat points")
            delay.print_pause(f"{style.inp}[2]{style.default} View your fighter details")
            delay.print_pause(f"{style.inp}[3]{style.default} Return to previous menu\n")

            delay.print_delay("\nPlease input your selection between 1 and 3:\n")
            user_input = int(input())

            if user_input == 1:
                
                os.system('clear')

                delay.print_delay(f"{style.default}Please choose which stat you would like to upgrade:\n")
                delay.print_pause(f"\n{style.inp}[Attack]{style.default} - Each additional point increases Attack by 25")
                delay.print_pause(f"{style.inp}[Defence]{style.default} - Each additional point increases Defence by 25")
                delay.print_pause(f"{style.inp}[HP]{style.default} - Each additional point increases HP by 150\n")

                delay.print_delay("\nPlease type in which stat you would like to upgrade: ")
                upgrade_input = input()
                upgrade_input_low = upgrade_input.lower()

                if upgrade_input_low == "attack":
                    character_creation.player.attack += 25
                    character_creation.player.statpoints -= 1
                    delay.print_delay("\nAttack successfully upgraded!\n")
                    delay.print_pause("\nPress Enter to return")
                    input()

                elif upgrade_input_low == "defence":
                    character_creation.player.defence += 25
                    character_creation.player.statpoints -= 1
                    delay.print_delay("\nDefence successfully upgraded!\n")
                    delay.print_pause("\nPress Enter to return")
                    input()

                elif upgrade_input_low == "hp":
                    character_creation.player.hp += 25
                    character_creation.player.statpoints -= 1
                    delay.print_delay("\nHP successfully upgraded!\n")
                    delay.print_pause("\nPress Enter to return")
                    input()

                else:
                    print(f"{style.err}That is an invalid selection. Please type in your selection from the above fighter stats")

                    user_input = 1

                    input(f"Press Enter to try again{style.default}")
                    
            elif user_input == 2:
                character_creation.character_details()

            elif user_input == 3:
                break

            else:
                print(f"{style.err}That's an invalid selection.")

                input(f"Press Enter to try again{style.default}")

        if character_creation.player.statpoints == 0:
            os.system('clear')
        
            delay.print_delay("Welcome to the upgrade menu\n")
            delay.print_delay("\nHere you will be able to spend available stat points to upgrade your fighter's stats\n")
            delay.print_delay("\nYou currently do not have any statpoints available to spend\n")

            delay.print_delay("\nPress Enter to return to previous menu")
            input()
            
    except ValueError:
        print(f"{style.err}\nThat was an invalid selection")
        print("Please enter a number between 1 and 3")

        input(f"\nPress Enter to try again{style.default}")

        upgrades()


                             


    