# Производная от задачи 5 - что если, коэффициенты отрицательные
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def polinom_des(polinom_in_file):
    with open(polinom_in_file, "r") as file:
        some_polinom = file.readline()
    some_polinom = some_polinom.replace(" ", "")
    some_polinom = some_polinom.split("=")[0]  # отделяем равно
    # обрабатываем отрицательные коэффициенты, если есть
    some_polinom = list(some_polinom)
    for i in range(len(some_polinom)-1, -1, -1):
        if some_polinom[i] == "-":
            some_polinom.insert(i, "+")
            continue
        else:
            pass
    some_polinom = "".join(map(str, some_polinom))
    some_polinom = some_polinom.split("+")  # делим на элементы сам многочлен
    #если первый элемент в строке был отрицательным, то после обработки в списке появится пустой элемент с индексом 0
    try: #уберем пустой элемент, если он был, с обработкой исключения
        some_polinom.remove('')
    except ValueError:
        pass
    for enum, i in enumerate(some_polinom):  # отделяем степени
        i = i.split("**")
        if len(i) == 1:
            i.append('1' if 'x' in i[0] else '0')
        some_polinom[enum] = i
    for enum, i in enumerate(some_polinom):  # отделяем коэффициенты
        j = i[0].split("*")
        if len(j) == 1:
            j.insert(0, '1' if 'x' in j else ('-1' if '-x' in j else '0'))
        some_polinom[enum].insert(0, j[0])
    try: #для красоты и понимания происходящего, заменить отрицательный x
        for i in some_polinom:
            if '-x' in i:
                i[i.index('-x')] = 'x'
            else:
                continue
    except ValueError:
        pass
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
    if i == 0:
        if sum_dict[i] == 0:
            sum_polinoms += f"=0"
        elif sum_dict[i] == -1:
            sum_polinoms += f"{sum_dict[i]}=0"
        elif sum_dict[i] < -1:
            sum_polinoms += f"{sum_dict[i]}=0"
        elif sum_dict[i] > 0:
            sum_polinoms += f"+{sum_dict[i]}=0"
    elif i == 1:
        if sum_dict[i] == 0:
            sum_polinoms += f"=0"
        elif sum_dict[i] == -1:
            sum_polinoms += f"-x"
        elif sum_dict[i] == 1:
            sum_polinoms += f"+x"
        elif sum_dict[i] > 1:
            sum_polinoms += f"+{sum_dict[i]}*x"
        else:
            sum_polinoms += f"{sum_dict[i]}*x"
    elif i < ext:
        if sum_dict[i] == 0:
            pass
        elif sum_dict[i] < -1:
            sum_polinoms += f"{sum_dict[i]}*x**{i}"
        elif sum_dict[i] == 1:
            sum_polinoms += f"+x**{i}"
        elif sum_dict[i] > 1:
            sum_polinoms += f"+{sum_dict[i]}*x**{i}"
        else:
            sum_polinoms += f"-x**{i}"
    elif i == ext:
        if sum_dict[i] == -1:
            sum_polinoms += f"-x**{i}"
        elif sum_dict[i] < -1:
            sum_polinoms += f"{sum_dict[i]}*x**{i}"
        elif sum_dict[i] == 1:
            sum_polinoms += f"x**{i}"
        elif sum_dict[i] > 1:
            sum_polinoms += f"{sum_dict[i]}*x**{i}"
        else:
            pass

print(sum_polinoms)

with open("sum_polinoms.txt", "w") as file:
    file.write(sum_polinoms)
