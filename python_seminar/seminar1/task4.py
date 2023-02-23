# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
# если получается некорректное разделение - напечатать "Неверное S"

INSTRUCTION = 'Введите количество сделанных журавликов(S): '
ERROR = '!!!Wrong (S)!!!'

num = int(input(INSTRUCTION))
pet =0
serj = 0
kat = 0
if num % 6 == 0: # почему 6: 3 участника и один из участников сделал в 2 раза больше
    pet = num // 6
    serj = pet
    kat = (pet + serj) * 2
    print ('{} {} {}'.format(pet, kat, serj))
else:
    print('wrong number')
