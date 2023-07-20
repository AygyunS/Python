import tkinter as tk
from tkinter import ttk


def create_tab_from_file(notebook, tab_name, file_name):
    # Създаване на нов таб
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_name)

    # Създаване на Treeview
    tree = ttk.Treeview(tab, columns=('Author', 'Year', 'Genre', 'Rating'))
    tree.heading('#0', text='Title')
    tree.heading('Author', text='Author')
    tree.heading('Year', text='Year')
    tree.heading('Genre', text='Genre')
    tree.heading('Rating', text='Rating')

    # Четене на данните от файл и добавяне към Treeview
    with open(file_name, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            title = data[0]
            author = data[1]
            year = data[2]
            genre = data[3]
            rating = data[4]
            tree.insert('', 'end', text=title, values=(author, year, genre, rating))

    # Показване на Treeview
    tree.pack(fill='both', expand=True)


# Създаване на основен прозорец на приложението
root = tk.Tk()
root.title("Моето приложение с табове")

# Създаване на обект Notebook
notebook = ttk.Notebook(root)

# Създаване на таб за файлът movies.txt
create_tab_from_file(notebook, 'Movies', 'movies.txt')

# Създаване на таб за файлът books.txt
create_tab_from_file(notebook, 'Books', 'books.txt')

# Създаване на таб за файлът games.txt
create_tab_from_file(notebook, 'Games', 'games.txt')

# Показване на табовете
notebook.pack(expand=1, fill="both")

# Стартиране на приложението
root.mainloop()
