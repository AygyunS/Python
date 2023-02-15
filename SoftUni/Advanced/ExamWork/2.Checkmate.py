
def is_inside(row, column, size):
    return 0 <= row < size and 0 <= column < size


def check_capture(king_row, king_column, queens, directions):
    queens_that_can_capture = []
    for direction in directions:
        test_king_row, test_king_column = king_row, king_column
        while is_inside(test_king_row, test_king_column, size):
            test_king_row, test_king_column = directions[direction](test_king_row, test_king_column)
            if [test_king_row, test_king_column] in queens:
                queens_that_can_capture.append([test_king_row, test_king_column])
                break
    return queens_that_can_capture


size = 8
matrix = []
king_row, king_column = None, None
queens = []
for row in range(size):
    line = input().split()
    matrix.append(line)

    for index, element in enumerate(line):
        if element == "K":
            king_row = row
            king_column = index
        elif element == "Q":
            queens.append([row, index])

directions = {
    "up": lambda row, column: (row - 1, column),
    "down": lambda row, column: (row + 1, column),
    "left": lambda row, column: (row, column - 1),
    "right": lambda row, column: (row, column + 1),
    "diagonal_left_up": lambda row, column: (row - 1, column - 1),
    "diagonal_right_up": lambda row, column: (row - 1, column + 1),
    "diagonal_left_down": lambda row, column: (row + 1, column - 1),
    "diagonal_right_down": lambda row, column: (row + 1, column + 1),
}

queens_result = check_capture(king_row, king_column, queens, directions)

if queens_result:
    print(*queens_result, sep="\n")
else:
    print("The king is safe!")