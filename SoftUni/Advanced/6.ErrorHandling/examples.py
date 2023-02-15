def main():
    n = int(input())
    battlefield = []
    for i in range(n):
        row = input()
        battlefield.append(list(row))

    r, c = 0, 0
    hits = 0
    cruisers = 3
    for i in range(n):
        for j in range(n):
            if battlefield[i][j] == 'S':
                r, c = i, j
                break

    while True:
        if cruisers == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

        if hits >= 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r + 1}, {c + 1}]!")
            break

        direction = input()
        if direction == 'up':
            r = r - 1 if r - 1 >= 0 else r
        elif direction == 'down':
            r = r + 1 if r + 1 < n else r
        elif direction == 'left':
            c = c - 1 if c - 1 >= 0 else c
        elif direction == 'right':
            c = c + 1 if c + 1 < n else c

        if battlefield[r][c] == '*':
            hits += 1
            battlefield[r][c] = '-'
        elif battlefield[r][c] == 'C':
            cruisers -= 1
            battlefield[r][c] = '-'

    for i in range(n):
        print(*battlefield[i])

if __name__ == '__main__':
    main()
