def read_matrix():
    rows, cols = map(int, input().split(', '))
    current_matrix = []

    for row in range(rows):
        row_data = list(map(int, input().split()))
        current_matrix.append(row_data)

    return current_matrix


# def get_sum_of_left_half(matrix):
#     sum_of_elements = 0
#     matrix_size = len(matrix)
#     for row in range(matrix_size):
#         for column in range(row + 1):
#             sum_of_elements += matrix[row][column]

#     return sum_of_elements


# def get_sum_of_right_half(matrix):
#     sum_of_elements = 0
#     matrix_size = len(matrix)
#     for row in range(matrix_size):
#         for column in range(row, matrix_size):
#             sum_of_elements += matrix[row][column]

#     return sum_of_elements


matrix = read_matrix()

print((matrix))
