from tkinter import ttk


class TreeView(ttk.Treeview):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, columns=('Author', 'Year', 'Genre', 'Rating'), *args, **kwargs)
        self.heading('#0', text='Title')
        self.heading('Author', text='Author')
        self.heading('Year', text='Year')
        self.heading('Genre', text='Genre')
        self.heading('Rating', text='Rating')
