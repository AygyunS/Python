from collections import deque

players = deque(input().split(", "))
size = 6
maze = [input().split() for row in range(size)]
winner = ""
player_to_be_ignored = []
while True:
    coordinates = input().lstrip("(").rstrip(")").split(", ")
    row, column = [int(i) for i in coordinates]

    if players[0] in player_to_be_ignored:
        player_to_be_ignored.remove(players[0])
        players.append(players.popleft())
        continue

    if maze[row][column] == "E":
        winner = players[0]
        print(f"{winner} found the Exit and wins the game!")
        break

    elif maze[row][column] == "T":
        winner = players[1]
        looser = players[0]
        print(f"{looser} is out of the game! The winner is {winner}.")
        break

    elif maze[row][column] == "W":
        player_to_be_ignored.append(players[0])
        print(f"{players[0]} hits a wall and needs to rest.")

    players.append(players.popleft())

