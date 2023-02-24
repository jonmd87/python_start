# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k),
# не превосходящие числа N.
# Ввод:
# 6
# Вывод
# 1 2 4
# Ввод
# 24
# Вывод
# 1 2 4 8 16

degree = 0
two = 2
result = two ** degree
number = int(input("enter number: "))

while result  <= number:
    print(f'{result}', end= ' ')
    degree += 1
    result = two ** degree
