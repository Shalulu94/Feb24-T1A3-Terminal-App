from classes import Opponent
import character_creation
import os
import delay
import time


sandy = Opponent("Sandy", "Huynh", "Chanel", 80, 40, 500)
pimmsy = Opponent("Pimmsy", "Huynh", "Big Dog", 125, 50, 1500)
sally = Opponent("Sally", "Huynh", "The Baker", 100, 50, 800)
jager = Opponent("Jager", "Huynh", "Sleepy", 100, 80, 800)


def opponent():


    os.system('clear')

    
    while character_creation.player.battle_won < 4:
        if character_creation.player.battle_won == 0:

            delay.print_delay(f"Your next opponent will be {sandy.opp_full_name}!\n")
            time.sleep(0.75)

            delay.print_delay(f"\n{sandy.opp_full_name}'s stats are as below:")
            delay.print_pause(f"\nAttack: {sandy.opp_attack}")
            delay.print_pause(f"Defence: {sandy.opp_defence}")
            delay.print_pause(f"Hp: {sandy.opp_hp}")   

        elif character_creation.player.battle_won == 1:

            delay.print_delay(f"Your next opponent will be {sally.opp_full_name}!\n")
            time.sleep(0.75)

            delay.print_delay(f"\n{sally.opp_full_name}'s stats are as below:")
            delay.print_pause(f"\nAttack: {sally.opp_attack}")
            delay.print_pause(f"Defence: {sally.opp_defence}")
            delay.print_pause(f"Hp: {sally.opp_hp}")   
        
        elif character_creation.player.battle_won == 2:

            delay.print_delay(f"Your next opponent will be {pimmsy.opp_full_name}!\n")
            time.sleep(0.75)

            delay.print_delay(f"\n{pimmsy.opp_full_name}'s stats are as below:")
            delay.print_pause(f"\nAttack: {pimmsy.opp_attack}")
            delay.print_pause(f"Defence: {pimmsy.opp_defence}")
            delay.print_pause(f"Hp: {pimmsy.opp_hp}")  
        
        else:
            delay.print_delay("You've defeated all the opponents and have been crowned World Champion!\n")
            delay.print_delay("\nGame over!")
        
        input("\nPress enter to return to Battle menu")

        os.system('clear')

        break

