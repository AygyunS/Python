def read_text():

    try:

        file = open("text.txt", "r")
        # Getting every line on different index
        lines = [line for line in file]
        file.close()
        return lines

    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def get_even_lines(text):
    even_lines = []
    for line in range(len(text)):
        if line % 2 == 0:
            # getting only the lines at even indexes
            even_lines.append(text[line])
    return even_lines


def change_symbol(text):
    # symbols that must be changed to @
    change_symbols = {"-", ",", ".", "!", "?"}

    for line in range(len(text)):
        for char in range(len(text[line])):
            if text[line][char] in change_symbols:
                text[line] = text[line][0:char] + '@' + text[line][char+1:]


def print_result(text):
    for line in text:
        # reversing the result, without reversing the words.
        sentence = line.split()[::-1]
        # Example:
        # >>> line = 'some text'
        # >>> line[::-1] -> 'txet emos'
        # >>> line.split()[::-1] -> ['text', 'some']
        # >>> ' '.join(line) -> 'text some'
        print(' '.join(sentence))


text = read_text()
even_lines = get_even_lines(text)

if __name__ == '__main__':
    change_symbol(even_lines)
    print_result(even_lines)
