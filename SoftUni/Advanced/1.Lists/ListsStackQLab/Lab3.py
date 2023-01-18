# Supermarket

queue = []

while True:
    line = input()

    if line == "End":
        break
    elif line == "Paid":
        for customers in queue:
            print(customers)
        queue = []
    else:
        queue.append(line)
print(f"{len(queue)} people remaining.")
