def read_matrix():
    rows, cols = map(int, input().split(', '))
    current_matrix = []

    for row in range(rows):
        row_data = list(map(int, input().split(', ')))
        current_matrix.append(row_data)

    return current_matrix


matrix = read_matrix()
matrix_elements_sum = sum([sum(current_el) for current_el in matrix])


# for elem in range(len(matrix)):
#     current_row = matrix[elem]
#     matrix_elements_sum += sum(current_row)

print(matrix_elements_sum)
print(matrix)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
