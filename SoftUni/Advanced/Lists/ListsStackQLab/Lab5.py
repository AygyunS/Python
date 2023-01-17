# Hot potato
kids = input().strip().split()

n = int(input())

i = 0

while len(kids) > 1:

    i = (i + n - 1) % len(kids)
    removed_kid = kids.pop(i)
    print(f"Removed {removed_kid}")


print(f"Last is {kids[0]}")
