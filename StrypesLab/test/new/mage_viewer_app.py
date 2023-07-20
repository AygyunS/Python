import tkinter as tk
from components import ImageList, ImageViewer, ButtonPanel
from utils import load_images

class ImageEditorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Viewer and Editor")
        self.geometry("1400x800")
        self.resizable(False, False)

        self.images = load_images("img")

        self.image_viewer = ImageViewer(self)
        self.image_viewer.pack(side="left", fill="both", expand=True)

        self.image_list = ImageList(self, self.image_viewer)
        self.image_list.pack(side="left", fill="y")

        for image in self.images:
            self.image_list.add_image(image)

        self.button_panel = ButtonPanel(self, self.image_list, self.image_viewer)
        self.button_panel.pack(side="left", fill="y")

        if self.images:
            self.image_viewer.display_image(self.images[0])
            self.image_list.listbox.selection_set(0)

if __name__ == "__main__":
    app = ImageEditorApp()
    app.mainloop()
