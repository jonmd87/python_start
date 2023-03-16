array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('[', end= ' ')
for i in array:
    if i % 2 == 0:
        print(f'({i},{i**2})', end= ' ')

print(']')
