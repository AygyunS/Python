import tkinter as tk
from tkinter import ttk


class Item:
    def __init__(self, title, author, year, genre, rating):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.rating = rating


class Collection:
    def __init__(self, collection_name, file_name):
        self.collection_name = collection_name
        self.items_list = []
        self.load_items(file_name)

    def load_items(self, file_name):
        try:
            with open(file_name, "r") as f:
                for line in f:
                    item_data = line.strip().split(",")
                    item = Item(item_data[0], item_data[1], item_data[2], item_data[3], item_data[4])
                    self.items_list.append(item)
            print(f"{len(self.items_list)} {self.collection_name} loaded from {file_name}")
        except FileNotFoundError:
            print(f"File {file_name} not found.")

    def add_item(self, item):
        self.items_list.append(item)

    def delete_item(self, item):
        self.items_list.remove(item)

    def update_item(self, item, new_title, new_author, new_year, new_genre, new_rating):
        item.title = new_title
        item.author = new_author
        item.year = new_year
        item.genre = new_genre
        item.rating = new_rating

    def search_items(self, keyword):
        results = []
        for item in self.items_list:
            if keyword in item.title or keyword in item.author:
                results.append(item)
        return results


class GUI(Collection):
    def __init__(self, collections):
        self.collections = collections
        self.root = tk.Tk()
        self.root.title("Collection Manager")

        search_frame = ttk.Frame(self.root)
        search_frame.pack(side=tk.TOP, fill=tk.X)

        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, padx=5, pady=5)

        search_button = ttk.Button(search_frame, text="Search", command=self.search_items)
        search_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(expand=1, fill="both")

        for collection in self.collections:
            tab = ttk.Frame(self.tab_control)
            self.tab_control.add(tab, text=collection.collection_name)

            columns = ("No", "Title", "Author", "Year", "Genre", "Rating")
            treeview = ttk.Treeview(tab, columns=columns, show="headings")
            treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            for col in columns:
                treeview.heading(col, text=col)

            for i, item in enumerate(collection.items_list):
                treeview.insert("", "end", values=(i + 1, item.title, item.author, item.year, item.genre, item.rating))

            button_frame = ttk.Frame(tab)
            button_frame.pack(side=tk.LEFT, fill=tk.Y)

            add_button = ttk.Button(button_frame, text="Add", command=lambda: self.add_item(collection, treeview))
            add_button.pack(pady=5)

            edit_button = ttk.Button(button_frame, text="Edit", command=lambda: self.edit_item(collection, treeview))
            edit_button.pack(pady=5)

            delete_button = ttk.Button(button_frame, text="Delete",
                                       command=lambda: self.delete_item(collection, treeview))
            delete_button.pack(pady=5)

        def search_items(self):
            keyword = self.search_var.get()
            for tab in self.tab_control.tabs():
                tab_treeview = self.tab_control.nametowidget(tab).children["!treeview"]
                items = tab_treeview.get_children()
                for item in items:
                    values = tab_treeview.item(item, "values")
                    if keyword.lower() in values[1].lower() or keyword.lower() in values[2].lower():
                        tab_treeview.selection_set(item)


        self.root.mainloop()

collections = []
collections.append(Collection("Movies", "db/movies.txt"))
collections.append(Collection("Books", "db/books.txt"))
collections.append(Collection("Games", "db/games.txt"))

print(collections[0].items_list[0].title)
gui = GUI(collections)

