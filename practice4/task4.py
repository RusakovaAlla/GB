#Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
from random import randint


polinom = str()
coef_dict = {}
k = int(input("Введите количество коэффициентов: "))
for i in range(k, -1, -1):
    coef_dict[i] = randint(0, 100)
    if coef_dict[i] != 0:
        if i != 0:
            if i == 1:
                if coef_dict[i+1] == 0:
                    polinom += f"{coef_dict[i]}x = 0"
                else:
                    polinom += f"{coef_dict[i]}x + "
            else:
                polinom += f"{coef_dict[i]}x**{i} + "
        else:
            polinom += f"{coef_dict[i]} = 0"
    else:
        continue

print(coef_dict, end="\n")
print(polinom)
with open("polinom.txt", "w") as file:
    file.write(polinom)
