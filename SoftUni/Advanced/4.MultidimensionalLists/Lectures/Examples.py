# Here's other examples from the lecture
def sum_of_matrix(matrix):
    sum_matrix = sum(sum(row) for row in matrix)
    return sum_matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
sum_matrix = sum_of_matrix(matrix)
