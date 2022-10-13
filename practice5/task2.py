# Создайте программу для игры в ""Крестики-нолики"".

import numpy
from random import choice

import numpy as np


def game_field():
    """создадим поле"""
    field = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=str)

    return field


def field_cells(array):
    """список вариантов хода"""
    cells_coord = []
    [cells_coord.append(([j, k])) for j in range(0, array.shape[1]) for k in range(0, array.shape[0])]
    coord_dict = {i: cells_coord[i - 1] for i in range(1, 10)}

    return coord_dict


def check4win(array):
    """победные комбинации"""
    combos = [[(0, 0), (0, 1), (0, 2)],
              [(1, 0), (1, 1), (1, 2)],
              [(2, 0), (2, 1), (2, 2)],
              [(0, 0), (1, 1), (2, 2)],
              [(2, 0), (1, 1), (0, 2)],
              [(0, 0), (1, 0), (2, 0)],
              [(0, 1), (1, 1), (2, 1)],
              [(0, 2), (1, 2), (2, 2)]]
    for combo in combos:
        if array[combo[0][0]][combo[0][1]] == array[combo[1][0]][combo[1][1]] == array[combo[2][0]][combo[2][1]]:
            #array[combo[0]][combo[1]] == array[combo[1]][combo[1][1]] == array[combo[2][0]][combo[2][1]]:
            return array[combo[0][0]][combo[0][1]]
    return False


def input_players():
    """получаем имена игроков и определяем порядок ходов"""
    players = []
    for i in range(2):
        try:
            players.append(str(input(f'Имя игрока{i + 1}: ')))
        except Exception:
            print(f'Ну как без имени то?')
            continue
    moves_order = [choice(players)]
    [moves_order.append(i) for i in players if i not in moves_order]
    moves_order.append(["X", "0"])
    print(f"Первым ходит игрок {moves_order[0]}")

    return moves_order


# начинаем игру
place = game_field()  # сформировали поле
choice_list = field_cells(place) #координаты клеток
players_list = input_players() #принимаем игроков
winner = False #пока играть не начали, победителя нет
move = 0 #счетчик ходов

print(place)
while not winner:
    for i in range(0, 2):
        player_answer = int(input(f"Ход игрока {players_list[i]}. Куда ставим {players_list[2][i]}? Укажите место "))
        while player_answer not in choice_list.keys():
            try:
                player_answer = int(input(f"Ход игрока {players_list[i]}. Куда ставим {players_list[2][i]}? Укажите индекс "))
            except:
                print("Клетка занята")
                continue
        place[choice_list[player_answer][0]][choice_list[player_answer][1]] = players_list[2][i]
        print(place)
        choice_list.pop(player_answer)#удаляем из координат выбранный вариант
        move += 1
        if move > 4:
            winner = check4win(place)
            if winner:
                print(f"Победил игрок {players_list[players_list[2].index(winner)]}")
                break
        elif move == 9:
            print("Ничья!")
            break
