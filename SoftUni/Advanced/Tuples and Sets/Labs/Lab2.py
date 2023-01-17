# Sets of Elements
length = input().split()
first_set = set([])
second_set = set([])

for n in range(int(length[0])):
    first_set.add(int(input()))
for m in range(int(length[1])):
    second_set.add(int(input()))

output = first_set & second_set
(lambda: [print(x) for x in output])()

# solution from lab
n, m = [int(x) for x in input().split()]

first_set = {int(input()) for _ in range(n)}  # !!!!
second_set = {int(input()) for _ in range(n)}  # !!!!

print(*first_set.intersection(second_set), sep="\n")


# n = int(input())
# first_set = {int(input()) for _ in range(n)}
# print(type(first_set))

# sec = [int(input()) for i in range(n)]
# print(type(sec))
