from PIL import Image, ImageTk

print('loaded utils.py')


def create_thumbnail(image_path, thumbnail_size):
    print('using it')
    img = Image.open(image_path)
    width, height = thumbnail_size
    aspect_ratio = img.height / img.width
    new_height = int(width * aspect_ratio)
    img = img.resize((width, new_height), Image.ANTIALIAS)
    thumbnail = ImageTk.PhotoImage(img)
    return thumbnail
