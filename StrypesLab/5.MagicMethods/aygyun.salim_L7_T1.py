import sys

maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'g', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]


def solveMaze(x, y):
    stack = [(x, y)]
    visited = set()
    visited.add((x, y))

    while stack:
        x, y = stack[-1]
        if maze[x][y] == 'g':
            return True
        found = False
        for x_offset, y_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x_next, y_next = x + x_offset, y + y_offset
            if (x_next, y_next) not in visited and maze[x_next][y_next] in ' g':
                stack.append((x_next, y_next))
                visited.add((x_next, y_next))
                found = True
                break
        if not found:
            maze[x][y] = 'x'
            stack.pop()
    return False


def printMaze():
    for row in maze:
        print(' '.join(row))


if len(sys.argv) < 3:
    sys.exit(1)

start_x, start_y = int(sys.argv[1]), int(sys.argv[2])
maze[start_x][start_y] = ' '
if not solveMaze(start_x, start_y):
    print('No solution found.')
else:
    printMaze()
