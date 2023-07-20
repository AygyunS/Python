import os
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageFilter
import shutil #копиране на снимките

class ImageViewerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Viewer")
        self.geometry("1400x800")

        self.current_image = None
        self.image_list = self.load_images_from_directory()
        self.current_index = 0

        self.create_widgets()
        self.load_image()
        self.crop_rectangle = None



    def load_images_from_directory(self):
        supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
        image_list = [filename for filename in os.listdir() if filename.lower().endswith(supported_formats)]
        return image_list

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

        self.thumbnail_frame = tk.Frame(self)
        self.thumbnail_frame.pack(side=tk.LEFT, padx=2, fill=tk.Y)

        self.thumbnail_canvas = tk.Canvas(self.thumbnail_frame, width=150)
        self.thumbnail_canvas.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.thumbnail_frame, orient="vertical", command=self.thumbnail_canvas.yview, width=20)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.thumbnail_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.thumbnail_canvas.bind('<Configure>', lambda e: self.thumbnail_canvas.configure(scrollregion=self.thumbnail_canvas.bbox('all')))

        self.inner_thumbnail_frame = tk.Frame(self.thumbnail_canvas)
        self.thumbnail_canvas.create_window((0, 0), window=self.inner_thumbnail_frame, anchor='nw')

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

        filter_names = [
            "Размазване",
            "Острота",
            "Намиране на ръбове",
            "Релеф",
            "Контури",
            "Черно-бяло",
        ]

        self.filter_menu = tk.OptionMenu(self.right_button_frame, self.selected_filter, *filter_names)
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

        for index, image_path in enumerate(self.image_list):
            thumbnail = self.create_thumbnail(image_path)
            thumbnail_label = tk.Label(self.inner_thumbnail_frame, image=thumbnail, cursor="hand2")
            thumbnail_label.image = thumbnail
            thumbnail_label.bind('<Button-1>', lambda event, idx=index: self.select_image(event, idx))
            thumbnail_label.pack(side=tk.TOP, pady=1)

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


    def create_thumbnail(self, image_path, fixed_width=100):
        img = Image.open(image_path)
        aspect_ratio = img.height / img.width
        new_height = int(fixed_width * aspect_ratio)
        img = img.resize((fixed_width, new_height), Image.ANTIALIAS)
        thumbnail = ImageTk.PhotoImage(img)
        return thumbnail

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

    def apply_filter(self):

        self.current_image = self.current_image.filter(ImageFilter.BLUR)
        self.update_image()

    def update_image(self):
        tk_image = ImageTk.PhotoImage(self.current_image)
        self.label.config(image=tk_image)
        self.label.image = tk_image

    def reset_image(self):
        self.load_image()

    def apply_filter_blur(self):
        self.current_image = self.current_image.filter(ImageFilter.BLUR)
        self.update_image()

    def apply_filter_sharpen(self):
        self.current_image = self.current_image.filter(ImageFilter.SHARPEN)
        self.update_image()

    def apply_filter_edges(self):
        self.current_image = self.current_image.filter(ImageFilter.FIND_EDGES)
        self.update_image()

    def apply_filter_emboss(self):
        self.current_image = self.current_image.filter(ImageFilter.EMBOSS)
        self.update_image()

    def apply_filter_contour(self):
        self.current_image = self.current_image.filter(ImageFilter.CONTOUR)
        self.update_image()

    def apply_filter_greyscale(self):
        self.current_image = self.current_image.convert('L')
        self.update_image()

    def apply_selected_filter(self):
        filter_name = self.selected_filter.get()

        if filter_name == "Размазване":
            self.apply_filter_blur()
        elif filter_name == "Острота":
            self.apply_filter_sharpen()
        elif filter_name == "Намиране на ръбове":
            self.apply_filter_edges()
        elif filter_name == "Релеф":
            self.apply_filter_emboss()
        elif filter_name == "Контури":
            self.apply_filter_contour()
        elif filter_name == "Черно-бяло":
            self.apply_filter_greyscale()
        else:
            messagebox.showerror("Грешка", "Моля, изберете валиден филтър.")

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp"),
                                                            ("All files", "*.*")])
        if file_path:
            self.current_image.save(file_path)

    def clear_thumbnail_list(self):
        for child in self.inner_thumbnail_frame.winfo_children():
            child.destroy()

    def refresh_thumbnail_list(self):
        self.clear_thumbnail_list()
        self.image_list = self.load_images_from_directory()

        for index, image_path in enumerate(self.image_list):
            thumbnail = self.create_thumbnail(image_path)
            thumbnail_label = tk.Label(self.inner_thumbnail_frame, image=thumbnail, cursor="hand2")
            thumbnail_label.image = thumbnail
            thumbnail_label.bind('<Button-1>', lambda event, idx=index: self.select_image(event, idx))
            thumbnail_label.pack(side=tk.TOP, pady=1)

        self.thumbnail_canvas.update_idletasks()

    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Images", ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.gif", "*.tiff", "*.ico")),
                       ("All files", "*.*")])
        if file_path:
            # Copy the image to the project folder
            file_name = os.path.basename(file_path)
            new_file_path = os.path.join(os.getcwd(), file_name)
            shutil.copy(file_path, new_file_path)

            # Add the new file path to the image list and update the current index
            self.image_list.append(new_file_path)
            self.current_index = len(self.image_list) - 1
            self.load_image()

            # Refresh the thumbnail list
            self.refresh_thumbnail_list()

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

        # Refresh the thumbnail list and scrollbar
        self.refresh_thumbnail_list()

        # Update the current index and load the next image
        self.current_index = min(self.current_index, len(self.image_list) - 1)
        if self.image_list:
            self.load_image()
        else:
            self.label.config(image="")


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
