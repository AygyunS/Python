import tkinter as tk
import os
from tkinter import filedialog
from PIL import Image, ImageTk
from utils import get_image_info, rotate_image, flip_horizontal, flip_vertical, save_image
import shutil

class ImageList(tk.Frame):
    def __init__(self, parent, image_viewer, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.image_viewer = image_viewer

        self.listbox = tk.Listbox(self)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", self.on_image_select)

    def add_image(self, img_path):
        self.listbox.insert(tk.END, img_path)

    def on_image_select(self, event):
        selected_index = self.listbox.curselection()[0]
        selected_image = self.listbox.get(selected_index)
        self.image_viewer.display_image(selected_image)

class ImageViewer(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(borderwidth=2, relief="groove")
        self.image = None

    def display_image(self, img_path):
        img = Image.open(img_path)
        img.thumbnail((400, 400))
        self.image = ImageTk.PhotoImage(img)
        self.config(image=self.image)

class ButtonPanel(tk.Frame):
    def __init__(self, parent, image_list, image_viewer, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.image_list = image_list
        self.image_viewer = image_viewer

        info_button = tk.Button(self, text="Info", command=self.show_image_info)
        info_button.pack(fill="x")

        open_button = tk.Button(self, text="Open", command=self.open_image)
        open_button.pack(fill="x")

        rotate_left_button = tk.Button(self, text="Rotate Left", command=self.rotate_left)
        rotate_left_button.pack(fill="x")

        rotate_right_button = tk.Button(self, text="Rotate Right", command=self.rotate_right)
        rotate_right_button.pack(fill="x")

        flip_horizontal_button = tk.Button(self, text="Flip Horizontal", command=self.flip_horizontal)
        flip_horizontal_button.pack(fill="x")

        flip_vertical_button = tk.Button(self, text="Flip Vertical", command=self.flip_vertical)
        flip_vertical_button.pack(fill="x")

    def show_image_info(self):
        selected_index = self.image_list.listbox.curselection()[0]
        selected_image = self.image_list.listbox.get(selected_index)
        info = get_image_info(selected_image)
        tk.messagebox.showinfo("Image Info", info)

    def open_image(self):
        img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.bmp;*.gif")])
        if img_path:
            img_name = os.path.basename(img_path)
            save_path = os.path.join("img", img_name)  # Change this line to include the "img" folder
            img = Image.open(img_path)
            save_image(img, save_path)
            shutil.move(img_path, save_path)  # Add this line to move the opened image to the "img" folder
            self.image_list.add_image(save_path)
            self.image_list.listbox.selection_clear(0, tk.END)
            self.image_list.listbox.selection_set(tk.END)
            self.image_list.listbox.yview(tk.END)

    def rotate_left(self):
        self._transform_image(rotate_image, -90)

    def rotate_right(self):
        self._transform_image(rotate_image, 90)

    def flip_horizontal(self):
        self._transform_image(flip_horizontal)

    def flip_vertical(self):
        self._transform_image(flip_vertical)

    def _transform_image(self, transform_func, *args):
        selected_index = self.image_list.listbox.curselection()[0]
        selected_image = self.image_list.listbox.get(selected_index)
        img = Image.open(selected_image)
        transformed_img = transform_func(img, *args)
        save_image(transformed_img, selected_image)
        self.image_viewer.display_image(selected_image)

