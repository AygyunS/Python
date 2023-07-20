import math


def f(x):
    return x * x * x + 3 * x - 5


def bisection(a, b, func):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers")
    if func(a) * func(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    while abs(b - a) > 0.001:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint
        elif func(midpoint) * func(a) < 0:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2


try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    print("Root of x^3 + 3x - 5: ", bisection(a, b, f))


    def g(x):
        return math.exp(x) - 2 * x - 2


    print("Root of exp(x) - 2x - 2: ", bisection(0, 1, g))
except ValueError as e:
    print(e)


