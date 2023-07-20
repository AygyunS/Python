from PIL import ImageFilter

print('loaded image_processing.py')


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
