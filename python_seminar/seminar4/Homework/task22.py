# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 списка.
# 1 строка - первый список через пробел.
# 2 строка - второй список через пробел.

string = input("enter first list of digits(split with space): ")
list1 = list(string.split())

string = input("enter second list of digits(split with space): ")
list2 = list(string.split())
print(list1)
print(list2)

list3 = list()
for i in list1:
    if i in list2:
        list3.append(i)

list3.sort()
print(list3)