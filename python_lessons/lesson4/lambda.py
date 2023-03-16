def calc(a, b):
    return a + b

def calc1(a, b):
    return a * b

def calc2(a, b):
    return a / b

def func(op, a, b):
    return op(a, b)

print(func(calc2, 5, 7))
print(func(lambda a,b: a * b, 5, 8 ))