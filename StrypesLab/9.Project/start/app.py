import tkinter as tk
from tkinter import ttk
from collection import Collection
from add_dialog import AddDialog

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Моето приложение с табове")
        self.collections = []
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=1, fill="both")

        # Добавяне на полето за търсене и бутоните "Търсене" и "Нулиране"
        self.search_frame = tk.Frame(self)
        self.search_frame.pack(side='top', fill='x', padx=5, pady=5)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side='left', padx=5, pady=5)

        self.search_button = tk.Button(self.search_frame, text='Търсене', command=self.search)
        self.search_button.pack(side='left', padx=5, pady=5)

        self.reset_button = tk.Button(self.search_frame, text='Нулиране', command=self.reset)
        self.reset_button.pack(side='left', padx=5, pady=5)

        # Добавяне на бутон за добавяне на нов запис
        self.add_button = tk.Button(self.search_frame, text='Добавяне', command=self.add)
        self.add_button.pack(side='right', padx=5, pady=5)

    def add(self):
        AddDialog(self)

    def add_collection(self, tab_name, file_name):
        collection = Collection(tab_name, file_name, self.notebook)
        self.collections.append(collection)

    def search(self):
        query = self.search_entry.get()
        for collection in self.collections:
            collection.search(query)

    def reset(self):
        for collection in self.collections:
            collection.reset()
        self.search_entry.delete(0, 'end')

if __name__ == '__main__':
    app = App()
    app.add_collection('Movies', 'movies.txt')
    app.add_collection('Books', 'books.txt')
    app.add_collection('Games', 'games.txt')
    app.mainloop()
