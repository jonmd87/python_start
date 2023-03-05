# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером) 1 2 3 4 3 2 1 -> 3 (2 , 3 , 4)

import random

list = [1, 2, 3, 0, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
max = 10
# for i in range(max + max):
#     list.insert(i, random.randint(0, max / 2))
print(list)

new_list = []
z = 0
length = len(list) - 1
while z < length:
    if list[z] < list[z + 1]:
        x = 0
        temp = []
        z += 1
        while z < length and list[z] < list[z + 1]:
            temp.insert(x, list[z])
            z += 1
            x += 1
        temp.insert(x, list[z])
        if len(new_list) < len(temp):
            new_list = temp
    z += 1
print(new_list)