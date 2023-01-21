def read_matrix():
    matrix = [[int(x) for x in input().split()]
              for _ in range(int(input(", ")))]
    return matrix

def nums_diagonal(matrix):
    diagonal_nums = []
    for i in range(len(matrix)):
        diagonal_nums.append(matrix[i][i])
    return diagonal_sum

def sum_of_diagonal_short(matrix):
    diagonal_sum = [matrix[i][i] for i in range(len((matrix)))]
    return diagonal_sum


matrix = read_matrix()

diagonal_nums = nums_diagonal(matrix)


print(f"Primary diagonal: {(*sum_of_all)}. Sum: {sum(diagonal_nums)}"))