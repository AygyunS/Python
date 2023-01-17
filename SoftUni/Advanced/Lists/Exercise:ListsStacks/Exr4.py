import queue

q = queue.deque()
user_input = input()

capacity = int(input())
sum = 0
count = 1
for i in user_input.split():
    q.append(int(i))

while len(q) > 0:
    sum+=q[-1]
    if sum <= capacity:
        q.pop()
    else:
        count+=1
        sum=0

print(count)