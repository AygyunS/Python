# Honey
from collections import deque


bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
operation = deque(input().split())

function = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "-": lambda x, y: x - y,
    "+": lambda x, y: x + y,
}

honey = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
        bees.appendleft(bee)
    elif nectar > bee:
        honey += abs(function[operation.popleft()](bee, nectar))

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")
