from test_3_RPG import game


start_game = game.Game.start
is_choice = game.Game.show_menu
rolling_dices = game.Game.roll_dice
battle_begin = game.Game.battle


if __name__ == '__main__':

    print(start_game)
    print(is_choice)
    while is_choice == 'b':
        p1 = int(input('choose your name:'))
        print(f'hi {p1} we are going to win')
        player1 = game.Game.create_player
        monster = game.Game.choose_random_monster
        print(f'your enemy is {monster}')
        print("the game start")
        print(rolling_dices)
        print(battle_begin)
    else:
        print('you are out from the game')


