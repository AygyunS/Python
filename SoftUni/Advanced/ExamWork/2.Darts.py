
def is_outside(row, column, size):
    return row < 0 or row >= size or column < 0 or column >= size


def corresponding_numbers(row, column, size, matrix):
    return int(matrix[0][column]) + int(matrix[size - 1][column]) + int(matrix[row][0]) + int(matrix[row][size - 1])


players_names = input().split(", ")
players_scores = [501, 501]
players_throws = [0, 0]
size = 7
matrix = [input().split() for row in range(size)]
winner = ""
winner_throws = 0

while not winner:
    player = players_names[0]
    players_throws[0] += 1
    throw = [int(i) for i in input().lstrip("(").rstrip(")").split(", ")]
    row, column = throw
    if not is_outside(row, column, size):
        if not matrix[row][column].isalpha():
            players_scores[0] -= int(matrix[row][column])
        elif matrix[row][column] == "D":
            players_scores[0] -= 2 * corresponding_numbers(row, column, size, matrix)
        elif matrix[row][column] == "T":
            players_scores[0] -= 3 * corresponding_numbers(row, column, size, matrix)
        elif matrix[row][column] == "B":
            winner = player
            winner_throws = players_throws[0]
            break
        if players_scores[0] <= 0:
            winner = player
            winner_throws = players_throws[0]
            break
    players_names[0], players_names[1] = players_names[1], players_names[0]
    players_scores[0], players_scores[1] = players_scores[1], players_scores[0]
    players_throws[0], players_throws[1] = players_throws[1], players_throws[0]

print(f"{winner} won the game with {winner_throws} throws!")