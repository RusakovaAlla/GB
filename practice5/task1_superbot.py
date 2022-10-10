#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета.
#Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#За один ход можно забрать не более чем 28 конфет.
#Все конфеты оппонента достаются сделавшему последний ход.
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

#Бот будет считать все, безжалостно :)
#Бот ходит первым - у игрока нет шансов.
#Если игрок ходит первым и ошибется с количеством выбираемых конфет хоть раз, бот выиграл

from random import choice, randint


def game_of_sweets(sweets, per_move):
    """
    Для победы первого игрока к последней паре ходов второму игроку должно остаться {per_move+1} конфет.
    Для победы ходящего первым игрока за каждый ход также должны убираться {per_move+1}конфет
    """
    for_first_take = sweets-sweets//(per_move+1)*(per_move+1)

    return for_first_take


def control_player_takeout(to_take=0):
    while to_take < 1 or to_take > 28:
        try:
            to_take = int(input("Сколько конфет возьмете? "))
        except ValueError:
            continue

    return to_take

#зададим количество
sweets, sweets_per_move_max = 2021, 28
player1, bot = 0, 0 #счётчик количества ходов каждого игрока
#проведем жеребьёвку
list_players = ["player1", "bot"]
moves_order = [choice(list_players)]
print(f"Первым ходит игрок {moves_order}")
[moves_order.append(i) for i in list_players if i not in moves_order]
print(moves_order)
while sweets != 0:
    if moves_order == ["player1", "bot"]:
        for i in moves_order:
            if player1 == 0 or bot == 0:
                if i == 'player1':
                    takeout = control_player_takeout()
                    sweets -= takeout
                else: #ходит бот
                    takeout = randint(1, 28) if takeout == 20 else 20-takeout if takeout < 20 else game_of_sweets(sweets, sweets_per_move_max)[0]
                    print(f'Игрок {i} берет {takeout} конфет')
                    sweets -= takeout
            else:
                if i == 'player1':
                    takeout = control_player_takeout()
                    sweets -= takeout
                else: #ход бота
                    takeout = randint(1, 28) if game_of_sweets(sweets, sweets_per_move_max)[0] == 0 else game_of_sweets(sweets, sweets_per_move_max)[0]
                    print(f'Игрок {i} берет {takeout} конфет')
                    sweets -= takeout
            if sweets < 29:
                winner = i
                break
        player1 += 1
        bot += 1
    else:
        for i in moves_order:
            if player1 == 0 or bot == 0:
                if i == 'bot':
                    takeout = game_of_sweets(sweets, sweets_per_move_max)[0]
                    print(f'Игрок {i} берет {takeout} конфет')
                    sweets -= takeout
                else: #ход игрока
                    takeout = control_player_takeout()
                    sweets -= takeout
            else:
                if i == 'bot':
                    takeout = 29 - takeout
                    print(f'Игрок {i} берет {takeout} конфет')
                    sweets -= takeout
                else: #ход игрока
                    takeout = control_player_takeout()
                    sweets -= takeout
            if sweets < 29:
                winner = i
                break
        bot += 1
        player1 += 1
else:
    print(f"Победил {winner}!")
