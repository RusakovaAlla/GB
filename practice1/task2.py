""" Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """


def checkPredicate():
    predicates = []
    for i in range(3):
        predicates.append(input(f"Введите значение {i+1} предикаты: "))
    if (not predicates[0] and not predicates[1] and not predicates[2]) == (not (predicates[0] or predicates[1] or predicates[2])):
        return "истинно"
    else:
        return "ложно"


print(f"Утверждение {checkPredicate()}")
