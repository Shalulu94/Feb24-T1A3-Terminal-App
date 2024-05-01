from classes import Opponent
import character_creation
import os


sandy = Opponent("Sandy", "Huynh", "Chanel", 80, 40, 500)
pimmsy = Opponent("Pimmsy", "Huynh", "Big Dog", 125, 50, 1500)
sally = Opponent("Sally", "Huynh", "The Baker", 100, 50, 800)
jager = Opponent("Jager", "Huynh", "Sleepy", 100, 80, 800)


def opponent():

    print("Hello")

    os.system('clear')

    
    while character_creation.player.battle_won < 4:
        if character_creation.player.battle_won == 0:

            print(f"Your next opponent will be {sandy.opp_full_name}!")
            print(f"\n{sandy.opp_full_name}'s stats are as below:")
            print(f"\nAttack: {sandy.opp_attack}")
            print(f"Defence: {sandy.opp_defence}")
            print(f"Hp: {sandy.opp_hp}")   

        elif character_creation.player.battle_won == 1:
            print(f"Your next opponent will be {sally.opp_full_name}!")
            print(f"\n{sally.opp_full_name}'s stats are as below:")
            print(f"\nAttack: {sally.opp_attack}")
            print(f"Defence: {sally.opp_defence}")
            print(f"Hp: {sally.opp_hp}")   
        
        elif character_creation.player.battle_won == 2:
            print(f"Your next opponent will be {pimmsy.opp_full_name}!")
            print(f"\n{pimmsy.opp_full_name}'s stats are as below:")
            print(f"\nAttack: {pimmsy.opp_attack}")
            print(f"Defence: {pimmsy.opp_defence}")
            print(f"Hp: {pimmsy.opp_hp}")  
        
        else:
            print("You've defeated all the opponents and have been crowned World Champion!")
            print("Game over!")
        
        input("\nPress enter to return to Battle menu")

        os.system('clear')

        break

