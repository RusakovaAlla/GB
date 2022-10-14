"""Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1"""

def rangeDict():
    number = None
    while type(number) != int:
        try:
            number = int(input("Введите целое число: "))
            break
        except ValueError:
            print(f"Вводите только целые числа!")
            continue
    num_dict = {i: 3*i+1 for i in range(1, number+1)}

    return num_dict


print(rangeDict())
