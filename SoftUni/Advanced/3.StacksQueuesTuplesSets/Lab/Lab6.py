# Paint Colors
from collections import deque

main_colors = ['red', 'yellow', 'blue']
sub_colors = ['orange', 'purple', 'green']

text = deque(input().split())

colors_que = deque()
while text:
    if len(text) > 1:
        first, second = text.popleft(), text.pop()
        straight, reverse = first + second, second + first
        if straight in main_colors or straight in sub_colors:
            colors_que.append(straight)
        elif reverse in main_colors or reverse in sub_colors:
            colors_que.append(reverse)
        else:
            edited_first, edited_second = first[:-1], second[:-1]
            middle = len(text) // 2
            if edited_first:
                text.insert(middle, edited_first)
            if edited_second:
                text.insert(middle, edited_second)
    else:
        substring = text.popleft()
        if substring in main_colors or substring in sub_colors:
            colors_que.append(substring)

for i in range(len(colors_que)):
    color = colors_que.popleft()
    if color == 'orange':
        if ('red' and 'yellow') in colors_que:
            colors_que.append(color)
    elif color == 'purple':
        if ('red' and 'blue') in colors_que:
            colors_que.append(color)
    elif color == 'green':
        if ('blue' and 'yellow') in colors_que:
            colors_que.append(color)
    else:
        colors_que.append(color)

print(list(colors_que))
