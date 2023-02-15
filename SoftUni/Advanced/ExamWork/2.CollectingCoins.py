size = int(input())
field = [input().split() for _ in range(size)]

coins = []
player_pos = None

for i in range(size):
    for j in range(size):
        if field[i][j] == "P":
            player_pos = [i, j]
        elif field[i][j].isdigit():
            coins.append([i, j, int(field[i][j])])

directions = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

total_coins = 0
path = [player_pos]

while True:
    command = input().strip()
    if command not in directions:
        continue

    movement = directions[command]
    next_pos = [(player_pos[0] + movement[0]) % size, (player_pos[1] + movement[1]) % size]
    if field[next_pos[0]][next_pos[1]] == "X":
        total_coins = total_coins // 2
        print(f"Game over! You've collected {total_coins} coins.")
        break

    for coin in coins:
        if next_pos == coin[:2]:
            total_coins += coin[2]
            coins.remove(coin)
            break

    player_pos = next_pos
    path.append(player_pos)

    if total_coins >= 100:
        print(f"You won! You've collected {total_coins} coins.")
        break

print("Your path:")
for pos in path:
    print(pos)
