from test_3_RPG import game
from test_3_RPG.core.goblin import Monster

class Orc(Monster):
    def __init__(self,name:str,hp:int,type:str,speed:int,power:float,armor_rating:int,weapon:str):
        super().__init__(name,hp,speed,power,armor_rating,weapon)
        self.type = type


    def speak(self):
        print(f'{self.type} {self.name} is angry')

    def attack(self):
        attacking_monster = game.Game.roll_dice(6) + self.power
        weapon =["Knife" ,"Sword", "Axe"]
        the_mult= [0.5,1,1.5]
        index = weapon.index(self.weapon)
        attacking_monster = the_mult[index]
        return attacking_monster