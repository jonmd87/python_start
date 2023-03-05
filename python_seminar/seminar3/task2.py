# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число. 1 2 3 4 5 K = 3 -> 3 4 5 1 2


list = []
for i in range(10):
    list.append(i)

print(f'Here is a list = {list}')
shift = int(input("enter shift: "))
print(list)

for i in range(shift):
    list.insert(0, list.pop())
    print(list)
print(list)