import os
from PIL import Image

def load_images(img_folder):
    img_files = [os.path.join(img_folder, f) for f in os.listdir(img_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
    return img_files

def get_image_info(img_path):
    img = Image.open(img_path)
    width, height = img.size
    img_format = img.format
    info = f"Dimensions: {width} x {height}\nFormat: {img_format}"
    return info

def rotate_image(img, angle):
    return img.rotate(angle)

def flip_horizontal(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)

def flip_vertical(img):
    return img.transpose(Image.FLIP_TOP_BOTTOM)

def save_image(img, filename):
    img.save(filename)
