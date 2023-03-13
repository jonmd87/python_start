# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, \
# и возводит число А в целую неотрицательную степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def degree(num, deg):
    if deg == 1:
        return num
    return num * degree(num, deg - 1)


a = int(input("Enter number: "))
b = int(input("Now enter degree: "))

print(degree(a, b))
