import secrets
from random import shuffle
from os import urandom


def myShuffle(some_list):
    for i in range(1, len(some_list)):
        j = int.from_bytes(int.to_bytes(i, i, 'little'), 'big')
        some_list[i], some_list[j] = some_list[j], some_list[i]
    return some_list


list1 = [8, -17, -12, 10, 3] #для моей функции
list2 = [8, -17, -12, 10, 3] #для random
list3 = [8, -17, -12, 10, 3] #для secrets

print(f"Результат работы myShuffle")
print(myShuffle(list1))
# print(f"Результат работы random")
# shuffle(list2)
# print(f"Работа модуля random \n {list22}")
# print(f"Результат работы secrets")
# for i in range(1, len(list3)):
#     j = secrets.randbelow(i)
#     list3[i], list3[j] = list3[j], list3[i]
# print(list3)
# shuffle(lst)
# print(f"Работа модуля random \n {lst}")
