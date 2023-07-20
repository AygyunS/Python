import os
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import shutil
from utils import load_images_from_directory
import image_processing
from image_list import ImageList

print('loaded image_viewer_app.py')


class ImageViewerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Viewer")
        self.geometry("1400x800")

        self.current_image = None
        self.image_list = load_images_from_directory()
        self.current_index = 0

        self.create_widgets()
        self.load_image()
        self.crop_rectangle = None

    def create_widgets(self):
        button_styles = {
            "width": 30,
            "height": 3,
            "bg": "#197fd4",
            "fg": "black",
            "relief": tk.RAISED,
            "bd": 2,
            "font": ("Arial", 12, "bold"),
        }

        self.image_list_frame = ImageList(self, self.select_image)
        self.image_list_frame.pack(side=tk.LEFT, padx=5, fill=tk.Y)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.LEFT, padx=5, fill=tk.Y)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.main_frame)
        self.label.pack()

        self.reset_button = tk.Button(self.button_frame, text="Възстанови", command=self.reset_image)
        self.reset_button.pack(pady=5)

        self.info_button = tk.Button(self.button_frame, text="Информация", command=self.show_image_info)
        self.info_button.pack(pady=5)

        self.rotate_button = tk.Button(self.button_frame, text="Завърти на 90 градуса", command=self.rotate_image)
        self.rotate_button.pack(pady=5)

        self.flip_horizontal_button = tk.Button(self.button_frame, text="Хоризонтално огледално обръщане",
                                                command=self.flip_image_horizontal)
        self.flip_horizontal_button.pack(pady=5)

        self.flip_vertical_button = tk.Button(self.button_frame, text="Вертикално огледално обръщане",
                                              command=self.flip_image_vertical)
        self.flip_vertical_button.pack(pady=5)

        self.right_button_frame = tk.Frame(self)
        self.right_button_frame.pack(side=tk.RIGHT, fill=tk.Y)


        self.selected_filter = tk.StringVar(self.button_frame)
        self.selected_filter.set("Избери филтър")

        self.filter_functions = {
            "Blur": lambda: image_processing.apply_filter_blur(self.current_image),
            "Sharpen": lambda: image_processing.apply_filter_sharpen(self.current_image),
            "Find Edges": lambda: image_processing.apply_filter_edges(self.current_image),
            "Emboss": lambda: image_processing.apply_filter_emboss(self.current_image),
            "Contour": lambda: image_processing.apply_filter_contour(self.current_image),
            "Greyscale": lambda: image_processing.apply_filter_greyscale(self.current_image),
        }

        self.filter_menu = tk.OptionMenu(self.right_button_frame, self.selected_filter, *self.filter_functions.keys())
        self.filter_menu.config(width=22, height=3)
        self.filter_menu.pack(pady=2)

        self.apply_filter_button = tk.Button(self.right_button_frame, text="Приложи филтър",
                                             command=self.apply_selected_filter)
        self.apply_filter_button.pack(pady=5)

        self.open_button = tk.Button(self.button_frame, text="Отвори", command=self.open_image)
        self.open_button.pack(pady=5)

        self.save_button = tk.Button(self.right_button_frame, text="Запази снимката", command=self.save_image)
        self.save_button.pack(pady=5)

        self.delete_button = tk.Button(self.right_button_frame, text="Изтрий", command=self.delete_image)
        self.delete_button.pack(pady=5)

        self.crop_button = tk.Button(self.button_frame, text="Изрежи", command=self.enable_crop_mode)
        self.crop_button.pack(pady=5)


        #Конфигурация на бутоните
        self.reset_button.config(**button_styles)
        self.info_button.config(**button_styles)
        self.rotate_button.config(**button_styles)
        self.flip_horizontal_button.config(**button_styles)
        self.flip_vertical_button.config(**button_styles)
        self.apply_filter_button.config(**button_styles)
        self.open_button.config(**button_styles)
        self.save_button.config(**button_styles)
        self.delete_button.config(**button_styles)
        self.crop_button.config(**button_styles)

    def select_image(self, event, index):
        self.current_index = index
        self.load_image()

    def load_image(self):
        image_path = self.image_list[self.current_index]
        self.current_image = Image.open(image_path)

        # Resize the image while maintaining its aspect ratio
        fixed_width = 500  # Set the fixed width
        aspect_ratio = self.current_image.height / self.current_image.width
        new_height = int(fixed_width * aspect_ratio)
        self.current_image = self.current_image.resize((fixed_width, new_height), Image.ANTIALIAS)

        self.update_image()

    def show_image_info(self):
        image_path = self.image_list[self.current_index]
        image_name = os.path.basename(image_path)
        image_size = self.current_image.size
        image_mode = self.current_image.mode

        info_text = f"Име: {image_name}\nРазмер: {image_size}\nРежим на цветовете: {image_mode}"
        messagebox.showinfo("Информация за изображението", info_text)

    def rotate_image(self):

        self.current_image = self.current_image.rotate(90)
        self.update_image()

    def flip_image_horizontal(self):

        self.current_image = self.current_image.transpose(Image.FLIP_LEFT_RIGHT)
        self.update_image()

    def flip_image_vertical(self):

        self.current_image = self.current_image.transpose(Image.FLIP_TOP_BOTTOM)
        self.update_image()

    def update_image(self):
        tk_image = ImageTk.PhotoImage(self.current_image)
        self.label.config(image=tk_image)
        self.label.image = tk_image

    def reset_image(self):
        self.load_image()

    def apply_selected_filter(self):
        filter_name = self.selected_filter.get()
        if filter_name in self.filter_functions:
            self.current_image = self.filter_functions[filter_name]()
            self.update_image()
        else:
            messagebox.showerror("Error", "Please select a valid filter.")

    def save_image(self):
        img_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
        initialdir = img_directory

        file_path = filedialog.asksaveasfilename(initialdir=initialdir, defaultextension=".png",
                                                 filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp"),
                                                            ("All files", "*.*")])

        if file_path:
            self.current_image.save(file_path)
            self.image_list_frame.update_image_list()

    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Images", ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.gif", "*.tiff", "*.ico")),
                       ("All files", "*.*")])
        if file_path:
            # Copy the image to the project folder
            file_name = os.path.basename(file_path)
            img_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')

            # Ensure unique file name in the 'img' directory
            file_name_wo_ext, file_ext = os.path.splitext(file_name)
            counter = 1
            while os.path.exists(os.path.join(img_directory, file_name)):
                file_name = f"{file_name_wo_ext}_{counter}{file_ext}"
                counter += 1

            new_file_path = os.path.join(img_directory, file_name)
            shutil.copy(file_path, new_file_path)

            # Add the new file path to the image list and update the current index
            self.image_list.append(new_file_path)
            self.current_index = len(self.image_list) - 1
            self.load_image()

            self.image_list_frame.update_image_list(selected_index=self.current_index)

    def delete_image(self):
        if not self.image_list:
            messagebox.showwarning("Внимание", "Няма изображения за изтриване.")
            return

        image_path = self.image_list[self.current_index]
        try:
            os.remove(image_path)
        except Exception as e:
            messagebox.showerror("Грешка", f"Изтриването на изображението не успя: {e}")
            return

        # Remove the deleted image from the image list
        self.image_list.pop(self.current_index)

        # Update the current index and load the next image
        self.current_index = min(self.current_index, len(self.image_list) - 1)
        if self.image_list:
            self.load_image()
        else:
            self.label.config(image="")

        # Add this line to update the image list
        self.image_list_frame.update_image_list()

    def start_crop(self, event):
        if self.crop_rectangle:
            self.label.delete(self.crop_rectangle)
        self.crop_start_x = event.x
        self.crop_start_y = event.y

    def end_crop(self, event):
        x1, y1, x2, y2 = self.crop_start_x, self.crop_start_y, event.x, event.y
        self.crop_rectangle = (x1, y1, x2, y2)
        self.crop_image()

    def crop_image(self):
        if self.crop_rectangle:
            x1, y1, x2, y2 = self.crop_rectangle
            self.current_image = self.current_image.crop((x1, y1, x2, y2))
            self.update_image()
            self.crop_rectangle = None

    def enable_crop_mode(self):
        if not self.image_list:
            messagebox.showwarning("Внимание", "Няма изображения за изрязване.")
            return

        if self.crop_button['text'] == "Изрежи":
            self.crop_button.config(text="Изход")
            self.label.bind("<ButtonPress-1>", self.start_crop)
            self.label.bind("<ButtonRelease-1>", self.end_crop)
        else:
            self.crop_button.config(text="Изрежи")
            self.label.unbind("<ButtonPress-1>")
            self.label.unbind("<ButtonRelease-1>")

if __name__ == "__main__":
    app = ImageViewerApp()
    app.mainloop()