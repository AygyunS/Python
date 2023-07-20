import os
from tkinter import Image
from PIL import ImageTk

print('loaded utils.py')


def load_images_from_directory(directory="img"):
    image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".ico"]
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.splitext(f)[1].lower() in image_extensions]
