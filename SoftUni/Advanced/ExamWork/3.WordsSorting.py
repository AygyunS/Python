def words_sorting(*args):
    words = {}

    for word in args:
        letters_sum = 0
        word_from_list = word
        for char in word:
            letters_sum += ord(char)
        words[word_from_list] = letters_sum

    sum_of_values = sum(value for value in words.values())
    if sum_of_values % 2 == 0:
        sorted_words = {k: v for k, v in sorted(words.items(), key=lambda x: (x[0], x[1]))}
    else:
        sorted_words = {k: v for k, v in sorted(words.items(), key=lambda x: (-x[1], x[0]))}

    result = []
    for word, num in sorted_words.items():
        result.append(f"{word} - {num}")

    return '\n'.join(result)



#
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#   ))