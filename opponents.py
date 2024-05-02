from classes import Opponent
import character_creation
import os
import delay
import time
import style


bailey = Opponent("Bailey", "Huynh", "Chanel", 80, 40, 500)
pimmsy = Opponent("Pimmsy", "White", "Big Dog", 150, 100, 1500)
johnny = Opponent("Johnny", "Yap", "The Bulldog", 125, 50, 800)
jager = Opponent("Jager", "Brown", "Sleepyhead", 100, 40, 500)


def opponent():

    os.system("clear")

    while character_creation.player.battle_won < 4:
        if character_creation.player.battle_won == 0:

            delay.print_delay(
                f"{style.default}Your next opponent will be {jager.opp_full_name}!\n"
            )
            time.sleep(0.75)

            delay.print_delay(f"\n{jager.opp_full_name}'s stats are as below:")
            time.sleep(0.5)
            delay.print_pause(f"\nAttack: {jager.opp_attack}")
            delay.print_pause(f"Defence: {jager.opp_defence}")
            delay.print_pause(f"Hp: {jager.opp_hp}")

        elif character_creation.player.battle_won == 1:

            delay.print_delay(
                f"{style.default}Your next opponent will be {johnny.opp_full_name}!\n"
            )
            time.sleep(0.75)

            delay.print_delay(f"\n{johnny.opp_full_name}'s stats are as below:")
            delay.print_pause(f"\nAttack: {johnny.opp_attack}")
            delay.print_pause(f"Defence: {johnny.opp_defence}")
            delay.print_pause(f"Hp: {johnny.opp_hp}")

        elif character_creation.player.battle_won == 2:

            delay.print_delay(
                f"{style.default}Your next opponent will be {pimmsy.opp_full_name}!\n"
            )
            time.sleep(0.75)

            delay.print_delay(f"\n{pimmsy.opp_full_name}'s stats are as below:")
            delay.print_pause(f"\nAttack: {pimmsy.opp_attack}")
            delay.print_pause(f"Defence: {pimmsy.opp_defence}")
            delay.print_pause(f"Hp: {pimmsy.opp_hp}")

        else:
            delay.print_delay(
                f"{style.default}You've defeated all the opponents and have been crowned {style.defbu}World Champion!{style.default}\n"
            )
            delay.print_delay("\nGame over!")

        input("\nPress enter to return to Battle menu")

        os.system("clear")

        break
