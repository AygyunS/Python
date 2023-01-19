# Periodic Table
n = int(input())

first_set = set([])

for line in range(n):
    elements = input().split()
    for el in elements:
        first_set.add(el)
    elements = []

(lambda: [print(x) for x in first_set])()
