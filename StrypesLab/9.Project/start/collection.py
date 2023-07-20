from tkinter import ttk
from treeview import TreeView


class Collection:
    def __init__(self, tab_name, file_name, notebook):
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text=tab_name)
        self.tree = TreeView(self.tab)
        self.data = []
        self.read_data(file_name)
        self.tree.pack(fill='both', expand=True)

    def read_data(self, file_name):
        with open(file_name, 'r') as f:
            for line in f:
                data = line.strip().split(',')
                title = data[0]
                author = data[1]
                year = data[2]
                genre = data[3]
                rating = data[4]
                self.data.append((title, author, year, genre, rating))
                self.tree.insert('', 'end', text=title, values=(author, year, genre, rating))

    def search(self, query):
        self.tree.delete(*self.tree.get_children())
        for item in self.data:
            if query.lower() in ' '.join(item).lower():
                self.tree.insert('', 'end', text=item[0], values=item[1:])

    def reset(self):
        self.tree.delete(*self.tree.get_children())
        for item in self.data:
            self.tree.insert('', 'end', text=item[0], values=item[1:])
