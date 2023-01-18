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

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)


# lab solution

occurrences = {}

for letter in input():
    occurrences[letter] = occurrences.get(letter, 0) + 1

for letter, times in sorted(occurrences.items()):
    print(f"{letter}: {occurrences[letter]} times/s")
