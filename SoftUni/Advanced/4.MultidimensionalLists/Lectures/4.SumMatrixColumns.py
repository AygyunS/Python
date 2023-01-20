def read_matrix():
    rows, cols = map(int, input().split(', '))
    current_matrix = []

    for row in range(rows):
        row_data = list(map(int, input().split()))
        current_matrix.append(row_data)

    return current_matrix


def sum_matrix_cols(matrix):

    sum_cols = []
    for i in range(len(matrix[0])):
        col_sum = 0
        for j in range(len(matrix)):
            col_sum += matrix[j][i]
        sum_cols.append(col_sum)
    return sum_cols


matrix = read_matrix()
sum_of_all = sum_matrix_cols(matrix)
print(*sum_of_all, sep='\n')


# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
