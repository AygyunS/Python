n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
output = []
while True:
    command = input().split()
    if command[0] == "END":
        break
    elif command[0] == "Add":
        row, col, value = int(command[1]), int(command[2]), int(command[3])
        if 0 <= row < n and 0 <= col < n:
            matrix[row][col] += value
        else:
            output.append("Invalid coordinates")
    elif command[0] == "Subtract":
        row, col, value = int(command[1]), int(command[2]), int(command[3])
        if 0 <= row < n and 0 <= col < n:
            matrix[row][col] -= value
        else:
            output.append("Invalid coordinates")

[print(x) for x in output]

for row in matrix:
    print(" ".join(str(x) for x in row))
