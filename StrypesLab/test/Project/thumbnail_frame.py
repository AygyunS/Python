import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class ThumbnailFrame(tk.Frame):
    def __init__(self, parent, image_list, select_image_callback):
        super().__init__(parent)
        self.image_list = image_list
        self.select_image_callback = select_image_callback
        self.thumbnail_labels = []  # Initialize the thumbnail_labels attribute here
        self.create_widgets()

    def create_widgets(self):
        self.thumbnail_canvas = tk.Canvas(self)
        self.thumbnail_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.thumbnail_canvas.yview)
        self.thumbnail_canvas.configure(yscrollcommand=self.thumbnail_scrollbar.set)

        self.thumbnail_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.thumbnail_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.thumbnail_canvas.bind('<Configure>', lambda e: self.thumbnail_canvas.configure(scrollregion=self.thumbnail_canvas.bbox("all")))

        self.thumbnail_frame_inner = tk.Frame(self.thumbnail_canvas)
        self.thumbnail_canvas.create_window((0, 0), window=self.thumbnail_frame_inner, anchor="nw")

        self.load_thumbnails()

    def create_thumbnail(self, image_path, thumbnail_size=(100, 100)):
        try:
            with Image.open(image_path) as img:
                img.thumbnail(thumbnail_size)
                thumbnail_image = ImageTk.PhotoImage(img)
                return thumbnail_image
        except Exception as e:
            print(f"Error creating thumbnail: {e}")
            return None

    def load_thumbnails(self):
        for i, image_path in enumerate(self.image_list):
            thumbnail = Image.open(image_path)
            thumbnail = thumbnail.resize((100, int(100 * thumbnail.height / thumbnail.width)), Image.ANTIALIAS)
            tk_thumbnail = ImageTk.PhotoImage(thumbnail)

            thumbnail_label = tk.Label(self.thumbnail_frame_inner, image=tk_thumbnail)
            thumbnail_label.image = tk_thumbnail
            thumbnail_label.grid(row=i, column=0, padx=5, pady=5)
            thumbnail_label.bind("<Button-1>", lambda event, index=i: self.select_image(event, index))

    def select_image(self, event, index):
        self.select_image_callback(event, index)

    def update_thumbnails(self, image_list):
        self.image_list = image_list

        # Create new thumbnail labels if required
        while len(self.thumbnail_labels) < len(self.image_list):
            index = len(self.thumbnail_labels)
            thumbnail_label = tk.Label(self, cursor="hand2")
            thumbnail_label.bind("<Button-1>", lambda event, idx=index: self.select_image_callback(idx))
            self.thumbnail_labels.append(thumbnail_label)

        for i, thumbnail_label in enumerate(self.thumbnail_labels):
            if i < len(self.image_list):
                thumbnail_image = self.create_thumbnail(self.image_list[i])
                thumbnail_label.config(image=thumbnail_image)
                thumbnail_label.image = thumbnail_image
                thumbnail_label.grid(row=i // 5, column=i % 5, padx=5, pady=5)
            else:
                thumbnail_label.grid_remove()