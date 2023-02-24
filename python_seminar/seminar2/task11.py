# дано число n > 1
# определить каким по счету числом фибоначи оно является
# если n не является числом фибоначи вывести -1

number = int(input('Enter 0 or  positive number: '))
if (number > 1):
    prew = 0
    fibonacci = 2
    counter = 4
    while fibonacci < number:
        temp = fibonacci
        fibonacci += prew
        prew = fibonacci - prew
        counter += 1
    print(f"position = {counter}")
elif number == 1:
    print("position = 2 or 3")
elif number == 0:
    print("position = 1")
else:
    print("only 0 or positive numbers!!!")