# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# Вариант1 - подключим numexpr
# import numexpr as ne
#
# with open("strings.txt", "r") as calculations:
#     cases = [i.rstrip() for i in calculations.readlines()]
#
# for i in cases:
#     print(f"{i} = {ne.evaluate(i)}")

# Вариант2 - разберем руками строку
with open("strings.txt", "r") as calculations:
    cases = [i.rstrip() for i in calculations.readlines()]


def parse_str(string):
    """разбор каждого примера из строк"""
    string_to_list = []
    while string:
        for pos, elem in enumerate(string):
            if not elem.isdigit():
                number = int(string[0:pos])
                string = string[string.find(elem) + 1:]
                string_to_list.append(number)
                string_to_list.append(elem)
                break
            else:
                if len(string) == 1:
                    string_to_list.append(int(elem))
                    string = string[string.find(elem) + 1:]
                    break
                else:
                    continue

    return string_to_list


def evaluating(list):
    """решаем"""
    eval_list = 0
    while list:
        if "*" in list:
            pos = list.index("*")
            eval_list = list[pos - 1] * list[pos + 1]
            del list[pos - 1:pos + 2]
            list.insert(pos - 1, eval_list)
            continue
        elif "/" in list:
            pos = list.index("/")
            eval_list = list[pos - 1] / list[pos + 1]
            del list[pos - 1:pos + 2]
            list.insert(pos - 1, eval_list)
            continue
        elif "+" in list:
            pos = list.index("+")
            eval_list = list[pos - 1] + list[pos + 1]
            del list[pos - 1:pos + 2]
            list.insert(pos - 1, eval_list)
            continue
        elif "-" in list:
            pos = list.index("-")
            eval_list = list[pos - 1] - list[pos + 1]
            del list[pos - 1:pos + 2]
            list.insert(pos - 1, eval_list)
            continue
        break

    return eval_list


cases_solved = []
cases_solved = [parse_str(i) for i in cases]  # обрабатываем каждую строку
for i in range(len(cases_solved)):
    cases_solved[i - 1] = evaluating(cases_solved[i - 1])  # решаем
for i in range(len(cases)):
    cases[i - 1] += "=" + str(cases_solved[i - 1])  # собираем в строки
with open("solved.txt", "w") as file:  # записываем в файл
    [file.write(cases[i] + '\n') for i in range(len(cases))]
