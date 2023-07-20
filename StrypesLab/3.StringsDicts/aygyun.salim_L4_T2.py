import sys

if __name__ == '__main__':
    text = sys.argv[1]
    histogram = [(char, text.lower().count(char)) for char in set(filter(str.isalpha, text.lower()))]
    histogram.sort(key=lambda x: x[1])
    print(histogram)
