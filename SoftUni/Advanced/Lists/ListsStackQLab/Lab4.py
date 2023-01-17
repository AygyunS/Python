# Water
# Read the starting quantity of water
start_quantity = int(input())

# Create a queue to store the people
people_queue = []

output = []

# Read the names of people until the command "Start" is received
name = input()
while name != "Start":
    people_queue.append(name)
    name = input()

# Read the commands until the command "End" is received
command = input()
while command != "End":
    # Check if the command is a refill command
    if command.startswith("refill"):
        # Extract the number of liters to refill
        liters = int(command.split()[1])
        start_quantity += liters
    else:
        # Extract the number of liters that the current person wants to get
        liters = int(command)

        # Check if there is enough water in the dispenser
        if liters <= start_quantity:
            # Remove the current person from the queue and reduce the water in the dispenser
            start_quantity -= liters
            person = people_queue.pop(0)
            output.append(f"{person} got water")
        else:
            # Remove the current person from the queue without reducing the water in the dispenser
            person = people_queue.pop(0)
            output.append(f"{person} must wait")
    command = input()

# Print the number of liters left
output.append(f"{start_quantity} liters left")
for line in output:
    print(line)
