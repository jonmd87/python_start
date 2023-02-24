# По данному неотрицательному числу n вычислить факториал от n (!n)

num = int(input("Enter positive number: "))

if (num < 0):
    print('Only positive number!!!')
else:
    result = 1
    while num > 0:
        result *= num
        num -= 1
    print("!n = {} ".format(result))