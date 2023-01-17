import sys
meal = int(input())

lst = [int(x) for x in input().split()]
maxEl = max(lst)

sum = 0

for n in lst.copy():
    sum += n
    if sum <= meal:
        lst.remove(n)
    else:
        print(maxEl)
        print("Orders left:", *lst)
        sys.exit()
print(maxEl)
print("Orders complete")
