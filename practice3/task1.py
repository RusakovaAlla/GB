from random import sample


def sum_nech_elems(list_of_nums):
    """Находим сумму элементов списка, стоящих на позиции с нечётным значением индекса элемента"""
    sum_nech = 0
    for num, i in enumerate(list_of_nums):
        if num % 2 != 0:
            sum_nech += i
        else:
            continue

    return sum_nech

#Проверка
list1 = sample(range(-100, 101), 20)
print(f"Список {list1} \nCумма значений элементов на нечетных позициях равна {sum_nech_elems(list1)}")
