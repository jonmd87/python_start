# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

from array import array

def arithmetic_progression(arr,differ):
    for i in range(len(arr)):
        if i != 0:
            arr[i] = arr[i - 1] + differ


first = int(input("Enter first element: "))
differ = int(input("Now enter difference: "))
quantity = int(input("Now enter quantity of elements: "))

arr = array('i', [first for i in range(quantity)])
arithmetic_progression(arr, differ)

for i in range(len(arr)):
    print(arr[i])