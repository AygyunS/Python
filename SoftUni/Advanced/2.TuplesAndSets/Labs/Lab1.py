# Unique Usernames
n = int(input())

usernames = set()

for person in range(n):
    usernames.add(input())

(lambda: [print(x) for x in usernames])()

# for per in usernames:
#     print(per)

# From the Lab 1 line solution
print(*{input() for _ in range(int(input()))}, sep="\n")
