# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*

# 385916 -> yes
# 123456 -> no

INSTRUCTION = 'Ener ticket number: '
ERROR = 'error'
ticket_number = str(input(INSTRUCTION))

if len(ticket_number) == 6 and ticket_number.isdigit(): # проверяем колво цифр и наличие букв в номере билета
    head = 0
    tail = int(len(ticket_number) - 1)
    result = 0
    for i in range(len(ticket_number) // 2):
        result += (int(ticket_number[i]) - int(ticket_number[tail]))
        tail -= 1

    if (result != 0):
        print("{} --> {}".format(ticket_number, 'NO'))
    else:
        print("{} --> {}".format(ticket_number, 'Yes'))

else:
    print(ERROR)