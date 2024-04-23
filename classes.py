import os

class Character():
    def __init__(self, first_name, last_name, alias, fight_style):
        self.first_name = first_name
        self.last_name = last_name
        self.alias = alias
        self.full_name = f"{first_name} \"{self.alias}\" {self.last_name}"
        self.fight_style = fight_style
       
        while fight_style != range(1,4):
            if fight_style == 1: 
                attack = 125
                defence = 50
                hp = 600
                break
            elif fight_style == 2:
                attack = 100
                defence = 75
                hp = 600
                break
            elif fight_style == 3:
                attack = 100
                defence = 50
                hp = 750
                break
            else: 
                os.system('clear')
                print("That fight style is not valid.")
                print("There are three fighting styles to choose from:")
                print("\n1. Aggressive - Your fighter will deal more damage with their attacks ")
                print("2. Defensive - Your fighter will take less damage on successful blocks")
                print("3. Tanky - Your fighter has a higher health pool\n")

                fight_style = int(input("Please enter in the number corresponding to the fighting style you want to adopt: "))

        self.attack = attack
        self.defence = defence
        self.hp = hp
        self.statpoints = 0
        self.battle_won = 0
        
        
    
class Opponent():
    def __init__(self, first_name, last_name, alias, attack, defence, hp):
        self.opp_first_name = first_name
        self.opp_last_name = last_name
        self.opp_alias = alias
        self.opp_attack = int(attack)
        self.opp_defence = int(defence)
        self.opp_hp = int(hp)
        self.opp_full_name = f"{first_name} \"{alias}\" {last_name}"