import sys

lst = [int(x) for x in sys.argv[1:]]

new_lst = []
seen = {}
for x in lst:
    if x not in seen:
        new_lst.append(x)
        seen[x] = True
print(new_lst)


