def read_matrix_rows_cols(rows, cols):
    matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
    return matrix


def squareMatrixSum(matrix, rows, cols):
    inside_matrix = []
    max_sum = float("-inf")
    for row in range(rows - 1):
        for col in range(cols - 1):
            first_row = matrix[row][col:col+2]
            second_row = matrix[row+1][col:col+2]
            current_sum = sum(first_row) + sum(second_row)

            if current_sum > max_sum:
                max_sum = current_sum
                inside_matrix = [first_row, second_row]

    return inside_matrix, max_sum


rows, cols = [int(x) for x in input().split(", ")]

matrix = read_matrix_rows_cols(rows, cols)

sum_matrix, max_sum = squareMatrixSum(matrix, rows, cols)

[print(*sum_matrix[row]) for row in range(2)]

print(max_sum)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
