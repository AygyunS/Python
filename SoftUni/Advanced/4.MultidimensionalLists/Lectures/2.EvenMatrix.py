def read_matrix():
    n = int(input())
    matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

    return matrix


def even_nums_matrix(matrix):
    for i in range(len(matrix)):
        matrix[i] = [x for x in matrix[i] if x % 2 == 0]
    return matrix


matrix = read_matrix()
even_matrix = even_nums_matrix(matrix)
print(even_matrix)
# print(sum_matrix)
# 2
# 1, 2, 3
# 4, 5, 6
# (Examples.py) We have 1 more function sum_of_matrix it's not in the workout but wanted to test the code from previous program
