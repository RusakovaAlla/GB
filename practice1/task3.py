'''
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)
'''
import math


def quarterNum():
    x = 0
    coordinates = dict({
        1: (math.inf, math.inf),
        2: [-math.inf, math.inf],
        3: [-math.inf, -math.inf],
        4: [math.inf, -math.inf]
    })
    while x not in range(1, 5):
        try:
            x = int(input("Введите номер четверти координатной плоскости: "))
            if x < 1 or x > 4:
                print(f"Номер четверти может принимать значения от 1 до 4 включительно. Повторите ввод")
                continue
            else:
                pass
        except ValueError:
            print("Вводить нужно строго числа!")
            continue

    return print(f'Возможные координаты точки: {coordinates[x]}')

