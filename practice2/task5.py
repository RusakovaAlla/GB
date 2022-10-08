# # Вариант1
from secrets import randbelow #нельзя random - возьмём другой :)


def myShuffle1(some_list):
    """
    список на выходе при каждом запуске функции получаем разный
    """
    for i in range(1, len(some_list)):
        j = randbelow(i)
        some_list[i], some_list[j] = some_list[j], some_list[i]

    return some_list

# Вариант2
from datetime import datetime


def myShuffle2(some_list):
    """%(len(some_list)-1),
    это лучше, длину списка контролировать не нужно"""
    for i in range(0, len(some_list)-1):
            j = datetime.now().microsecond % 10 >> 3
            some_list[i], some_list[j] = some_list[j], some_list[i]
    return some_list


# Проверка:
list1 = [10, -12, -13, 8]
print(f"Вариант1 - {myShuffle1(list1)}")
print(f"Вариант2 - {myShuffle2(list1)}")
