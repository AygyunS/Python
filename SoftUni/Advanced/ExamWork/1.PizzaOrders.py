# Pizza orders
from collections import deque

pizza_order = deque(map(int, input().split(", ")))
employees_capacities = deque(map(int, input().split(", ")))


for i in list(pizza_order):
    if i > 10:
        pizza_order.remove(i)
    elif i < 1:
        pizza_order.remove(i)

pizza_order = [x for x in pizza_order if x <= 10]


all_pizzas = 0

while True:
    if not pizza_order:
        break
    if not employees_capacities:
        break

    current_pizza = pizza_order.popleft()
    current_employee = employees_capacities.pop()

    if current_pizza <= current_employee:
        all_pizzas += current_pizza
    else:
        current_pizza -= current_employee
        all_pizzas += current_employee
        pizza_order.appendleft(current_pizza)


if not pizza_order:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {all_pizzas}")
    print(f"Employees: {', '.join(map(str, employees_capacities))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_order))}")
