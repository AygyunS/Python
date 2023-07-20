import sys
import csv

def load_stem_file(file_name):
    stem_dict = {}
    with open(file_name, newline='') as f:
        reader = csv.reader(f, delimiter=':')
        for row in reader:
            stem_dict[row[0]] = row[1]
    return stem_dict

def get_base_form(stem_dict, word):
    if word in stem_dict:
        return stem_dict[word]
    else:
        return "Word not found in stem dictionary."

if __name__ == "__main__":
    stem_file_name = sys.argv[1]
    word = sys.argv[2]
    stem_dict = load_stem_file(stem_file_name)
    base_form = get_base_form(stem_dict, word)
    print(base_form)
