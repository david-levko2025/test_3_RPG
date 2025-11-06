import random
from random import randint
from test_3_RPG.core.orc import Orc
from test_3_RPG.core.goblin import Goblin
from test_3_RPG.core.player import Player


class Game:
    #static?
    def start(self):
        print("welcome to the maze and monster game!")

    def show_menu(self):
        print(f'---menu---'
              f'battle(b) or exit(e)')

    def create_player(self):
        player = Player("david",50,randint(5,10),randint(5,10), randint(5,15),random.choice(["warrior","healer"]))


    def choose_random_monster(self):
        random.choice([Orc,Goblin])
        orc =Orc("Bon",50,"orc",randint(0,5),randint(10,15),randint(2,8),random.choice(["Knife" ,"Sword", "Axe"]))
        goblin =Goblin("Bibi",20,"goblin",randint(5,10),randint(5,10),1,random.choice(["Knife" ,"Sword", "Axe"]))

    def battle(self,player,monster):
        dice_p = Game.roll_dice(6) + player.speed
        dice_m = Game.roll_dice(6) + monster.spped
        if dice_p >= dice_m:
            attacking = player
            attacked = monster
        else:
            attacking = monster
            attacked = player


            while attacking.hp > 0 and attacked.hp > 0:
                im_alive = True
                sum_attack = Game.roll_dice(20) + attacking.spped
                if sum_attack > attacked.armor_rating:
                    attacked.speak()
                    if attacked.hp <= 0:
                        im_alive = False
                        print(f'{attacking} win')
                    else:
                        attacking, attacked = attacked, attacking

    def roll_dice(self,sides):
        throw1 = randint(1,6)
        throw2 = randint(1,20)

