class Character():
    def __init__(self, name, alias, fight_style):
        self.name = name
        self.alias = alias
        self.fight_style = fight_style
        self.attack = 100
        self.defence = 50
        self.hp = 600
        self.statpoints = 0
        
    




player = Character("Shahrul", "Money", "Aggressive")

print(f"Fighter name is: {player.name}")
print(player.alias)
print(player.fight_style)
print(player.attack)
print(player.defence)
print(player.hp)
print(player.statpoints)


