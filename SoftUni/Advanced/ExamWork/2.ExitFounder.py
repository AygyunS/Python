def create_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append(input().split(' '))

    return matrix

players = input().split(', ')
matrix = create_matrix(6)

while True:
    command = input().strip("()").split(', ')
    print(command)
