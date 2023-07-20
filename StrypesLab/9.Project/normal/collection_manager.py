import tkinter as tk
from tkinter import ttk, messagebox


class CollectionManager:

    def __init__(self, master):
        self.master = master
        self.master.title("Collection Manager")

        self.collection = []
        self.load_collection()

        self.create_widgets()

    def create_widgets(self):
        # create main frame for displaying collections
        self.main_frame = tk.Frame(self.master, padx=10, pady=10)
        self.main_frame.pack()

        # create label for collection
        self.collection_label = tk.Label(self.main_frame, text="Collection:")
        self.collection_label.pack()

        # create treeview for displaying collection items
        self.collection_treeview = ttk.Treeview(self.main_frame)
        self.collection_treeview["columns"] = ("Author", "Year", "Genre", "Rating")
        self.collection_treeview.heading("#0", text="Title")
        self.collection_treeview.heading("Author", text="Author")
        self.collection_treeview.heading("Year", text="Year")
        self.collection_treeview.heading("Genre", text="Genre")
        self.collection_treeview.heading("Rating", text="Rating")
        for item in self.collection:
            self.collection_treeview.insert("", tk.END, text=item[0], values=item[1:])
        self.collection_treeview.pack()

        # create frame for adding new item
        self.add_frame = tk.Frame(self.master, padx=10, pady=10)
        self.add_frame.pack()

        # create labels and entry widgets for new item
        self.title_label = tk.Label(self.add_frame, text="Title:")
        self.title_label.grid(row=0, column=0, sticky=tk.W)
        self.title_entry = tk.Entry(self.add_frame)
        self.title_entry.grid(row=0, column=1)

        self.author_label = tk.Label(self.add_frame, text="Author:")
        self.author_label.grid(row=1, column=0, sticky=tk.W)
        self.author_entry = tk.Entry(self.add_frame)
        self.author_entry.grid(row=1, column=1)

        self.year_label = tk.Label(self.add_frame, text="Year:")
        self.year_label.grid(row=2, column=0, sticky=tk.W)
        self.year_entry = tk.Entry(self.add_frame)
        self.year_entry.grid(row=2, column=1)

        self.genre_label = tk.Label(self.add_frame, text="Genre:")
        self.genre_label.grid(row=3, column=0, sticky=tk.W)
        self.genre_entry = tk.Entry(self.add_frame)
        self.genre_entry.grid(row=3, column=1)

        self.rating_label = tk.Label(self.add_frame, text="Rating:")
        self.rating_label.grid(row=4, column=0, sticky=tk.W)
        self.rating_entry = tk.Entry(self.add_frame)
        self.rating_entry.grid(row=4, column=1)

        self.add_item_button = tk.Button(self.add_frame, text="Add Item", command=self.add_item)
        self.add_item_button.grid(row=5, column=1, sticky=tk.E)

        # create frame for actions
        self.action_frame = tk.Frame(self.master, padx=10, pady=10)
        self.action_frame.pack()

        # create buttons for actions
        self.add_button = tk.Button(self.action_frame, text="Add", command=self.show_add_item)
        self.add_button.pack(side=tk.LEFT)

        self.edit_button = tk.Button(self.action_frame, text="Edit", command=self.edit_item)
        self.edit_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.action_frame, text="Delete", command=self.delete_item)
        self.delete_button.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.action_frame, text="Search", command=self.search_item)
        self.search_button.pack(side=tk.LEFT)

    def load_collection(self):
        with open("collection.txt", "r") as f:
            for line in f:
                item = line.strip().split(",")
                self.collection.append(item)

    def save_collection(self):
        with open("collection.txt", "w") as f:
            for item in self.collection:
                f.write(",".join(item) + "\n")

    def show_add_item(self):
        self.add_frame.pack()

    def hide_add_item(self):
        self.add_frame.pack_forget()

    def add_item(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        genre = self.genre_entry.get()
        rating = self.rating_entry.get()

        if not all([title, author, year, genre, rating]):
            messagebox.showwarning("Error", "All fields are required.")
            return

        new_item = [title, author, year, genre, rating]
        self.collection.append(new_item)
        self.collection_treeview.insert("", tk.END, text=new_item[0], values=new_item[1:])
        self.save_collection()
        self.hide_add_item()

    def edit_item(self):
        self.hide_add_item()
        self.edit_button.config(state=tk.DISABLED)
        selected_item = self.collection_treeview.focus()
        if selected_item:
            title = self.collection_treeview.item(selected_item)["text"]
            for i, item in enumerate(self.collection):
                if item[0] == title:
                    self.edit_frame = tk.Frame(self.master, padx=10, pady=10)
                    self.edit_frame.pack()

                    self.title_label = tk.Label(self.edit_frame, text="Title:")
                    self.title_label.grid(row=0, column=0, sticky=tk.W)
                    self.title_entry = tk.Entry(self.edit_frame, text=item[0])
                    self.title_entry.grid(row=0, column=1)

                    self.author_label = tk.Label(self.edit_frame, text="Author:")
                    self.author_label.grid(row=1, column=0, sticky=tk.W)
                    self.author_entry = tk.Entry(self.edit_frame, text=item[1])
                    self.author_entry.grid(row=1, column=1)

                    self.year_label = tk.Label(self.edit_frame, text="Year:")
                    self.year_label.grid(row=2, column=0, sticky=tk.W)
                    self.year_entry = tk.Entry(self.edit_frame, text=item[2])
                    self.year_entry.grid(row=2, column=1)

                    self.genre_label = tk.Label(self.edit_frame, text="Genre:")
                    self.genre_label.grid(row=3, column=0, sticky=tk.W)
                    self.genre_entry = tk.Entry(self.edit_frame, text=item[3])
                    self.genre_entry.grid(row=3, column=1)

                    self.rating_label = tk.Label(self.edit_frame, text="Rating:")
                    self.rating_label.grid(row=4, column=0, sticky=tk.W)
                    self.rating_entry = tk.Entry(self.edit_frame, text=item[4])
                    self.rating_entry.grid(row=4, column=1)

                    self.save_button = tk.Button(self.edit_frame, text="Save", command=lambda: self.save_edited_item(i))
                    self.save_button.grid(row=5, column=0, columnspan=2)
        else:
            messagebox.showwarning("Error", "Please select an item to edit.")


    def save_edited_item(self, index):
        self.edit_button.config(state=tk.NORMAL)
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        genre = self.genre_entry.get()
        rating = self.rating_entry.get()

        if not all([title, author, year, genre, rating]):
            messagebox.showwarning("Error", "All fields are required.")
            return

        edited_item = [title, author, year, genre, rating, rating]
        self.collection[index] = edited_item
        self.collection_treeview.item(self.collection_treeview.focus(), text=edited_item[0], values=edited_item[1:])
        self.save_collection()
        self.edit_frame.pack_forget()

    def delete_item(self):
        selected_item = self.collection_treeview.focus()
        if selected_item:
            title = self.collection_treeview.item(selected_item)["text"]
            for i, item in enumerate(self.collection):
                if item[0] == title:
                    del self.collection[i]
                    self.collection_treeview.delete(selected_item)
                    self.save_collection()
                    break
        else:
            messagebox.showwarning("Error", "Please select an item to delete.")


    def search_item(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = CollectionManager(root)
    root.mainloop()
