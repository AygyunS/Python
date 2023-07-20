import os
from PIL import Image, ImageFilter


def load_images_from_directory(img_folder="img"):
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    current_directory = os.path.dirname(os.path.abspath(__file__))
    img_directory = os.path.join(current_directory, img_folder)

    image_list = [os.path.join(img_directory, filename) for filename in os.listdir(img_directory) if
                  filename.lower().endswith(supported_formats)]

    # Sort the image list by creation date
    image_list.sort(key=lambda x: os.path.getctime(x), reverse=True)

    return image_list


def apply_filter_blur(current_image):
    return current_image.filter(ImageFilter.BLUR)


def apply_filter_sharpen(current_image):
    return current_image.filter(ImageFilter.SHARPEN)


def apply_filter_edges(current_image):
    return current_image.filter(ImageFilter.FIND_EDGES)


def apply_filter_emboss(current_image):
    return current_image.filter(ImageFilter.EMBOSS)


def apply_filter_contour(current_image):
    return current_image.filter(ImageFilter.CONTOUR)


def apply_filter_greyscale(current_image):
    return current_image.convert('L')
