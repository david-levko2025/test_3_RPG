from test_3_RPG import game

class Player:
    def __init__(self,name:str,hp:int,speed:int,power:int,armor_rating:int,profession:str):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.profession = profession

        if self.profession == "healer":
            self.hp += 10
        if self.profession == "warrior":
            self.power += 2


    def speak(self):
        print(f'its {self.name} we going to win')

    def attack(self):
        attacking_monster = game.Game.roll_dice(6) + self.power

