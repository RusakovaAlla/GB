from secrets import randbelow #нельзя random - возьмём другой :)


def myShuffle(some_list):
    for i in reversed(range(1, len(some_list))):
        j = randbelow(i)
        some_list[i], some_list[j] = some_list[j], some_list[i]

    return some_list


# Проверка:
# list1 = [8, -17, -12, 10, 3]
# #print(myShuffle(list1))

