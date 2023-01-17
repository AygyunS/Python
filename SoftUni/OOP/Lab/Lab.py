# get the size of the rhombus from the user
n = int(input())

# create a list of spaces and asterisks for the top half of the rhombus
top_half = []
for i in range(n):
    # calculate the number of spaces and asterisks for this row
    spaces = n - i - 1
    asterisks = i + 1

    # create the row as a string
    row = " " * spaces + "* " * asterisks + " " * spaces
    top_half.append(row)

# print the top half of the rhombus
for row in top_half:
    print(row)

# print the bottom half of the rhombus by reversing the list and printing each row
top_half.pop(-1)
for row in reversed(top_half):
    print(row)
