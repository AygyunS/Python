def create_matrix(size):
    matrix = []
    for _ in range(size):
        data = input().split(' ')
        matrix.append(data)

    return matrix

matrix = create_matrix(6)
commands = input().split(', ')
rover_position = [0, 0]

for pos in range(len(matrix)):
    if 'E' in matrix[pos]:
        rover_position = [pos, matrix[pos].index('E')]
        break

suitable = {"Water": 0, "Metal": 0, "Concrete": 0}

for command in commands:
    if command == 'left':
        rover_position[1] -= 1
        if rover_position[1] < 0:
            rover_position[1] = 5
    elif command == 'right':
        rover_position[1] += 1
        if rover_position[1] > 5:
            rover_position[1] = 0
    elif command == 'up':
        rover_position[0] -= 1
        if rover_position[0] < 0:
            rover_position[0] = 5
    elif command == 'down':
        rover_position[0] += 1
        if rover_position[0] > 5:
            rover_position[0] = 0
    if matrix[rover_position[0]][rover_position[1]] == 'W':
        print(f'Water deposit found at ({rover_position[0]}, {rover_position[1]})')
        suitable['Water'] += 1

    if matrix[rover_position[0]][rover_position[1]] == 'M':
        print(f'Metal deposit found at ({rover_position[0]}, {rover_position[1]})')
        suitable['Metal'] += 1
    if matrix[rover_position[0]][rover_position[1]] == 'C':
        print(f'Concrete deposit found at ({rover_position[0]}, {rover_position[1]})')
        suitable['Concrete'] += 1
    if matrix[rover_position[0]][rover_position[1]] == 'R':
        print(f'Rover got broken at ({rover_position[0]}, {rover_position[1]})')
        break


if all(value > 0 for value in suitable.values()):
    print(f'Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')






