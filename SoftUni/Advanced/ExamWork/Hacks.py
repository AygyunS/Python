# Read the input matrix
matrix = []
for i in range(6):
    matrix.append(input().split())

# OR below def
def create_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append(input().split(' '))

    return matrix

