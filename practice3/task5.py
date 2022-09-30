"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов."""

n = int(input("Число: "))
pos_fibonacchi = []
neg_fibonacchi = []
for i in range(0, n+1):
    if i == 0:
        pos_fibonacchi.append(0)
    elif i == 1:
        pos_fibonacchi.insert(1, 1)
        neg_fibonacchi.insert(0, 1)
    else:
        pos_fibonacchi.append(pos_fibonacchi[i-2]+pos_fibonacchi[i-1])
        neg_fibonacchi.insert(0, (-1)**(i+1)*pos_fibonacchi[i])

print(neg_fibonacchi+pos_fibonacchi)
