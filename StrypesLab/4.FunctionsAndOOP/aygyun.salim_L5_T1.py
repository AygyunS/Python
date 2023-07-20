import sys


def fibonacci(n, cache):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
        return cache[n]


start = int(sys.argv[1])
end = int(sys.argv[2])
output = []
cache = {0: 0, 1: 1}
for i in range(start-1, end):
    output.append(fibonacci(i, cache))

print(output)
