def read_matrix_rows_cols(rows, cols):
    matrix = [input().split() for _ in range(rows)]
    return matrix


def squareMatrix(matrix, rows, cols):
    equal_block = 0

    for row in range(rows - 1):
        for col in range(cols - 1):
            symbol = matrix[row][col]
            if matrix[row][col+1] == symbol and matrix[row + 1][col] == symbol and matrix[row+1][col+1] == symbol:
                equal_block += 1
    return equal_block


rows, cols = [int(x) for x in input().split()]
matrix = read_matrix_rows_cols(rows, cols)
equal_blocks = squareMatrix(matrix, rows, cols)

print(equal_blocks)
# print("\n".join(" ".join(map(str, row)) for row in matrix))
