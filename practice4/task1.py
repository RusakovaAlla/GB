#Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

#Вариант1 - если понимаем, что на вход нужно подавать только отрицательные степени числа 10
import math

# def pres():
#     d = float(input("Задайте точность округления числа п: "))
#     while not (10**(-10) <= d <= 10**(-1)):
#         try:
#             d = float(input("Укажите точность округления числа п (10**(-x)): "))
#         except ValueError:
#             print("Повторите ввод")
#             continue
#
#     return round(math.pi, int(abs(math.log10(d))))
#
#
# print(pres())

#Вариант2 - подаем на вход любое число меньше 1
def pres():
    d = float(input("Задайте точность округления числа п: "))
    while not (10**(-10) <= d < 10**0):
        try:
            d = float(input("Укажите точность округления числа п (10**(-x)): "))
        except ValueError:
            print("Повторите ввод")
            continue

    return round(math.pi, len(str(d).split(".")[1]))


print(pres())
