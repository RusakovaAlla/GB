# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# with open("polinom41.txt", "r") as file:
#     part1 = file.readline()
#
# with open("polinom42.txt", "r") as file:
#     part2 = file.readline()


def polinom_des(polinom_in_file):
    with open(polinom_in_file, "r") as file:
        some_polinom = file.readline()
    some_polinom = some_polinom.split(" = ")[0]  # отделяем равно
    some_polinom = some_polinom.split(" + ")  # делим на элементы сам многочлен
    for enum, i in enumerate(some_polinom):  # отделяем степени
        i = i.split("**")
        if len(i) == 1:
            i.append('1' if 'x' in i[0] else '0')
        some_polinom[enum] = i
    for enum, i in enumerate(some_polinom):  # отделяем коэффициенты
        j = i[0].split("*")
        if len(j) == 1:
            j.insert(0, '1' if 'x' in j else '0')
        some_polinom[enum].insert(0, j[0])
    power_list = [] #список степеней
    for i in some_polinom:
            power_list.append(int(i[2]))

    return some_polinom, power_list


# разбираем полиномы на составляющие
pol1 = polinom_des("polinom41.txt")
pol2 = polinom_des("polinom42.txt")
print(pol1, '\n', pol2)

ext = max(pol2[1]+pol1[1])#ищем максимальную степень полиномов

sum_dict = {}
#складываем полиномы поэлементно
for i in range(ext, -1, -1):
    sum_dict[i] = 0
    for j in pol1[0]:
        if j[2] == str(i):
            if i != 0:
                sum_dict[i] += int(j[0])
                break
            else:
                sum_dict[i] += int(j[1])
                break
        else:
            continue
    for k in pol2[0]:
        if k[2] == str(i):
            if i != 0:
                sum_dict[i] += int(k[0])
                break
            else:
                sum_dict[i] += int(k[1])
                break
        else:
            continue
print(sum_dict)

sum_polinoms = str()
for i in range(ext, -1, -1):
    if sum_dict[i] != 0:
        if sum_dict[i] != 1:
            if i != 0:
                if i == 1:
                    if sum_dict[i + 1] == 0:
                        sum_polinoms += f"{sum_dict[i]}x = 0"
                    else:
                        sum_polinoms += f"{sum_dict[i]}x + "
                else:
                    sum_polinoms += f"{sum_dict[i]}x**{i} + "
            else:
                sum_polinoms += f"{sum_dict[i]} = 0"
        else:
            if i != 0:
                if i == 1:
                    if sum_dict[i + 1] == 0:
                        sum_polinoms += f"x = 0"
                    else:
                        sum_polinoms += f"x + "
                else:
                    sum_polinoms += f"x**{i} + "
            else:
                sum_polinoms += f" = 0"
    else:
        continue

print(sum_polinoms)

with open("sum_polinoms.txt", "w") as file:
    file.write(sum_polinoms)
