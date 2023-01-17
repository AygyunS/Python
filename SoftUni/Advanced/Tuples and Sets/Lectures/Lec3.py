# Record Unique Names
n = int(input())

uni_names = set()

for name in range(n):
    uni_names.add(input())

for person in uni_names:
    print(person)
