def printStars(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "* " * (i + 1))

printStars(int(input()))
