# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

user_str = input("please enter a user_str: ")
dictionary = dict.fromkeys(set(user_str), 0)

for letter in user_str:
    if dictionary.get(letter) > 0:
        print(f'{letter}_{dictionary.get(letter)}', end=' ')
    else:
        print(letter, end=' ')
    dictionary[letter] += 1
