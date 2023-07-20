import re


def extract_words(text):
    return re.findall(r'\b\w+\b', text)


def extract_sentences(text):
    return re.findall(r'([^.!?]+[.!?])', text)


def extract_bigrams(text):
    words = extract_words(text)
    return [words[i:i+2] for i in range(len(words)-1)]

with open('input_file2.txt', 'r') as f_in:
    text = f_in.read()

    # Words
    words = extract_words(text)
    with open('words_file.txt', 'w') as f_words:
        f_words.write('\n'.join(words))

    f_words.close()

    # Sentences
    sentences = extract_sentences(text)
    with open('sentences_file.txt', 'w') as f_sentences:
        f_sentences.write('\n'.join(sentences))
    # Close sentences file
    f_sentences.close()

    # all bigrams
    bigrams = extract_bigrams(text)
    with open('bigrams_file.txt', 'w') as f_bigrams:
        for bigram in bigrams:
            f_bigrams.write(' '.join(bigram) + '\n')

    f_bigrams.close()
