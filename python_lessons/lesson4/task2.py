list1 = [x for x in range(1, 20)]
print(list1)
print(list(filter(lambda x: x%2 == 0, list1)))
print(list(map(lambda x: x+(1/2), list1)))