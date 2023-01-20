def read_matrix():
    matrix = [[int(x) for x in input().split(", ")]
              for _ in range(int(input()))]

    return matrix


def flatten_matrix(matrix):
    new_matrix = []
    for row in matrix:
        for num in row:
            new_matrix.append(num)
    return new_matrix


def flatten_matrix_short(matrix):
    result = [num for row in matrix for num in row]
    return result


matrix = read_matrix()
# print(flatten_matrix(matrix))
print(flatten_matrix_short(matrix))
