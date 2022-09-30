"""Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов."""
# Вариант1
"""не трогаем исходный список"""
list1 = [1.1, 1.2, 3.1, 5, 10.01]
max_frac = list1[0] % 1
min_frac = list1[0] % 1
for i in list1[1:]:
    if max_frac < (i % 1):
        max_frac = i % 1
    elif min_frac > (i % 1):
        min_frac = i % 1
diff_maxmin = (max_frac - min_frac)*100 // 1 #если количество десятичных знаков критично, получаем строго 0.19
print(diff_maxmin/100)
#print(round(max_frac - min_frac, 2)) #число округляется до 0.2

# Вариант2
"""если список не важен, заменим элементы"""
list1 = [1.1, 1.2, 3.1, 5, 10.01]
for num, i in enumerate(list1):
    list1[num] = i % 1
print(round(max(list1) - min(list1), 2)) #число округляется до 0.2
