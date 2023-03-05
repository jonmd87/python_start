# Задача 16: Требуется вычислить, сколько раз встречается
# некоторое число X в массиве из случайных чисел.
# Пользователь в первой строке вводит натуральное число N,
# количество элементов в массиве. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
    # -> 1

import random

list = []
quantity = int(input('Enter number of positions: '))
for i in range(quantity):
    list.append(random.randint(0, 10))

number = int(input('Now enter number(from 1 to 10): '))
counter = 0
for i in list:
    if i == number:
        counter += 1
print(list)
print(f'{number} --> {counter}')