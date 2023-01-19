length = input().split()
first_set = set([])
second_set = set([])

for n in range(int(length[0])):
    first_set.add(int(input()))
for m in range(int(length[1])):
    second_set.add(int(input()))

output = first_set & second_set
(lambda: [print(x) for x in output])()
