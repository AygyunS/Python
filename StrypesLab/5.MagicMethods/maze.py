def iterative_maze_solver(maze, start, end):
    stack = [start]

    while stack:
        current_cell = stack.pop()

        if current_cell == end:
            return True

        x, y = current_cell
        if maze[x][y] == ".":
            maze[x][y] = "visited"

            if x > 0:
                stack.append((x - 1, y))
            if x < len(maze) - 1:
                stack.append((x + 1, y))
            if y > 0:
                stack.append((x, y - 1))
            if y < len(maze[0]) - 1:
                stack.append((x, y + 1))

    return False

