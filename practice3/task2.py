"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д."""
list1 = [2, 3, 4, 5, 6]
mult_list = []
for i in range(0, len(list1)): #с использованием numpy от цикла можно избавиться
    mult_list.append(list1[i] * list1[::-1][i]) #поэлементно перемножаем два списка
if len(list1) % 2 != 0: #удаляем лишние элементы
    del mult_list[len(list1)//2+1:]
else:
    del mult_list[len(list1) // 2:]
print(mult_list)