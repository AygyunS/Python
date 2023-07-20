def recursive_maze_solver(maze, start, end):
    x, y = start

    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
        return False

    if maze[x][y] == "#":
        return False

    if maze[x][y] == "visited":
        return False

    if start == end:
        return True

    maze[x][y] = "visited"


    if (recursive_maze_solver(maze, (x - 1, y), end) or
        recursive_maze_solver(maze, (x + 1, y), end) or
        recursive_maze_solver(maze, (x, y - 1), end) or
        recursive_maze_solver(maze, (x, y + 1), end)):
        return True

    return False
