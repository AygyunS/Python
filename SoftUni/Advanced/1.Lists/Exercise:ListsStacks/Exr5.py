n = int(input())

# Read the petrol pump information
pumps = []
for i in range(n):
    a, d = map(int, input().split())
    pumps.append((a, d))

# Find the first petrol pump from where the truck can complete the circle
total_petrol = 0
start_index = 0
for i in range(n):
    total_petrol += pumps[i][0] - pumps[i][1]
    if total_petrol < 0:
        total_petrol = 0
        start_index = i + 1

# Print the result
print(start_index)