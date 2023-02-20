companies = {'Sony': 120, 'Apple': 150, 'Samsung': 105, 'Hp': 132, 'Acer': 125}

# sorted by value
sorted_companies_data = sorted(companies.items(), key=lambda x: x[1])

# sorted by key
sorted_companies_data = sorted(companies.items(), key=lambda x: x[0])

# sorted first by value then by key
companies = {'Sony': 120, 'Apple': 150, 'Samsung': 105, 'Hp': 132, 'Acer': 125, 'Acea': 125}
companies_data = sorted(companies.items(), key=lambda x: (x[1], x[0]))
print(companies_data)


#matrix - board type
size = 7
board = [input().split() for row in range(size)]

def is_outside(row, column, rows, columns):
    return row < 0 or column < 0 or row >= rows or column >= columns