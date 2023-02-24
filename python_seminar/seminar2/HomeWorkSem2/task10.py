# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 1 - герб, 0 - решка
# Ввод:
# 4 - число монет
# 0
# 1
# 1
# 1
# Вывод:
# 1

from random import randint

coins = int(input('enter the number of coins: '))
tails = 0

for i in range(coins):
    coin = randint(0, 1)
    print(f'{coin}', end=' ')
    if (coin == 0):
        tails += 1
print(f'need to flip over {tails}', end=' ')
if tails > 1:
    print('coins')
else:
    print('coin')