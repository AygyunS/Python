# Unique Usernames
n = int(input())

usernames = set()

for person in range(n):
    usernames.add(input())

(lambda: [print(x) for x in usernames])()
