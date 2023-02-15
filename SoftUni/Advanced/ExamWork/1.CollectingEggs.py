from collections import deque

eggs_size = deque(map(int, input().split(", ")))
paper_size = deque(map(int, input().split(", ")))

box = 50
result = 0

while eggs_size and paper_size:
    current_egg = eggs_size.popleft()
    current_paper = paper_size.pop()

    if current_egg <= 0:
        paper_size.append(current_paper)
    elif current_egg == 13:
        first_paper = paper_size.popleft()
        paper_size.append(first_paper)
        paper_size.appendleft(current_paper)
    else:
        if current_egg + current_paper <= box:
            result += 1
        else:
            continue

if result > 0:
    print(f"Great! You filled {result} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if paper_size:
    print(f"Pieces of paper left: {', '.join(str(el) for el in paper_size)}")
if eggs_size:
    print(f"Eggs left: {', '.join(str(el) for el in eggs_size)}")


