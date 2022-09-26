'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
'''


def checkDayWeekend():
    day = 0
    while day not in range(1, 8):
        try:
            day = int(input("Введите номер дня недели в диапазоне от 1 до 7: "))
            if day not in [6, 7]:
                text = "К сожалению, это рабочий день"
            else:
                text = "Это выходной!"
        except ValueError:
            print("Вводить нужно строго числа!")
            continue
    return print(text)

checkDayWeekend()