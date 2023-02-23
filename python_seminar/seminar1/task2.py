# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

instruction = "Enter positive number: "
number = int(input(instruction))
x = 10
result = 0

if number < 0:
    number *= -1

while number / 10 > 0:
    result += number % x
    number //= x

print(result)