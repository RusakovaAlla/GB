"""Напишите программу, которая будет преобразовывать десятичное число в двоичное."""

# Вариант1
"""ничего не делаем, пользуемся стандартным форматированием"""
print(format(11, 'b'))

# Вариант2
import math

"""проходимся циклом и считаем сами
"""
string_binary = ""
number = 11
for i in reversed(range(int(math.log(number, 2) // 1 + 1))):
    if 2 ** i <= number:
        string_binary += "1"
        number -= 2 ** i
    else:
        string_binary += "0"
print(string_binary)
