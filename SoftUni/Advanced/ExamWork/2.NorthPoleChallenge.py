def current_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "Y":
                return i, j

def is_outside(row, column, rows, columns):
    return row < 0 or column < 0 or row >= rows or column >= columns
def move_in_matrix(matrix, current_postion, direction, steps):
    row, col = current_postion
    if direction == "up":
        row -= steps
    elif direction == "down":
        row += steps
    elif direction == "left":
        col -= steps
    elif direction == "right":
        col += steps
    return row, col

rows, cols = [int(i) for i in input().split(", ")]

decorations = 0
gifts = 0
cookies = 0

matrix = [input().split(" ") for j in range(rows)]

# print(*matrix, sep="\n")


while True:
    command = input()
    if command == "End":
        break
    command = command.split("-")


    if len(command) == 5:
        action, row, col, value = command
        row, col, value = int(row), int(col), int(value)
        if row < 0 or row >= rows or col < 0 or col >= cols:
            print("Invalid coordinates")
        else:
            if action == "Add":
                matrix[row][col] = int(matrix[row][col]) + value
            elif action == "Subtract":
                matrix[row][col] = int(matrix[row][col]) - value
    else:
        print("Invalid coordinates")