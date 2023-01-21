def read_matrix():
    matrix = [[int(x) for x in input().split()]
              for _ in range(int(input()))]
    return matrix


def nums_diagonal(matrix):
    diagonal_nums = []
    for i in range(len(matrix)):
        diagonal_nums.append(matrix[i][i])
    return diagonal_nums


def num_sub_diagonal(matrix):
    diagonal_nums = []

    for i in range(len(matrix) - 1, -1, -1):  # i=2, i=1, i=0
        diagonal_nums.append(matrix[(len(matrix) - 1) - i][i])

    return diagonal_nums


matrix = read_matrix()

diagonal_nums = sum(nums_diagonal(matrix))
diagonal_sub_num = sum(num_sub_diagonal(matrix))
print(abs(diagonal_nums-diagonal_sub_num))
