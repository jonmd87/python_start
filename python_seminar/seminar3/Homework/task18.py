# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n)
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N,
# количество элементов в массиве. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

quantity = int(input('enter number of positions: '))
list = []

for i in range(quantity):
    list.append(random.randint(0, quantity))

print(list)
number = int(input('now enter number that i need to search: '))
flag = True
index = 0
while flag:
    if list.count(number - index) > 0:
        flag = False
        print(number - index)
    if list.count(number + index) > 0:
        flag = False
        print(number + index)
    index += 1