"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
"""
from random import randint


def numElem():
    """контроль ввод числа, формирование списка"""
    number = None
    rangelist = []
    while type(number) != int:
        try:
            number = int(input("Введите число для определения состава последовательности: "))
            for num in range(1, number + 1):
                rangelist.append(randint(-number, number))
            break
        except ValueError:
            print(f"Вводите только целые числа!")
            continue

    return rangelist


def readPos(file):
    """список номеров позиций из полученного файла"""
    positions = []
    with open(file, "r") as pos:
        for line in pos:
            try:
                positions.append(int(line))
            except ValueError:
                continue
    pos.close()

    return positions


N = numElem()
print(N)# наш список
mult_pos = readPos("file.txt")
print(mult_pos)
mult_nums = 1

if mult_pos:
    for pos in mult_pos:
        try:
            if pos in range(0, len(N)+1):
                mult_nums *= N[pos]
                print(N[pos])
                continue
            else:
                raise IndexError
        except IndexError:
            print(f"В списке только {len(N)} элементов. Элемента с индексом {pos} нет")
else:
    print("Файл был пуст. Ничего не посчитаем")
    mult_nums = 0


