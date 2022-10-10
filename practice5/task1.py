#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета.
#Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#За один ход можно забрать не более чем 28 конфет.
#Все конфеты оппонента достаются сделавшему последний ход.
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота "интеллектом"

from random import choice, randint


def game_of_sweets(sweets, per_move):
    """
    Для победы первого игрока к последней паре ходов второму игроку должно остаться {per_move+1} конфет.
    Для победы ходящего первым игрока за каждый ход также должны убираться {per_move+1}конфет
    """
    for_first_take = sweets-sweets//(per_move+1)*(per_move+1)

    return for_first_take, (f"Первому игроку для победы нужно забрать {for_first_take} конфет")


print(game_of_sweets(2021, 28)[1])
