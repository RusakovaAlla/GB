"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
"""


def checkPoint():
    point = [None, None]
    while type(point[0]) != int or type(point[1]) != int:
        try:
            point[0], point[1] = map(int, input("Введите координаты точки через запятую: ").split(","))
        except ValueError:
            print("Вводить нужно строго числа!")
            continue

    return point

def calcDistance():
    p1 = checkPoint()
    p2 = checkPoint()
    s = round(
        ((p1[0]-p2[0])**2 + ((p1[1]-p2[1])**2))**0.5,
        2
    )
    return p1, p2, s


distance = calcDistance()
print(f"Расстояние между точками {distance[0]} и {distance[1]} на плоскости равно {distance[2]}")