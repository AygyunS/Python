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
    i=len(matrix)
    for i in range(i, -1, -1):
        diagonal_nums.append(matrix[i][i])
    return diagonal_nums

matrix = read_matrix()

diagonal_nums = nums_diagonal(matrix)
diagonal_sub_num = num_sub_diagonal(matrix)

print(f"Primary diagonal: {', '.join(map(str,diagonal_nums))}. Sum: {sum(diagonal_nums)}")
print(f"Primary diagonal: {', '.join(map(str,diagonal_nums))}. Sum: {sum(diagonal_nums)}")
