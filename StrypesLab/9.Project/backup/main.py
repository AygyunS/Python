import tkinter as tk
from tkinter import ttk
import json


class Item:
    def __init__(self, data):
        self.data = data

    def __getattr__(self, name):
        try:
            return self.data[name]
        except KeyError:
            raise AttributeError(f"Item has no attribute {name}")


class Collection:
    def __init__(self, collection_name, file_name):
        self.collection_name = collection_name
        self.items_list = []
        self.load_items(file_name)

    def load_items(self, file_name):
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
                for item_data in data["items"]:
                    item = Item(item_data)
                    self.items_list.append(item)
            print(f"{len(self.items_list)} {self.collection_name} loaded from {file_name}")
        except FileNotFoundError:
            print(f"File {file_name} not found.")


collections = []
collections.append(Collection("Movies", "db/movies.json"))
collections.append(Collection("Books", "db/books.json"))
collections.append(Collection("Games", "db/games.json"))


#I want to create TKinter window with tabs for each collection and listbox with items from each collection

class App:
    def __init__(self, collections):
        self.collections = collections
        self.root = tk.Tk()
        self.root.title("Collection Manager")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill='both')

        self.frames = []

        for collection in self.collections:
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=collection.collection_name)
            self.frames.append(frame)

            treeview = ttk.Treeview(frame)
            treeview.pack(side="left", fill="both", expand=True)

            vsb = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
            vsb.pack(side="right", fill="y")
            treeview.configure(yscrollcommand=vsb.set)

            headings = list(collection.items_list[0].data.keys())

            treeview["columns"] = headings
            for h in headings:
                treeview.heading(h, text=h, anchor="w")
                treeview.column(h, anchor="w")

            for i, item in enumerate(collection.items_list):
                values = list(item.data.values())
                treeview.insert("", "end", text=i+1, values=values)



        #Add button
        add_button = ttk.Button(frame, text="Add record", command=self.add_record)
        add_button.pack()

    # I want to add button to add new item to the listbox
    def add_record(self):
        collection = self.collections[self.notebook.index(self.notebook.select())]
        item_data = {}  # dictionary to store new item data
        for key in collection.items_list[0].data.keys():  # prompt for values for each key
            item_data[key] = input(f"Enter {key}: ")
        item = Item(item_data)  # create a new item
        collection.items_list.append(item)  # add it to the collection
        treeview = self.frames[self.notebook.index(self.notebook.select())].children[
            '!treeview']  # get the Treeview widget for the current tab
        values = list(item.data.values())
        treeview.insert("", "end", text=len(collection.items_list),
                        values=values)  # add a new row to the Treeview widget


app = App(collections)
app.root.mainloop()





