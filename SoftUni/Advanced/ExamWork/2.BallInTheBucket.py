
def create_matrix(size):
    matrix = []
    for _ in range(size):
        data = input().split(' ')
        matrix.append(data)

    return matrix

def get_coordinates():
    coordinates = []
    for _ in range(3):
        line = input().strip()
        x, y = map(int, line.strip('()').split(','))
        coordinates.append((x, y))

    return coordinates

def get_sum_of_column(matrix, column):
    total = 0
    for row in matrix:
        total += int(row[column])

    return total

matrix = create_matrix(6)
points = 0

coordinates = get_coordinates()

for i in coordinates:
    if i[0] > len(matrix) or i[1] > len(matrix):
        continue
    if matrix[i[0]][i[1]] == "B":
        matrix[i[0]][i[1]] = 0
        points += get_sum_of_column(matrix, i[1])



if points < 100:
    print(f"Sorry! You need {100-points} points more to win a prize.")
else:
    if 100 <= points < 200:
        print(f"Good job! You scored {points} points, and you've won Football.")
    elif 200 <= points < 300:
        print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
    elif 300 <= points < 400:
        print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")




