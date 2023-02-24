# 14. Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!

watermelons = int(input("enter the number of watermelons: "))

min = 1000
max = 0
i = 0
while i < watermelons:
    temp = int(input(f"enter weight of {i + 1} watermelon: "))
    if min > temp:
        min = temp
    if temp > max:
        max = temp
    i += 1

print(f"min = {min} \nmax = {max}")