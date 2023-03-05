# Дан список чисел.
# Определите, сколько в нем встречается различных чисел.
# 1 2 3 1 2 4 -> 4 (1 2 3 4)

import random

max = 10
num = int(input(f"enter number of elements (0 < N < {max}): "))
list = []

for i in range(num):
    list.append(random.randint(0, max - 3))
print(list)

dictionary = dict(zip(list, list))
print(f'quantity = {len(dictionary)} ==> {dictionary.keys()}')