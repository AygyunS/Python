text = input()

char_counts = {}


for char in text:
    if char not in char_counts:
        char_counts[char] = 1
    else:
        char_counts[char] += 1

sorted_keys = sorted(char_counts.keys())

for char in sorted_keys:
    print(f"{char}: {char_counts[char]} time/s")
