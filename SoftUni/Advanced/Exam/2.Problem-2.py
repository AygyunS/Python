rows, cols = [int(x) for x in input().split()]
moves, touches = 0, 0
matrix, pos = [], []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    matrix.append(input().split())
    if 'B' in matrix[row]:
        pos = [row, matrix[row].index('B')]

while touches < 3:
    command = input()

    if command == 'Finish':
        break

    r, c = pos[0] + directions[command][0], pos[1] + directions[command][1]

    if not (0 <= r < rows and 0 <= c < cols):
        continue

    element = matrix[r][c]

    if element == 'O':
        continue

    elif element == 'P':
        matrix[r][c] = '-'
        touches += 1

    moves += 1
    pos = [r, c]

print("Game over!")
print(f"Touched opponents: {touches} Moves made: {moves}")