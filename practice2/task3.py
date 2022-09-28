"""
Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму
"""


def sumNumber():
    number = None
    while type(number) != int:
        try:
            number = int(input("Введите число: "))
            break
        except ValueError:
            print(f"Вводите только целые числа!")
            continue
    sum_num = []
    for i in range(1, number + 1):
        sum_num.append(round((1+(1/i))**i, 2))

    return sum_num, round(sum(sum_num), 2)


print(sumNumber())
