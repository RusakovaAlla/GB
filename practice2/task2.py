"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
"""
from math import factorial


def multiplyNumber():
    number = None
    while type(number) != int:
        try:
            number = int(input("Введите число: "))
            break
        except ValueError:
            print(f"Вводите только целые числа!")
            continue
    mult_num = []
    for i in range(1, number + 1):
        mult_num.append(factorial(i))

    return mult_num


print(multiplyNumber())
