from classes import Character
from classes import Opponent
import battle_menu
import opponents
import character_creation
import os
import random


def battle_sim():

   
    os.system('clear')

    player_hp = character_creation.player.hp
    player_full_damage = character_creation.player.attack
    player_block_damage = character_creation.player.attack - opponents.sandy.opp_defence

    # opponent_hp = opponents.sandy.opp_hp
    # opponent_full_damage = opponents.sandy.opp_attack
    # opponent_block_damage = opponents.sandy.opp_attack - character_creation.player.defence

    if character_creation.player.battle_won == 0:
        opponent_first_name = opponents.sandy.opp_first_name
        opponent_full_name = opponents.sandy.opp_full_name
        opponent_hp = opponents.sandy.opp_hp
        opponent_full_damage = opponents.sandy.opp_attack
        opponent_block_damage = opponents.sandy.opp_attack - character_creation.player.defence
    
    elif character_creation.player.battle_won == 1:
        opponent_first_name = opponents.sally.opp_first_name
        opponent_full_name = opponents.sally.opp_full_name
        opponent_hp = opponents.sally.opp_hp
        opponent_full_damage = opponents.sally.opp_attack
        opponent_block_damage = opponents.sally.opp_attack - character_creation.player.defence

    elif character_creation.player.battle_won == 2:
        opponent_first_name = opponents.pimmsy.opp_first_name
        opponent_full_name = opponents.pimmsy.opp_full_name
        opponent_hp = opponents.pimmsy.opp_hp
        opponent_full_damage = opponents.pimmsy.opp_attack
        opponent_block_damage = opponents.pimmsy.opp_attack - character_creation.player.defence
    else:
        print("Congratulations, you have defeated all of the opponents and been crowned World Champion!")

        input("\nPress enter to return to the locker room")

        break

    cpu_att_action = ["Left Hook", "Right Hook", "Uppercut"]
    cpu_def_action = ["Block Left Hook", "Block Right Hook", "Block Uppercut"]

    print(f"Ladies and Gentlemen, please welcome to the arena our our fighter's for the tonight.")
    print(f"\nIn the red corner, we have {character_creation.player.full_name}!")
    print(f"\nIn the blue corner, we have {opponent_full_name}!")
    print("Fighter's to your corners...")
    print("Let's get ready to R-R-RUMBLEEE!!")

    while player_hp > 0 and opponent_hp > 0:

        os.system('clear')

        print(f"\nYour current HP is: {player_hp}")
        print(f"Your opponent's HP is: {opponent_hp}")

        print("\nIt is your turn to attack! Please enter one of the following actions: 'Left Hook', 'Right Hook', 'Uppercut'")

        player_attack = input("\nPlease Enter your action: ")
        cpu_defence = random.choice(cpu_def_action)
        

        if player_attack.lower() == "left hook":

            if cpu_defence.lower() == "block left hook":
                opponent_hp = opponent_hp - player_block_damage

                print("You throw a Left Hook")
                print(f"\n{opponent_first_name} blocked your Left Hook!")
                print(f"\nYou dealt {player_block_damage} damage to your opponent!")
            else:
                opponent_hp = opponent_hp - player_full_damage

                print("You throw a Left Hook")
                print(f"\n{opponent_first_name} couldn't block your attack!")
                print(f"\nYou dealt {player_full_damage} damage to {opponent_first_name}!")

        elif player_attack.lower() == "right hook":

            if cpu_defence.lower() == "block right hook":
                opponent_hp = opponent_hp - player_block_damage

                print("You throw a Right Hook")
                print(f"\n{opponent_first_name} blocked your Right Hook!")
                print(f"You dealt {player_block_damage} damage to your opponent!")
            else:
                opponent_hp = opponent_hp - player_full_damage

                print("You throw a Right Hook")
                print(f"\n{opponent_first_name} couldn't block your attack!")
                print(f"You dealt {player_full_damage} damage to {opponent_first_name}!")

        elif player_attack.lower() == "uppercut":  
                
            if cpu_defence.lower() == "block uppercut":
                opponent_hp = opponent_hp - player_block_damage

                print("You throw an Uppercut")
                print(f"\n{opponent_first_name} blocked your Uppercut!")
                print(f"You dealt {player_block_damage} damage to your opponent!")
            else:
                opponent_hp = opponent_hp - player_full_damage

                print("You throw an Uppercut")
                print(f"\n{opponent_first_name} couldn't block your attack!")
                print(f"You dealt {player_full_damage} damage to {opponent_first_name}!")

        else:
            print("\nThat was an invalid attack! Please input one of the following options: 'Left Hook', 'Right Hook', 'Uppercut'")
            continue

        print(f"\nYour current HP is: {player_hp}")
        print(f"Your opponent's HP is: {opponent_hp}")

        # Defence portion of the battle simulator. Users will input their defence action and CPU action will be randomly generated from their attack list

        print("\nIt is now your turn to defend! Please enter one of the following actions: 'Block Left Hook', 'Block Right Hook', 'Block Uppercut'")

        player_defence = input("\nPlease Enter your action: ")
        cpu_attack = random.choice(cpu_att_action)

        if cpu_attack.lower() == "left hook":

            if player_defence.lower == "block left hook":
                player_hp = player_hp - opponent_block_damage

                print(f"{opponent_first_name} threw a {cpu_attack}")
                print(f"\nYou blocked the left hook!")
                print(f"\nYou took {opponent_block_damage} damage from your opponent!")
            
            else:
                player_hp = player_hp - opponent_full_damage

                print(f"{opponent_first_name} threw a {cpu_attack}")
                print(f"\nYou couldn't block the attack!")
                print(f"\nYou took {opponent_full_damage} damage from your opponent!")

        elif cpu_attack.lower() == "right hook":

            if player_defence.lower == "block right hook":
                player_hp = player_hp - opponent_block_damage

                print(f"{opponent_first_name} threw a {cpu_attack}")
                print(f"\nYou blocked the right hook!")
                print(f"\nYou took {opponent_block_damage} damage from your opponent!")
            
            else:
                player_hp = player_hp - opponent_full_damage

                print(f"{opponent_first_name} threw a {cpu_attack}")
                print(f"\nYou couldn't block the attack!")
                print(f"\nYou took {opponent_full_damage} damage from your opponent!")

        elif cpu_attack.lower() == "uppercut":

            if player_defence.lower == "block uppercut":
                player_hp = player_hp - opponent_block_damage

                print(f"{opponent_first_name} threw a {cpu_attack}")
                print(f"\nYou blocked the uppercut!")
                print(f"\nYou took {opponent_block_damage} damage from your opponent!")
            
            else:
                player_hp = player_hp - opponent_full_damage

                print(f"{opponent_first_name} threw a {cpu_attack}")
                print(f"\nYou couldn't block the attack!")
                print(f"\nYou took {opponent_full_damage} damage from your opponent!")
        
        else:
            print("\nThat was an invalid attack! Please input one of the following options: 'Left Hook', 'Right Hook', 'Uppercut'")
            continue





        

            