import sys

lst = [int(x) for x in sys.argv[1:]]

is_sorted = True
for i in range(1, len(lst)):
    if lst[i] < lst[i-1]:
        is_sorted = False
        break

if is_sorted:
    print("sorted")
else:
    print("unsorted")

