def read_matrix():
    matrix = [[int(x) for x in input().split()]
              for _ in range(int(input()))]
    return matrix


def sum_of_diagonal(matrix):
    diagonal_sum = []
    for i in range(len(matrix)):
        diagonal_sum.append(matrix[i][i])
    return diagonal_sum


def sum_of_diagonal_short(matrix):
    diagonal_sum = [matrix[i][i] for i in range(len((matrix)))]
    return diagonal_sum


matrix = read_matrix()
# diagonal_sum = sum_of_diagonal(matrix)
diagonal_sum = sum_of_diagonal_short(matrix)

print(sum(diagonal_sum))

# 3
# 11 2 4
# 4 5 6
# 10 8 -12
