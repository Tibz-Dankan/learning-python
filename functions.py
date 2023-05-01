# Functions are used for code reuse (Dont Repeat Yourself(DRY))

def add(x, y):
    return x+y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))