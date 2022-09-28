# Вариант1
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
    for i in range(0, len(some_list)):
        j = datetime.now().microsecond % 10 >> 1  # текущее время в микросекундах
        some_list[i], some_list[j] = some_list[j], some_list[i]
        # some_list.reverse()
    return some_list


# Проверка:
list1 = [8, -17, -12, 10, 3]
print(f"Вариант1 - {myShuffle1(list1)}")
print(f"Вариант2 - {myShuffle2(list1)}")
