# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Вариант1 - используем коллекцию, однако в этом случае получим сортированный список

# from random import randint
#
#
# amount = int(input("Сколько чисел будет в последовательности: "))
# numbers = [randint(-10, 10) for i in range(amount)]
# print(f"Сформированный список: \n {numbers}")
# print(f"Неповтряющиеся элементы списка: \n {set(numbers)}")
#
# # Вариант2 - проверяем каждое число при добавлении
#
# amount = int(input("Сколько чисел будет в последовательности: "))
# unique_nums = []
# for i in range(amount+1):
#     number = randint(-10, 10)
#     unique_nums.append(number) if number not in unique_nums
#
# print(unique_nums)

# Вариант3 - если список уже задан

list_nums = [-8, 9, -3, 0, 4, -9, 10, 8, -3, 10, 2, 10, 0, -5, -9, -9, 4, -7, -2, -4]
new_list = []
[new_list.append(i) for enum, i in enumerate(list_nums[:]) if list_nums[enum] not in new_list]

print(new_list)

# Вариант4 - c исправлением по оригинальному заданию, только неповторяющиеся элементы

list_nums = [-8, 9, -3, 0, 4, -9, 10, 8, -3, 10, 2, 10, 0, -5, -9, -9, 4, -7, -2, -4]
new_list = []
[new_list.append(i) for i in list_nums[:] if len(list(filter(lambda x: x == i, list_nums))) == 1]

print(new_list)