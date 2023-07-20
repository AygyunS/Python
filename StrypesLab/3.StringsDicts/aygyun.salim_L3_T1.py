import sys

def caesar_cipher(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return plaintext.translate(table)


if __name__ == "__main__":
    plaintext = sys.argv[1]
    key = int(sys.argv[2])
    ciphertext = caesar_cipher(plaintext, key)
    print(ciphertext)
