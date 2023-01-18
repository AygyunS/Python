# Periodic Table

elements = set()

for line in range(int(input())):
    for el in input().split():
        elements.add(el)

print(*elements, sep="\n")
