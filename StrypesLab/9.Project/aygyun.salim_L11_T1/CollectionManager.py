import json
import tkinter as tk
from tkinter import messagebox, ttk


class CollectionManager:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Data file not found or corrupted.")
            return {'Movies': [], 'Video games': [], 'Books': []}

    def save_data(self):
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError:
            messagebox.showerror("Error", "Failed to save data.")

    def create_item(self, category, item):
        self.data[category].append(item)
        self.save_data()

    def read_item(self, category, index):
        return self.data[category][index]

    def update_item(self, category, index, item):
        self.data[category][index] = item
        self.save_data()

    def delete_item(self, category, index):
        del self.data[category][index]
        self.save_data()

    def search(self, category, search_term):
        results = []
        for item in self.data[category]:
            if (search_term.lower() in item['title'].lower() or
                    search_term.lower() in item['author'].lower() or
                    search_term.lower() in item['year']):
                results.append(item)
        return results


class CollectionGUI(tk.Tk):
    def __init__(self, collection_manager):
        super().__init__()
        self.collection_manager = collection_manager
        self.title("Collection Manager")
        self.geometry("830x770")
        self.resizable(False, False)
        self.create_widgets()

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def create_widgets(self):
        self.category_var = tk.StringVar(self)
        self.category_var.set("Movies")

        def update_listbox(*args):
            self.update_listbox()

        category_menu = tk.OptionMenu(self, self.category_var, "Movies", "Video games", "Books", command=update_listbox)
        category_menu.config(width=12)
        category_menu.grid(row=0, column=0, padx=10, pady=10)

        self.search_var = tk.StringVar(self)
        search_entry = tk.Entry(self, textvariable=self.search_var)
        search_entry.grid(row=0, column=1, padx=10, pady=10)

        search_button = tk.Button(self, text="Search", command=self.search, width=15, height=2, font=("Arial", 14))
        search_button.grid(row=0, column=2, padx=10, pady=10)

        reset_button = tk.Button(self, text="Reset", command=self.update_listbox, width=15, height=2, font=("Arial", 14))
        reset_button.grid(row=0, column=3, padx=10, pady=10)

        self.result_treeview = ttk.Treeview(self, columns=("Title", "Author", "Year"), show="headings", height=20)
        self.result_treeview.heading("Title", text="Title")
        self.result_treeview.heading("Author", text="Author")
        self.result_treeview.heading("Year", text="Year")
        self.result_treeview.column("Title", width=300, stretch=False)
        self.result_treeview.column("Author", width=250, stretch=False)
        self.result_treeview.column("Year", width=100, stretch=False)
        self.result_treeview.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        scrollbar.config(command=self.result_treeview.yview)
        scrollbar.grid(row=1, column=4, sticky="NS")

        self.result_treeview.config(yscrollcommand=scrollbar.set)

        self.update_listbox()

        add_button = tk.Button(self, text="Add", command=self.add_item, width=15, height=2, font=("Arial", 14))
        add_button.grid(row=2, column=0, padx=10, pady=10)

        edit_button = tk.Button(self, text="Edit", command=self.edit_item, width=15, height=2, font=("Arial", 14))
        edit_button.grid(row=2, column=1, padx=10, pady=10)

        delete_button = tk.Button(self, text="Delete", command=self.delete_item, width=15, height=2, font=("Arial", 14))
        delete_button.grid(row=2, column=2, padx=10, pady=10)

        clear_button = tk.Button(self, text="Clear", command=self.clear_fields, width=15, height=2, font=("Arial", 14))
        clear_button.grid(row=2, column=3, padx=10, pady=10)

        tk.Label(self, text="Title").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self, text="Author").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self, text="Author").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self, text="Year").grid(row=5, column=0, padx=10, pady=10)

        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=3, column=1, padx=10, pady=10)

        self.author_entry = tk.Entry(self)
        self.author_entry.grid(row=4, column=1, padx=10, pady=10)

        self.year_entry = tk.Entry(self)
        self.year_entry.grid(row=5, column=1, padx=10, pady=10)

        self.update_button = tk.Button(self, text="Update", command=self.update_item, width=15, height=2,
                                       font=("Arial", 14))
        self.update_button.grid(row=6, column=0, padx=10, pady=10)

        quit_button = tk.Button(self, text="Quit", command=self.destroy, width=15, height=2, font=("Arial", 14))
        quit_button.grid(row=6, column=1, padx=10, pady=10)

    def update_listbox(self):
        self.result_treeview.delete(*self.result_treeview.get_children())
        category = self.category_var.get()
        for item in self.collection_manager.data[category]:
            self.result_treeview.insert("", tk.END, values=(item['title'], item['author'], item['year']))

    def search(self):
        search_term = self.search_var.get()
        if not search_term:
            messagebox.showerror("Error", "Please enter a search term.")
            return

        category = self.category_var.get()
        results = self.collection_manager.search(category, search_term)

        self.result_treeview.delete(*self.result_treeview.get_children())

        for item in results:
            self.result_treeview.insert("", tk.END, values=(item['title'], item['author'], item['year']))

    def is_valid_year(self, year):
        if not year.isdigit() or len(year) >= 5:
            return False
        return True

    def add_item(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        category = self.category_var.get()

        if not title or not author or not year:
            self.show_error("Please enter a value for all fields.")
            return

        if not self.is_valid_year(year):
            self.show_error("Please enter a valid year.")
            return

        item = {'title': title, 'author': author, 'year': year}
        self.collection_manager.create_item(category, item)
        self.update_listbox()

    def edit_item(self):
        selected_item = self.result_treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an item to edit.")
            return

        item_values = self.result_treeview.item(selected_item, "values")
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(tk.END, item_values[0])

        self.author_entry.delete(0, tk.END)
        self.author_entry.insert(tk.END, item_values[1])

        self.year_entry.delete(0, tk.END)
        self.year_entry.insert(tk.END, item_values[2])

    def update_item(self):
        selected_item = self.result_treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an item to update.")
            return

        index = self.result_treeview.index(selected_item)
        category = self.category_var.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()

        if not title or not author or not year:
            messagebox.showerror("Error", "Please enter a value for all fields.")
            return

        if not self.is_valid_year(year):
            messagebox.showerror("Error", "Please enter a valid year.")
            return

        item = {'title': title, 'author': author, 'year': year}
        self.collection_manager.update_item(category, index, item)
        self.update_listbox()

    def delete_item(self):
        selected_item = self.result_treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an item to delete.")
            return

        index = self.result_treeview.index(selected_item)
        category = self.category_var.get()

        self.collection_manager.delete_item(category, index)
        self.update_listbox()

    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)


data_file = "data.json"
collection_manager = CollectionManager(data_file)
app = CollectionGUI(collection_manager)
app.mainloop()


