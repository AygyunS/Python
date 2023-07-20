import sys

lst = [int(x) for x in sys.argv[1:]]

counts = {}
for x in lst:
    if x in counts:
        print("True")
        break
    counts[x] = 1
else:
    print("False")

