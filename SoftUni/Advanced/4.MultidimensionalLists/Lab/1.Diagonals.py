def read_matrix():
    matrix = [[int(x) for x in input().split(", ")]
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


def primary_diagonal_short(matrix):
    primary = [matrix[r][r] for r in range(len(matrix))]
    return primary


def second_diagonal_short(matrix):
    secondary = [matrix[(len(matrix) - 1) - r][r]
                 for r in range(len(matrix)-1, -1, -1)]
    return secondary


matrix = read_matrix()

# diagonal_nums = nums_diagonal(matrix)
# diagonal_sub_num = num_sub_diagonal(matrix)

diagonal_nums = primary_diagonal_short(matrix)
diagonal_sub_num = second_diagonal_short(matrix)

# print(
#     f"Primary diagonal: {', '.join(map(str,diagonal_nums))}. Sum: {sum(diagonal_nums)}")

print(
    f"Primary diagonal: {', '.join(str(x) for x in diagonal_nums)}. Sum: {sum(diagonal_nums)}")

# print(
#     f"Secondary diagonal: {', '.join(map(str,diagonal_sub_num))}. Sum: {sum(diagonal_sub_num)}")

print(
    f"Secondary diagonal: {', '.join(str(x) for x in diagonal_sub_num)}. Sum: {sum(diagonal_sub_num)}")
