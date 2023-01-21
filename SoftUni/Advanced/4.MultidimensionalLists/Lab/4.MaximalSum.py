def read_matrix_rows_cols(rows, cols):
    matrix = [[int(x) for x in input().split()] for _ in range(rows)]
    return matrix


def squareMatrixSum(matrix, rows, cols):
    inside_matrix = []
    max_sum = float("-inf")
    for row in range(rows - 2):
        for col in range(cols - 2):
            first_row = matrix[row][col:col+3]
            second_row = matrix[row+1][col:col+3]
            third_row = matrix[row+2][col:col+3]
            current_sum = sum(first_row) + sum(second_row) + sum(third_row)

            if current_sum > max_sum:
                max_sum = current_sum
                inside_matrix = [first_row, second_row, third_row]

    return inside_matrix, max_sum


rows, cols = [int(x) for x in input().split()]

matrix = read_matrix_rows_cols(rows, cols)

sum_matrix, max_sum = squareMatrixSum(matrix, rows, cols)

print(f"Sum = {max_sum}")
[print(*sum_matrix[row]) for row in range(3)]
