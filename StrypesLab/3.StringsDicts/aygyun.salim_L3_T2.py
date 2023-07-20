import sys

def vigenere_cipher(plaintext, key):
    key_len = len(key)
    key_shifts = [ord(char.lower()) - ord('a') for char in key]
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_shift = key_shifts[i % key_len]
            shifted = ord(char) + key_shift
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            ciphertext += chr(shifted)
        else:
            ciphertext += char
    return ciphertext

if __name__ == "__main__":
    plaintext = sys.argv[1]
    key = sys.argv[2]
    ciphertext = vigenere_cipher(plaintext, key)
    print(ciphertext)
