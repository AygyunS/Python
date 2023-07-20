import sys


def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return power(1/x, -n)
    if n % 2 == 0:
        y = power(x, n/2)
        return y * y
    else:
        return x * power(x, n-1)


x = int(sys.argv[1])
n = int(sys.argv[2])
print(power(x, n))




