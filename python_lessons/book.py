import random

name = ('evgheni', 'gherasimenco', 'from', 'moldova', 'deutschland', "ukraine", 'rusland')
for i in range(0, 5):
    print(f'{random.choice(name)} --> {random.choice(random.choice(name))}')