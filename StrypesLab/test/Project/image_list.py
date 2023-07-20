import os
import tkinter as tk
from utils import load_images_from_directory

class ImageList(tk.Frame):
    def __init__(self, master, select_image_callback):
        super().__init__(master)

        self.image_list = load_images_from_directory()
        self.select_image_callback = select_image_callback

        self.listbox = tk.Listbox(self, width=40, height=20)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        for image_path in self.image_list:
            image_name = os.path.basename(image_path)
            self.listbox.insert(tk.END, image_name)

        self.listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

    def on_listbox_select(self, event):
        index = self.listbox.curselection()[0]
        self.select_image_callback(event, index)

    def update_image_list(self, selected_index=None):
        img_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
        self.image_list = load_images_from_directory(img_directory)

        self.listbox.delete(0, tk.END)
        for index, image_path in enumerate(self.image_list):
            image_name = os.path.basename(image_path)
            self.listbox.insert(tk.END, image_name)

            if selected_index is not None and index == selected_index:
                self.listbox.selection_set(selected_index)
