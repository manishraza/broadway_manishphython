# lambda in python are the elegant to create a on-online functions



def addition(a, b):
    return a + b
sum = lambda a, b: a + b
print(sum(4, 5))

is_even = lambda  x: x % 2 == 0
print(is_even(4))