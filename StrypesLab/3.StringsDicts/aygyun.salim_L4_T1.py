import sys

d = {1:'a', 2:'b', 3:'c', 4:'a', 5:'d', 6:'e', 7:'a', 8:'b'}


def find_keys_by_value(dictionary, value):
    keys = [key for key in dictionary if dictionary[key] == value]
    return keys


if __name__ == '__main__':
    value = sys.argv[1]
    keys = find_keys_by_value(d, value)
    print(f'{keys}')
