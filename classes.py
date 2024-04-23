class Character():
    def __init__(self, first_name, last_name, alias, fight_style):
        self.first_name = first_name
        self.last_name = last_name
        self.alias = alias
        self.fight_style = fight_style
        if fight_style == "aggressive" or fight_style == "Aggressive": 
            attack = 125
        else:
            attack = 100

        if fight_style == "defensive" or fight_style == "Defensive":
            defence = 75
        else:
            defence = 50
        
        if fight_style == "tanky" or fight_style == "Tanky":
            hp = 750
        else:
            hp = 600
        self.attack = attack
        self.defence = defence
        self.hp = hp
        self.statpoints = 3
        
    



# print(f"\nFighter name is: {player.name}")
# print(player.alias)
# print(player.fight_style)
# print(player.attack)
# print(player.defence)
# print(player.hp)
# print(player.statpoints)


