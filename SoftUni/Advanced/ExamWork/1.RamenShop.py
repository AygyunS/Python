from collections import deque

first_line = deque(map(int, input().split(", ")))
second_line = deque(map(int, input().split(", ")))

result = []

while first_line and second_line:
    bowls = first_line.pop()
    customers = second_line.popleft()

    if bowls == customers:
        continue
    elif bowls > customers:
        first_line.append(bowls - customers)
    elif customers > bowls:
        second_line.appendleft(customers - bowls)

if not second_line:
    print("Great job! You served all the customers.")
    if not first_line:
        exit()

if first_line:
    print("Bowls of ramen left: " + ", ".join(map(str, first_line)))
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print("Customers left: " + ", ".join(map(str, second_line)))


