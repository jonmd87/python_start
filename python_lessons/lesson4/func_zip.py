users = ['evghen', 'ivan', 'grigorii', 'boris']
ages = [20, 22, 23, 24, 25]

# функция zip пробегает только по минимальному входящему набору
print(list(zip(users, ages))) #[('evghen', 20), ('ivan', 22), ('grigorii', 23), ('boris', 24)]