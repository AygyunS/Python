# lst = input().split('|')
# clean_list = [" ".join(string.split()) for string in lst]
# print(*clean_list[::-1])

nums = [string.split() for string in input().split('|')]
print(*[' '.join(string) for string in nums[::-1] if string])

def flatten_list():
    input_string = input()
    list_of_strings = input_string.split('|')

    list_of_strings = [list(map(int, string.split())) for string in list_of_strings if string.strip()]

    list_of_strings = list_of_strings[::-1]

    flatten_list = list(reversed([item for sublist in list_of_strings for item in sublist]))
    flatten_list = flatten_list[::-1]
    return flatten_list

output = flatten_list()
print(" ".join(map(str,output)))