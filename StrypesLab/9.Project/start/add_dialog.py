import tkinter as tk


class AddDialog(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title('Добавяне на нов запис')
        self.geometry('400x200')
        self.transient(parent)
        self.grab_set()

        self.author_label = tk.Label(self, text='Author:')
        self.author_label.pack(pady=5)

        self.author_entry = tk.Entry(self)
        self.author_entry.pack()

        self.year_label = tk.Label(self, text='Year:')
        self.year_label.pack(pady=5)

        self.year_entry = tk.Entry(self)
        self.year_entry.pack()

        self.genre_label = tk.Label(self, text='Genre:')
        self.genre_label.pack(pady=5)

        self.genre_entry = tk.Entry(self)
        self.genre_entry.pack()

        self.rating_label = tk.Label(self, text='Rating:')
        self.rating_label.pack(pady=5)

        self.rating_entry = tk.Entry(self)
        self.rating_entry.pack()

        self.collection_label = tk.Label(self, text='Колекция:')
        self.collection_label.pack(pady=5)

        self.collection_var = tk.StringVar()
        self.collection_menu = tk.OptionMenu(self, self.collection_var, *self.parent.collections)
        self.collection_menu.pack()

        self.add_button = tk.Button(self, text='Добавяне', command=self.add)
        self.add_button.pack(side='right', padx=5, pady=5)

        self.cancel_button = tk.Button(self, text='Отказ', command=self.destroy)
        self.cancel_button.pack(side='right', padx=5, pady=5)

    def add(self):
        author = self.author_entry.get()
        year = self.year_entry.get()
        genre = self.genre_entry.get()
        rating = self.rating_entry.get()
        collection_name = self.collection_var.get()

        for collection in self.parent.collections:
            if collection.name == collection_name:
                collection.add(author, year, genre, rating)
                self.parent.update_tab(collection_name)
                break

        self.destroy()

