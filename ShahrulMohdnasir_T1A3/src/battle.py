import os
import random

from classes import Character
from classes import Opponent
import battle_menu
import opponents
import character_creation
import time
import delay
import style


def battle_sim():

    os.system("clear")

    # Identifies which CPU opponent player will fight
    # Dependent on how many wins they have secured

    if character_creation.player.battle_won == 0:
        opponent_first_name = opponents.jager.opp_first_name
        opponent_full_name = opponents.jager.opp_full_name
        opponent_hp = opponents.jager.opp_hp
        opponent_full_damage = opponents.jager.opp_attack
        opponent_block_damage = (
            opponents.jager.opp_attack - character_creation.player.defence
        )

    elif character_creation.player.battle_won == 1:
        opponent_first_name = opponents.johnny.opp_first_name
        opponent_full_name = opponents.johnny.opp_full_name
        opponent_hp = opponents.johnny.opp_hp
        opponent_full_damage = opponents.johnny.opp_attack
        opponent_block_damage = (
            opponents.johnny.opp_attack - character_creation.player.defence
        )

    elif character_creation.player.battle_won == 2:
        opponent_first_name = opponents.pimmsy.opp_first_name
        opponent_full_name = opponents.pimmsy.opp_full_name
        opponent_hp = opponents.pimmsy.opp_hp
        opponent_full_damage = opponents.pimmsy.opp_attack
        opponent_block_damage = (
            opponents.pimmsy.opp_attack - character_creation.player.defence
        )

    else:
        print(
            f"{style.default}Congratulations, you have defeated all of the opponents and been crowned {style.defbu}World Champion!{style.default}"
        )

        input("\nPress enter to return to the locker room")

        battle_menu.battle_screen()

    player_hp = character_creation.player.hp
    player_full_damage = character_creation.player.attack
    player_block_damage = character_creation.player.attack - opponent_block_damage

    cpu_att_action = ["left hook", "right hook", "uppercut"]
    cpu_def_action = ["Block Left Hook", "Block Right Hook", "Block Uppercut"]

    delay.print_delay(
        f"{style.default}Ladies and Gentlemen, please welcome to the arena our fighter's for the tonight.\n"
    )
    time.sleep(1)
    delay.print_delay(
        f"\nIn the red corner, we have {style.bold}{character_creation.player.full_name}!\n"
    )
    time.sleep(1)
    delay.print_delay(
        f"\n{style.default}In the blue corner, we have {style.bold}{opponent_full_name}!\n"
    )
    time.sleep(1)
    delay.print_delay(f"\n{style.default}Fighter's to your corners...")
    time.sleep(0.75)
    delay.print_delay("\nLet's get ready to R-R-RUMBLEEE!!\n")

    delay.print_pause("\nPress Enter to begin the match")
    input()

    while player_hp > 0 and opponent_hp > 0:

        os.system("clear")

        print(f"\n{style.default}Your current HP is: {style.hp}{player_hp}")
        print(f"{style.default}Your opponent's HP is: {style.hp}{opponent_hp}\n")

        delay.print_delay(
            f"{style.default}It is your turn to attack! Please enter one of the following actions: {style.inp}[Left Hook], [Right Hook], [Uppercut]{style.default}\n"
        )

        delay.print_delay("\nPlease Enter your action: \n")
        player_attack = input()
        cpu_defence = random.choice(cpu_def_action)

        if player_attack.lower() == "left hook":

            if cpu_defence.lower() == "block left hook":
                opponent_hp = opponent_hp - player_block_damage

                delay.print_delay("\nYou throw a Left Hook\n")
                time.sleep(0.75)
                delay.print_delay(f"\n{opponent_first_name} blocked your Left Hook!\n")
                time.sleep(0.75)
                delay.print_delay(
                    f"\nYou dealt {style.hit}{player_block_damage}{style.default} damage to your opponent!\n"
                )
            else:
                opponent_hp = opponent_hp - player_full_damage

                delay.print_delay("You throw a Left Hook\n")
                time.sleep(0.75)
                delay.print_delay(
                    f"\n{opponent_first_name} couldn't block your attack!\n"
                )
                time.sleep(0.75)
                delay.print_delay(
                    f"\nYou dealt {style.hit}{player_full_damage}{style.default} damage to {opponent_first_name}!\n"
                )

        elif player_attack.lower() == "right hook":

            if cpu_defence.lower() == "block right hook":
                opponent_hp = opponent_hp - player_block_damage

                delay.print_delay("\nYou throw a Right Hook\n")
                time.sleep(0.75)
                delay.print_delay(f"\n{opponent_first_name} blocked your Right Hook!\n")
                time.sleep(0.75)
                delay.print_delay(
                    f"You dealt {style.hit}{player_block_damage}{style.default} damage to your opponent!\n"
                )
            else:
                opponent_hp = opponent_hp - player_full_damage

                delay.print_delay("You throw a Right Hook\n")
                time.sleep(0.75)
                delay.print_delay(
                    f"\n{opponent_first_name} couldn't block your attack!\n"
                )
                time.sleep(0.75)
                delay.print_delay(
                    f"You dealt {style.hit}{player_full_damage}{style.default} damage to {opponent_first_name}!\n"
                )

        elif player_attack.lower() == "uppercut":

            if cpu_defence.lower() == "block uppercut":
                opponent_hp = opponent_hp - player_block_damage

                delay.print_delay("\nYou throw an Uppercut\n")
                time.sleep(0.75)
                delay.print_delay(f"\n{opponent_first_name} blocked your Uppercut!\n")
                time.sleep(0.75)
                delay.print_delay(
                    f"You dealt {style.hit}{player_block_damage}{style.default} damage to your opponent!\n"
                )
            else:
                opponent_hp = opponent_hp - player_full_damage

                delay.print_delay("You throw an Uppercut\n")
                time.sleep(0.75)
                delay.print_delay(
                    f"\n{opponent_first_name} couldn't block your attack!\n"
                )
                time.sleep(0.75)
                delay.print_delay(
                    f"You dealt {style.hit}{player_full_damage}{style.default} damage to {opponent_first_name}!\n"
                )

        else:
            print(
                f"{style.err}\nThat was an invalid attack! Please input one of the following options: [Left Hook], [Right Hook], [Uppercut]"
            )

            input("\nPress Enter to try again")
            continue

        delay.print_delay(f"\nYour current HP is: {style.hp}{player_hp}{style.default}")
        delay.print_delay(
            f"\nYour opponent's HP is: {style.hp}{opponent_hp}{style.default}\n"
        )

        if opponent_hp <= 0:
            delay.print_delay(
                f"You've successfully knocked out {opponent_first_name}!\n"
            )
            time.sleep(0.75)
            delay.print_delay(
                f"\nThe winner of the match is {character_creation.player.full_name}!!\n"
            )

            delay.print_delay(
                "\nYou've been awarded 3 stat points to upgrade your fighter"
            )
            delay.print_delay(
                "\nYou can spend these stat points by visiting the upgrade menu from the locker room\n"
            )

            character_creation.player.statpoints += 3
            character_creation.player.battle_won += 1

            delay.print_delay("\nPress Enter to return to the locker room")
            input()

            break

        else:
            delay.print_delay(f"\n{style.default}Your turn to attack is over")
            delay.print_delay("\nPress Enter to move to defence round")
            input()

        # Defence portion of the battle simulator. Users will input their defence action and CPU action will be randomly generated from their attack list

        player_defence_low = ""

        while player_defence_low == "":

            os.system("clear")

            delay.print_delay(f"\n{style.default}It is now your turn to defend!\n")
            time.sleep(0.75)
            delay.print_delay(
                f"\nPlease enter one of the following actions: {style.inp}[Block Left Hook], [Block Right Hook], [Block Uppercut]{style.default}\n"
            )

            delay.print_delay("\nEnter your action: ")

            player_defence = input()
            player_defence_low = player_defence.lower()
            cpu_attack = random.choice(cpu_att_action)

            if cpu_attack.lower() == "left hook":

                if player_defence_low == "block left hook":
                    player_hp = player_hp - opponent_block_damage

                    delay.print_delay(f"\n{opponent_first_name} threw a left hook\n")
                    time.sleep(0.75)
                    delay.print_delay(f"\nYou blocked the left hook!\n")
                    time.sleep(0.75)
                    delay.print_delay(
                        f"\nYou took {style.hit}{opponent_block_damage}{style.default} damage from your opponent!\n"
                    )

                elif player_defence_low == "block right hook":
                    player_hp = player_hp - opponent_full_damage

                    delay.print_delay(f"\n{opponent_first_name} threw a left hook\n")
                    time.sleep(0.75)
                    delay.print_delay(f"\nYou couldn't block the attack!")
                    time.sleep(0.75)
                    delay.print_delay(
                        f"\nYou took {style.hit}{opponent_full_damage}{style.default} damage from your opponent!\n"
                    )

                elif player_defence_low == "block uppercut":
                    player_hp = player_hp - opponent_full_damage

                    delay.print_delay(f"\n{opponent_first_name} threw a left hook\n")
                    time.sleep(0.75)
                    delay.print_delay(f"\nYou couldn't block the attack!\n")
                    time.sleep(0.75)
                    delay.print_delay(
                        f"\nYou took {style.hit}{opponent_full_damage}{style.default} damage from your opponent!\n"
                    )

                else:
                    print(
                        "\nThat was an invalid defence option! Please input one of the following options: 'Block Left Hook', 'Block Right Hook', 'Block Uppercut'"
                    )

                    input("\nPress Enter to try again")

                    player_defence_low = ""

                    continue

            elif cpu_attack.lower() == "right hook":

                if player_defence_low == "block right hook":
                    player_hp = player_hp - opponent_block_damage

                    delay.print_delay(f"\n{opponent_first_name} threw a right hook\n")
                    time.sleep(0.75)
                    delay.print_delay(f"\nYou blocked the right hook!\n")
                    time.sleep(0.75)
                    delay.print_delay(
                        f"\nYou took {style.hit}{opponent_block_damage}{style.default} damage from your opponent!\n"
                    )

                elif player_defence_low == "block left hook":
                    player_hp = player_hp - opponent_full_damage

                    delay.print_delay(f"\n{opponent_first_name} threw a right hook\n")
                    time.sleep(0.75)
                    delay.print_delay(f"\nYou couldn't block the attack!\n")
                    time.sleep(0.75)
                    delay.print_delay(
                        f"\nYou took {style.hit}{opponent_full_damage}{style.default} damage from your opponent!\n"
                    )

                elif player_defence_low == "block uppercut":
                    player_hp = player_hp - opponent_full_damage

                    delay.print_delay(f"\n{opponent_first_name} threw a right hook\n")
                    time.sleep(0.75)
                    delay.print_delay(f"\nYou couldn't block the attack!\n")
                    time.sleep(0.75)
                    delay.print_delay(
                        f"\nYou took {style.hit}{opponent_full_damage}{style.default} damage from your opponent!\n"
                    )

                else:
                    print(
                        "\nThat was an invalid defence option! Please input one of the following options: 'Block Left Hook', 'Block Right Hook', 'Block Uppercut'"
                    )

                    input("\nPress Enter to try again")

                    player_defence_low = ""

                    continue

            elif cpu_attack.lower() == "uppercut":

                if player_defence_low == "block uppercut":
                    player_hp = player_hp - opponent_block_damage

                    delay.print_delay(f"\n{opponent_first_name} threw an uppercut\n")
                    time.sleep(0.75)
                    delay.print_delay(f"\nYou blocked the uppercut!\n")
                    time.sleep(0.75)
                    delay.print_delay(
                        f"\nYou took {style.hit}{opponent_block_damage}{style.default} damage from your opponent!\n"
                    )

                elif player_defence_low == "block right hook":
                    player_hp = player_hp - opponent_full_damage

                    delay.print_delay(f"\n{opponent_first_name} threw an uppercut\n")
                    time.sleep(0.75)
                    delay.print_delay(f"\nYou couldn't block the attack!\n")
                    time.sleep(0.75)
                    delay.print_delay(
                        f"\nYou took {style.hit}{opponent_full_damage}{style.default} damage from your opponent!\n"
                    )

                elif player_defence_low == "block left hook":
                    player_hp = player_hp - opponent_full_damage

                    delay.print_delay(f"\n{opponent_first_name} threw an uppercut\n")
                    time.sleep(0.75)
                    delay.print_delay(f"\nYou couldn't block the attack!\n")
                    time.sleep(0.75)
                    delay.print_delay(
                        f"\nYou took {style.hit}{opponent_full_damage}{style.default} damage from your opponent!\n"
                    )

                else:
                    print(
                        "\nThat was an invalid defence! Please input one of the following options: 'Block Left Hook', 'Block Right Hook', 'Block Uppercut'"
                    )

                    input("\nPress Enter to try again")

                    player_defence_low = ""

                    continue

            else:
                print(
                    "\nThat was an invalid attack option! Please input one of the following options: 'Left Hook', 'Right Hook', 'Uppercut'"
                )
                continue

        delay.print_delay(f"\nYour current HP is: {style.hp}{player_hp}{style.default}")
        delay.print_delay(
            f"\nYour opponent's HP is: {style.hp}{opponent_hp}{style.default}\n"
        )

        if player_hp <= 0:
            delay.print_delay(
                f"Oh no!! You've been knocked out by {opponent_first_name}!\n"
            )
            time.sleep(0.75)
            delay.print_delay(f"\nThe winner of the match is {opponent_full_name}!!\n")

            delay.print_delay("\nPress Enter to return to the locker room")
            input()

            break

        else:
            input("Press Enter to move onto your next turn to attack")
