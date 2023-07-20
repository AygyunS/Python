import tkinter as tk
import random
import os
import requests


def get_random_word():
    #Взимане на случайна дума от api-ninjas в случай, че не можем списък с думи
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': 'E641OSS+YLhT3YikNjav0A==LWzEkh0vC3iIfe3s'})
    if response.status_code == 200:
        data = response.json()
        return data["word"].lower()
    else:
        words = [
            'abundance', 'trampoline', 'calculator', 'satellite', 'microscope',
            'adventure', 'orangutan', 'watermelon', 'hypothesis', 'alligator',
            'chandelier', 'restaurant', 'meadow', 'pineapple', 'character',
            'umbrella', 'helicopter', 'compass', 'telephone', 'independent'
        ]
        return random.choice(words)


class Hangman:
    def __init__(self):
        self.word = get_random_word()
        self.guesses_left = 7
        self.guessed_letters = set()
        self.masked_word = self.mask_word(self.word)

    def mask_word(self, word):
        masked = [word[0]] + ['_' for _ in range(1, len(word) - 1)] + [word[-1]]
        return masked

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return False

        self.guessed_letters.add(letter)
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.masked_word[i] = letter
            return True
        else:
            self.guesses_left -= 1
            return False

    def is_solved(self):
        return '_' not in self.masked_word

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Hangman')
        self.master.geometry('400x500')
        self.master.resizable(False, False)
        self.game = Hangman()
        self.create_widgets()

    def create_widgets(self):
        self.img = tk.PhotoImage(file=os.path.join('images', f'hangman{6 - self.game.guesses_left}.png'))
        self.img_label = tk.Label(self.master, image=self.img)
        self.img_label.pack(pady=10)

        self.label = tk.Label(self.master, text=' '.join(self.game.masked_word), font=('Helvetica', 16))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master, font=('Helvetica', 16))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda event: self.submit_guess())#Добавяне на Enter клик бутон за приемане на буква

        self.message_label = tk.Label(self.master, text='', font=('Helvetica', 14), wraplength=250)
        self.message_label.pack(pady=10)

        self.submit_button = tk.Button(self.master, text='Guess', font=('Helvetica', 16), command=self.submit_guess)
        self.submit_button.pack(pady=10)

        self.new_game_button = tk.Button(self.master, text='New Game', font=('Helvetica', 16), command=self.new_game)
        self.new_game_button.pack(pady=10)

    def update_image(self):
        self.img = tk.PhotoImage(file=os.path.join('images', f'hangman{6 - self.game.guesses_left}.png'))
        self.img_label.config(image=self.img)
        self.img_label.image = self.img

    def new_game(self):
        self.game = Hangman()
        self.label.config(text=' '.join(self.game.masked_word))
        self.message_label.config(text='')
        self.entry.config(state='normal')
        self.submit_button.config(state='normal')
        self.entry.delete(0, tk.END)
        self.update_image()


    def submit_guess(self):
        letter = self.entry.get().lower()
        if len(letter) != 1 or not letter.isalpha():
            self.message_label.config(text="Please enter only one letter!")
            self.entry.delete(0, tk.END)
            return

        if letter in self.game.guessed_letters:
            self.message_label.config(text=f"You already tried '{letter}'!")
            self.entry.delete(0, tk.END)
            return

        if self.game.guess_letter(letter):
            if self.game.is_solved():
                self.label.config(text='You won! The word was ' + self.game.word)
                self.submit_button.config(state='disabled')
                self.entry.config(state='disabled')
                self.message_label.config(text='')
            else:
                self.label.config(text=' '.join(self.game.masked_word))
                self.message_label.config(text=f'Correct! {self.game.guesses_left} tries left.')
        else:
            if self.game.guesses_left == 0:
                self.label.config(text='You lost! The word was ' + self.game.word)
                self.submit_button.config(state='disabled')
                self.entry.config(state='disabled')
                self.message_label.config(text='')
            else:
                self.label.config(text=' '.join(self.game.masked_word))
                self.message_label.config(text=f'Incorrect! {self.game.guesses_left} tries left.')

        self.entry.delete(0, tk.END)
        self.update_image()

def main():
    root = tk.Tk()
    HangmanGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
