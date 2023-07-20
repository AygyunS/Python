import tkinter as tk
from tkinter import messagebox
from collection import Collection
from item import Item
import os

class CollectionManager:
    def __init__(self, master):
        self.master = master
        master.title("Collection Manager")

        self.collection = Collection("Movies", "movies.txt")
        self.current_collection = self.collection

        self.create_widgets()

        self.switch_collection("Movies")

    def load_collections(self):
        self.collections["Movies"] = Collection("Movies", "movies.txt")
        self.collections["Books"] = Collection("Books", "books.txt")

    def create_widgets(self):
        self.label = tk.Label(self.master, text=f"{self.collection.name} Collection")
        self.label.pack()

        # Add an option menu to switch between collections
        collection_files = [f for f in os.listdir('../start') if os.path.isfile(f) and f.endswith('.txt')]
        self.collections = {}
        for file in collection_files:
            name = os.path.splitext(file)[0]
            collection = Collection(name, file)
            self.collections[name] = collection
        self.collection_menu = tk.OptionMenu(self.master, tk.StringVar(value="Movies"), *self.collections.keys(),
                                             command=self.switch_collection)
        self.collection_menu.pack()

        self.listbox = tk.Listbox(self.master)
        for item in self.collection.items:
            self.listbox.insert(tk.END, item.title)
        self.listbox.pack()

        self.add_button = tk.Button(self.master, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.remove_button = tk.Button(self.master, text="Remove Item", command=self.remove_item)
        self.remove_button.pack()

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack()

        self.collection_label = tk.Label(self.master, text=f"Current Collection: {self.current_collection.name}")
        self.collection_label.pack()

    def switch_collection(self, filename):
        self.current_collection.save_to_file(self.current_collection.file)
        self.current_collection = self.collections[os.path.splitext(filename)[0]]
        self.listbox.delete(0, tk.END)
        for item in self.current_collection.items:
            self.listbox.insert(tk.END, item.title)
        self.collection_label.config(text=f"Current Collection: {self.current_collection.name}")

    def add_item(self):
        top = tk.Toplevel(self.master)

        tk.Label(top, text="Title").grid(row=0, column=0)
        tk.Label(top, text="Author").grid(row=1, column=0)
        tk.Label(top, text="Year").grid(row=2, column=0)
        tk.Label(top, text="Genre").grid(row=3, column=0)
        tk.Label(top, text="Rating").grid(row=4, column=0)

        title_entry = tk.Entry(top)
        author_entry = tk.Entry(top)
        year_entry = tk.Entry(top)
        genre_entry = tk.Entry(top)
        rating_entry = tk.Entry(top)

        title_entry.grid(row=0, column=1)
        author_entry.grid(row=1, column=1)
        year_entry.grid(row=2, column=1)
        genre_entry.grid(row=3, column=1)
        rating_entry.grid(row=4, column=1)

        submit_button = tk.Button(top, text="Add",
                                  command=lambda: self.submit_item(top, title_entry.get(), author_entry.get(),
                                                                   year_entry.get(), genre_entry.get(),
                                                                   rating_entry.get()))
        submit_button.grid(row=5, column=1)

    def submit_item(self, top, title, author, year, genre, rating):
        if title and author and year and genre and rating:
            try:
                year = int(year)
                rating = float(rating)
                item = Item(title, author, year, genre, rating)
                self.current_collection.items.append(item)
                self.listbox.insert(tk.END, title)
                self.current_collection.save_to_file()
                top.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Year must be an integer and rating must be a float.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def remove_item(self):
        selection = self.listbox.curselection()
        if len(selection) > 0:
            index = selection[0]
            title = self.listbox.get(index)
            for item in self.current_collection.items:
                if item.title == title:
                    self.current_collection.items.remove(item)
                    self.listbox.delete(index)
                    self.current_collection.save_to_file()
                    break

        else:
            messagebox.showerror("Error", "Please select an item to remove.")

    def mainloop(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    manager = CollectionManager(root)
    root.protocol("WM_DELETE_WINDOW", manager.save_collection)
    manager.mainloop()
