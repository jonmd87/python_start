# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит первый массив через пробел и второй через пробел на разных строках.
# [1, 2, 3, 4, 5]
# [1, 2, 3] -> [4, 5]

user_input = input("enter the first list of numbers, separated with space: ")
set1 = set(map(int, user_input.split()))

user_input = input("enter the second list of numbers, separated with space: ")
set2 = set(map(int, user_input.split()))

print(set1.difference(set2))
