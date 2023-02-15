from functools import reduce


#recursive function
def multiply(*args):
    if len(args) == 1:
        return args[0]
    return args[0] * multiply(*args[1:])

def mul(*args):
    return reduce(lambda a, b: a * b, args)

print(multiply(1, 4, 5))
print(mul(5))


