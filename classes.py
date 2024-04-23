class Character():
    def __init__(self, first_name, last_name, alias, fight_style):
        self.first_name = first_name
        self.last_name = last_name
        self.alias = alias
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
                print("That fight style is not valid.")
                print("There are three fighting styles to choose from:")
                print("\n1. Aggressive - Your fighter will deal more damage with their attacks ")
                print("2. Defensive - Your fighter will take less damage on successful blocks")
                print("3. Tanky - Your fighter has a higher health pool\n")

                fight_style = int(input("Please enter in the number corresponding to the fighting style you want to adopt: "))

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


