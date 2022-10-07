# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

multipliers = []
check_mults = []
while n < 1 or not isinstance(n, int):
    n = int(input("Введите натуральное число N: "))
for i in range(2, n + 1):
    if n % i == 0:
        check_mults = []
        j = 1
        while len(check_mults) <= 2 and j <= i:
            if i % j == 0:
                check_mults.append(j)
            else:
                pass
            j += 1
        if len(check_mults) == 2:
            multipliers.append(i)
        else:
            continue
    else:
        continue

print(multipliers)


