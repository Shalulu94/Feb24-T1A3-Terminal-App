from classes import Character
from classes import Opponent
import battle_menu
import opponents
import character_creation
import os
import random


def battle_sim():

    if character_creation.player.battle_won == 0:
        os.system('clear')

        player_hp = character_creation.player.hp
        player_full_damage = character_creation.player.attack
        player_block_damage = character_creation.player.attack - opponents.sandy.opp_defence

        opponent_hp = opponents.sandy.opp_hp
        opponent_full_damage = opponents.sandy.opp_attack
        opponent_block_damage = opponents.sandy.opp_attack - character_creation.player.defence

        cpu_att_action = ["Left Hook", "Right Hook", "Uppercut"]
        cpu_def_action = ["Block Left Hook", "Block Right Hook", "Block Uppercut"]

        while player_hp > 0 and opponent_hp > 0:

            print(f"\nYour current HP is: {player_hp}")
            print(f"Your opponent's HP is: {opponent_hp}")

            print("\nIt is your turn to attack! Please enter one of the following actions: 'Left Hook', 'Right Hook', 'Uppercut'")

            player_attack = input("\nPlease Enter your action: ")
            cpu_defence = random.choice(cpu_def_action)
           

            if player_attack.lower() == "left hook":

                if cpu_defence.lower() == "block left hook":
                    opponent_hp = opponent_hp - player_block_damage

                    print("You throw a Left Hook")
                    print(f"\n{opponents.sandy.opp_first_name} blocked your Left Hook!")
                    print(f"\nYou dealt {player_block_damage} damage to your opponent!")
                else:
                    opponent_hp = opponent_hp - player_full_damage

                    print("You throw a Left Hook")
                    print(f"\n{opponents.sandy.opp_first_name} couldn't block your attack!")
                    print(f"\nYou dealt {player_full_damage} damage to {opponents.sandy.opp_first_name}!")

            elif player_attack.lower() == "right hook":

                if cpu_defence.lower() == "block right hook":
                    opponent_hp = opponent_hp - player_block_damage

                    print("You throw a Right Hook")
                    print(f"\n{opponents.sandy.opp_first_name} blocked your Right Hook!")
                    print(f"You dealt {player_block_damage} damage to your opponent!")
                else:
                    opponent_hp = opponent_hp - player_full_damage

                    print("You throw a Right Hook")
                    print(f"\n{opponents.sandy.opp_first_name} couldn't block your attack!")
                    print(f"You dealt {player_full_damage} damage to {opponents.sandy.opp_first_name}!")

            elif player_attack.lower() == "uppercut":  
                    
                if cpu_defence.lower() == "block uppercut":
                    opponent_hp = opponent_hp - player_block_damage

                    print("You throw an Uppercut")
                    print(f"\n{opponents.sandy.opp_first_name} blocked your Uppercut!")
                    print(f"You dealt {player_block_damage} damage to your opponent!")
                else:
                    opponent_hp = opponent_hp - player_full_damage

                    print("You throw an Uppercut")
                    print(f"\n{opponents.sandy.opp_first_name} couldn't block your attack!")
                    print(f"You dealt {player_full_damage} damage to {opponents.sandy.opp_first_name}!")

            else:
                print("\nThat was an invalid attack! Please input one of the following options: 'Left Hook', 'Right Hook', 'Uppercut'")
                continue

            print(f"\nYour current HP is: {player_hp}")
            print(f"Your opponent's HP is: {opponent_hp}")

            print("\nIt is now your turn to defend! Please enter one of the following actions: 'Block Left Hook', 'Block Right Hook', 'Block Uppercut'")

            player_defence = input("\nPlease Enter your action: ")
            cpu_attack = random.choice(cpu_att_action)

            if cpu_attack.lower() == "left hook":

                if player_defence.lower == "block left hook":
                    player_hp = player_hp - opponent_block_damage

        

            
