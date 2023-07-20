import os
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageDraw, ImageFont, ImageOps, ImageChops
import shutil
from image_processing import load_images_from_directory, apply_filter_blur, apply_filter_sharpen, apply_filter_edges, apply_filter_emboss, apply_filter_contour, apply_filter_greyscale
import matplotlib.pyplot as plt
import cv2
import numpy as np


print('loaded image_viewer_app.py')


class ImageViewerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Viewer")
        self.geometry("1440x800")

        self.current_image = None
        self.image_list = load_images_from_directory()
        self.current_index = 0

        self.create_widgets()
        self.load_image()

        self.crop_rectangle = None
        self.crop_coordinates = None
        self.crop_canvas = None

    def create_widgets(self):
        button_styles = {
            "width": 12,
            "height": 3,
            "bg": "#197fd4",
            "fg": "black",
            "relief": tk.RAISED,
            "bd": 2,
            "font": ("Arial", 12, "bold"),
        }

        self.undo_stack = []
        self.redo_stack = []

        self.thumbnail_frame = tk.Frame(self)
        self.thumbnail_frame.pack(side=tk.LEFT, padx=0, pady=0, fill=tk.Y)

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
        self.main_frame.pack(side=tk.BOTTOM, padx=0, pady=0, anchor="n", fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.main_frame)
        self.label.pack(padx=0, pady=0, anchor="n")

        #Levite butoni
        self.rotate_button = tk.Button(self.button_frame, text="Завърти", command=self.rotate_image)
        self.rotate_button.grid(row=1, column=0, pady=5)

        self.rotate_counter_clockwise = tk.Button(self.button_frame, text="Завърти обратно", command=self.rotate_counter_clockwise)
        self.rotate_counter_clockwise.grid(row=1, column=1, pady=5)

        self.flip_horizontal_button = tk.Button(self.button_frame, text="Хоризонтално",
                                                command=self.flip_image_horizontal)
        self.flip_horizontal_button.grid(row=2, column=0, pady=5)

        self.flip_vertical_button = tk.Button(self.button_frame, text="Вертикално",
                                              command=self.flip_image_vertical)
        self.flip_vertical_button.grid(row=2, column=1, pady=5)

        self.open_button = tk.Button(self.button_frame, text="Отвори", command=self.open_image)
        self.open_button.grid(row=3, column=1, pady=5)

        self.crop_button = tk.Button(self.button_frame, text="Изрежи", command=self.enable_crop_mode)
        self.crop_button.grid(row=3, column=0, pady=5)

        self.zoom_in_button = tk.Button(self.button_frame, text="Увеличи", command=self.zoom_in)
        self.zoom_in_button.grid(row=4, column=1, pady=5)

        self.zoom_out_button = tk.Button(self.button_frame, text="Намали", command=self.zoom_out)
        self.zoom_out_button.grid(row=4, column=0, pady=5)



        # konstrast i svetlost
        self.increase_brightness_button = tk.Button(self.button_frame, text="Увеличи яркост",
                                                    command=self.increase_brightness)
        self.increase_brightness_button.grid(row=5, column=1, pady=5)

        self.decrease_brightness_button = tk.Button(self.button_frame, text="Намали яркост",
                                                    command=self.decrease_brightness)
        self.decrease_brightness_button.grid(row=5, column=0, pady=5)

        self.increase_contrast_button = tk.Button(self.button_frame, text="Увеличи контраст",
                                                  command=self.increase_contrast)
        self.increase_contrast_button.grid(row=6, column=1, pady=5)

        self.decrease_contrast_button = tk.Button(self.button_frame, text="Намали контраст",
                                                  command=self.decrease_contrast)
        self.decrease_contrast_button.grid(row=6, column=0, pady=5)

        self.invert_colors_button = tk.Button(self.button_frame, text="Обр. цветове", command=self.invert_colors)
        self.invert_colors_button.grid(row=7, column=0, pady=5)

        self.add_text_button = tk.Button(self.button_frame, text="Текст", command=self.add_text_to_image)
        self.add_text_button.grid(row=7, column=1, pady=5)

        self.histogram_button = tk.Button(self.button_frame, text="Хистограма", command=self.show_image_histogram)
        self.histogram_button.grid(row=8, column=0, pady=5)

        self.blend_button = tk.Button(self.button_frame, text="Смесване", command=self.blend_images)
        self.blend_button.grid(row=8, column=1, pady=5)

        self.adjust_opacity = tk.Button(self.button_frame, text="Прозрачност", command=self.adjust_opacity)
        self.adjust_opacity.grid(row=9, column=0, pady=5)

        self.auto_enhance_button = tk.Button(self.button_frame, text="Авто подобряване",
                                             command=self.apply_auto_enhance)
        self.auto_enhance_button.grid(row=9, column=1, pady=5)

        self.adjust_hsl_button = tk.Button(self.button_frame, text="Настройка на HSL", command=self.show_hsl_sliders)
        self.adjust_hsl_button.grid(row=10, column=0, pady=5)

        self.red_eye_reduction_button = tk.Button(self.button_frame, text="Червени очи",
                                                  command=self.apply_red_eye_reduction)
        self.red_eye_reduction_button.grid(row=10, column=1, pady=5)

        self.straighten_image_button = tk.Button(self.button_frame, text="Изправяне",
                                                 command=self.get_straighten_angle)
        self.straighten_image_button.grid(row=11, column=0, pady=5)

        self.noise_reduction_button = tk.Button(self.button_frame, text="Намали шума",
                                                command=self.apply_noise_reduction)
        self.noise_reduction_button.grid(row=11, column=1, pady=5)

        self.undo_button = tk.Button(self.button_frame, text="Назад", command=self.undo)
        self.undo_button.grid(row=12, column=0, pady=5)

        self.redo_button = tk.Button(self.button_frame, text="Напред", command=self.redo)
        self.redo_button.grid(row=12, column=1, pady=5)

        #Desni butoni
        self.right_button_frame = tk.Frame(self)
        self.right_button_frame.pack(side=tk.RIGHT, padx=5, fill=tk.Y)

        self.filter_functions = {
            "Размазване": apply_filter_blur,
            "Изостране": apply_filter_sharpen,
            "Намерете ръбове": apply_filter_edges,
            "Релеф": apply_filter_emboss,
            "Контур": apply_filter_contour,
            "Скала на сивото": apply_filter_greyscale,
        }

        self.selected_filter = tk.StringVar(self.right_button_frame)
        self.selected_filter.set("Избери филтър")

        self.filter_menu = tk.OptionMenu(self.right_button_frame, self.selected_filter, *self.filter_functions.keys())
        self.filter_menu.config(width=20, height=1)
        self.filter_menu.pack(side=tk.TOP, pady=5)

        self.apply_filter_button = tk.Button(self.right_button_frame, text="Приложи филтър",
                                             command=self.apply_selected_filter)
        self.apply_filter_button.pack(side=tk.TOP, pady=5)

        self.apply_vignette_button = tk.Button(self.right_button_frame, text="Винетен ефект", command=self.apply_vignette)
        self.apply_vignette_button.pack(side=tk.TOP, pady=5)

        for index, image_path in enumerate(self.image_list):
            thumbnail = self.create_thumbnail(image_path, fixed_width=100)
            thumbnail_label = tk.Label(self.inner_thumbnail_frame, image=thumbnail, cursor="hand2")
            thumbnail_label.image = thumbnail
            thumbnail_label.bind('<Button-1>', lambda event, idx=index: self.select_image(event, idx))
            thumbnail_label.pack(side=tk.TOP, pady=0)



        #Osnovnoto izobrajenie!
        self.image_label = tk.Label(self, image=None)
        self.image_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES, pady=0, padx=0)

        self.red_title = tk.Label(self.right_button_frame, text="Червен баланс")
        self.red_title.pack(side=tk.TOP, pady=2)
        self.red_scale = tk.Scale(self.right_button_frame, from_=0.5, to=1.5, resolution=0.01,
                                  orient=tk.HORIZONTAL,
                                  command=lambda value: self.adjust_color_balance(float(value), self.green_scale.get(),
                                                                                  self.blue_scale.get()), length=300)
        self.red_scale.set(1)
        self.red_scale.pack(side=tk.TOP, pady=5)

        self.green_title = tk.Label(self.right_button_frame, text="Зелен баланс")
        self.green_title.pack(side=tk.TOP, pady=2)
        self.green_scale = tk.Scale(self.right_button_frame, from_=0.5, to=1.5, resolution=0.01,
                                    orient=tk.HORIZONTAL,
                                    command=lambda value: self.adjust_color_balance(self.red_scale.get(), float(value),
                                                                                    self.blue_scale.get()), length=300)
        self.green_scale.set(1)
        self.green_scale.pack(side=tk.TOP, pady=5)

        self.blue_title = tk.Label(self.right_button_frame, text="Син баланс")
        self.blue_title.pack(side=tk.TOP, pady=2)
        self.blue_scale = tk.Scale(self.right_button_frame, from_=0.5, to=1.5, resolution=0.01,
                                   orient=tk.HORIZONTAL,
                                   command=lambda value: self.adjust_color_balance(self.red_scale.get(),
                                                                                   self.green_scale.get(),
                                                                                   float(value)), length=300)
        self.blue_scale.set(1)
        self.blue_scale.pack(side=tk.TOP, pady=5)

        self.saturation_title = tk.Label(self.right_button_frame, text="Наситеност")
        self.saturation_title.pack(side=tk.TOP, pady=2)
        self.saturation_scale = tk.Scale(self.right_button_frame, from_=0, to=2, resolution=0.01,
                                         orient=tk.HORIZONTAL, command=self.adjust_saturation, length=300)
        self.saturation_scale.set(1)
        self.saturation_scale.pack(side=tk.TOP, pady=5)

        #Ostanalite desni butoni
        self.save_button = tk.Button(self.right_button_frame, text="Запази", command=self.save_image)
        self.save_button.pack(side=tk.TOP, pady=5)

        self.delete_button = tk.Button(self.right_button_frame, text="Изтрий", command=self.delete_image)
        self.delete_button.pack(side=tk.TOP, pady=5)

        self.reset_button = tk.Button(self.right_button_frame, text="Възстанови", command=self.reset_image)
        self.reset_button.pack(side=tk.TOP, pady=5)

        self.info_button = tk.Button(self.right_button_frame, text="Информация", command=self.show_image_info)
        self.info_button.pack(side=tk.TOP, pady=5)

        self.exit_button = tk.Button(self.right_button_frame, text="Изход", command=self.quit_app)
        self.exit_button.pack(side=tk.TOP, pady=5)

        #Конфигурация на бутоните
        self.reset_button.config(**button_styles)
        self.apply_vignette_button.config(**button_styles)
        self.info_button.config(**button_styles)
        self.rotate_button.config(**button_styles)
        self.rotate_counter_clockwise.config(**button_styles)
        self.flip_horizontal_button.config(**button_styles)
        self.flip_vertical_button.config(**button_styles)
        self.apply_filter_button.config(**button_styles)
        self.open_button.config(**button_styles)
        self.save_button.config(**button_styles)
        self.delete_button.config(**button_styles)
        self.crop_button.config(**button_styles)
        self.zoom_in_button.config(**button_styles)
        self.zoom_out_button.config(**button_styles)
        self.undo_button.config(**button_styles)
        self.redo_button.config(**button_styles)
        self.increase_brightness_button.config(**button_styles)
        self.decrease_brightness_button.config(**button_styles)
        self.increase_contrast_button.config(**button_styles)
        self.decrease_contrast_button.config(**button_styles)
        self.noise_reduction_button.config(**button_styles)
        self.invert_colors_button.config(**button_styles)
        self.add_text_button.config(**button_styles)
        self.histogram_button.config(**button_styles)
        self.blend_button.config(**button_styles)
        self.adjust_opacity.config(**button_styles)
        self.auto_enhance_button.config(**button_styles)
        self.adjust_hsl_button.config(**button_styles)
        self.red_eye_reduction_button.config(**button_styles)
        self.straighten_image_button.config(**button_styles)
        self.exit_button.config(**button_styles)



    def create_thumbnail(self, image_path, fixed_width=100):
        img = Image.open(image_path)
        aspect_ratio = img.height / img.width
        new_height = int(fixed_width * aspect_ratio)
        img = img.resize((fixed_width, new_height), Image.ANTIALIAS)
        thumbnail = ImageTk.PhotoImage(img)
        return thumbnail

    def update_image(self, new_image=None):
        if new_image is not None:
            self.current_image = new_image

        self.tk_image = ImageTk.PhotoImage(self.current_image)
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image

    def select_image(self, event, index):
        self.current_index = index
        self.load_image()

    def load_image(self):
        image_path = self.image_list[self.current_index]
        self.current_image = Image.open(image_path)

        #fiksirana shirina na izobrajenieto
        fixed_width = 500
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
        self.push_to_undo()
        self.current_image = self.current_image.rotate(90)
        self.update_image()

    def rotate_counter_clockwise(self):
        self.push_to_undo()
        self.current_image = self.current_image.rotate(-90)
        self.update_image()

    def flip_image_horizontal(self):
        self.push_to_undo()
        self.current_image = self.current_image.transpose(Image.FLIP_LEFT_RIGHT)
        self.update_image()

    def flip_image_vertical(self):
        self.push_to_undo()
        self.current_image = self.current_image.transpose(Image.FLIP_TOP_BOTTOM)
        self.update_image()

    def auto_enhance(self, image: Image.Image) -> Image.Image:
        self.push_to_undo()
        if image.mode != 'RGB':
            image = image.convert('RGB')
        return ImageOps.autocontrast(image, cutoff=0, ignore=None)

    def apply_auto_enhance(self):
        self.push_to_undo()
        self.current_image = self.auto_enhance(self.current_image)
        self.update_image()




    def reset_image(self):
        self.update_image()
        self.load_image()
        self.red_scale.set(1)
        self.green_scale.set(1)
        self.blue_scale.set(1)
        self.saturation_scale.set(1)

    def apply_selected_filter(self):
        self.push_to_undo()
        filter_name = self.selected_filter.get()

        if filter_name in self.filter_functions:
            self.current_image = self.filter_functions[filter_name](self.current_image)
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
            self.refresh_thumbnail_list()

    def clear_thumbnail_list(self):
        for child in self.inner_thumbnail_frame.winfo_children():
            child.destroy()

    def refresh_thumbnail_list(self):
        self.clear_thumbnail_list()
        self.image_list = load_images_from_directory(img_folder='img')

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
            # Kopirane na izbraniq ot img papkata
            file_name = os.path.basename(file_path)
            img_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
            new_file_path = os.path.join(img_directory, file_name)
            shutil.copy(file_path, new_file_path)

            # dobaivane na noviq put do kopiranoto izobrajenie
            self.image_list.append(new_file_path)
            self.current_index = len(self.image_list) - 1
            self.load_image()

            # refreshvane na thumbnaila
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

        # refreshvane na thumbnaila
        self.refresh_thumbnail_list()

        # Update na tekushtiq index i zarejdane na sledvashtoto izobrajenie
        self.current_index = min(self.current_index, len(self.image_list) - 1)
        if self.image_list:
            self.load_image()
        else:
            self.label.config(image="")

    def start_crop(self, event):
        if self.crop_rectangle:
            self.crop_canvas.delete(self.crop_rectangle)
        self.crop_start_x = event.x
        self.crop_start_y = event.y

    def draw_crop_rectangle(self, event):
        if self.crop_rectangle:
            self.crop_canvas.delete(self.crop_rectangle)
        x1, y1, x2, y2 = self.crop_start_x, self.crop_start_y, event.x, event.y
        self.crop_rectangle = self.crop_canvas.create_rectangle(x1, y1, x2, y2, outline='red')

    def end_crop(self, event):
        x1, y1, x2, y2 = self.crop_start_x, self.crop_start_y, event.x, event.y

        canvas_width = self.crop_canvas.winfo_width()
        canvas_height = self.crop_canvas.winfo_height()
        image_width, image_height = self.current_image.size
        center_x = (canvas_width - image_width) // 2
        center_y = (canvas_height - image_height) // 2

        adjusted_x1 = x1 - center_x
        adjusted_y1 = y1 - center_y
        adjusted_x2 = x2 - center_x
        adjusted_y2 = y2 - center_y

        self.crop_coordinates = (adjusted_x1, adjusted_y1, adjusted_x2, adjusted_y2)
        self.crop_image()

    def crop_image(self):
        self.push_to_undo()
        if self.crop_coordinates:
            x1, y1, x2, y2 = self.crop_coordinates
            self.current_image = self.current_image.crop((x1, y1, x2, y2))
            self.update_image()
            self.crop_coordinates = None
            self.crop_canvas.delete(self.crop_rectangle)
            self.crop_rectangle = None

            self.crop_canvas.update()
            canvas_width = self.crop_canvas.winfo_width()
            canvas_height = self.crop_canvas.winfo_height()
            image_width, image_height = self.current_image.size
            center_x = (canvas_width - image_width) // 2
            center_y = (canvas_height - image_height) // 2

            self.crop_canvas.create_image(center_x, center_y, image=self.image_label.cget("image"), anchor='nw')

    def enable_crop_mode(self):
        if not self.image_list:
            messagebox.showwarning("Внимание", "Няма изображения за изрязване.")
            return

        if self.crop_button['text'] == "Изрежи":
            self.crop_button.config(text="Изход")
            self.crop_canvas = tk.Canvas(self.image_label, width=self.image_label.winfo_width(),
                                         height=self.image_label.winfo_height(), bd=0, highlightthickness=0)
            self.crop_canvas.pack(fill=tk.BOTH, expand=tk.YES)

            self.crop_canvas.update()
            canvas_width = self.crop_canvas.winfo_width()
            canvas_height = self.crop_canvas.winfo_height()
            image_width, image_height = self.current_image.size
            center_x = (canvas_width - image_width) // 2
            center_y = (canvas_height - image_height) // 2

            self.crop_canvas.create_image(center_x, center_y, image=self.image_label.cget("image"), anchor='nw')
            self.crop_canvas.bind("<ButtonPress-1>", self.start_crop)
            self.crop_canvas.bind("<B1-Motion>", self.draw_crop_rectangle)
            self.crop_canvas.bind("<ButtonRelease-1>", self.end_crop)
        else:
            self.crop_button.config(text="Изрежи")
            self.crop_canvas.unbind("<ButtonPress-1>")
            self.crop_canvas.unbind("<B1-Motion>")
            self.crop_canvas.unbind("<ButtonRelease-1>")
            self.crop_canvas.destroy()
            self.crop_canvas = None

    def zoom_image(self, scale_factor):
        self.push_to_undo()
        width, height = self.current_image.size
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        self.current_image = self.current_image.resize((new_width, new_height), Image.ANTIALIAS)
        self.update_image()

    def zoom_in(self):
        self.zoom_image(1.25)

    def zoom_out(self):
        self.zoom_image(0.8)

    def increase_brightness(self):
        self.push_to_undo()
        enhancer = ImageEnhance.Brightness(self.current_image)
        self.current_image = enhancer.enhance(1.1)  # Uvelichava osvetlenieto s 10%
        self.update_image()

    def decrease_brightness(self):
        self.push_to_undo()
        enhancer = ImageEnhance.Brightness(self.current_image)
        self.current_image = enhancer.enhance(0.9)  # Namali osvetlenieto s 10%
        self.update_image()

    def increase_contrast(self):
        self.push_to_undo()
        enhancer = ImageEnhance.Contrast(self.current_image)
        self.current_image = enhancer.enhance(1.1)  # Uvelichava kontrasta s 10%
        self.update_image()

    def decrease_contrast(self):
        self.push_to_undo()
        enhancer = ImageEnhance.Contrast(self.current_image)
        self.current_image = enhancer.enhance(0.9)  # Namali kontrasta s 10%
        self.update_image()

    def push_to_undo(self):
        self.undo_stack.append(self.current_image.copy())
        self.redo_stack.clear()

    def undo(self):
        if len(self.undo_stack) > 0:
            last_action = self.undo_stack.pop()
            self.redo_stack.append(self.current_image)
            self.current_image = last_action
            self.update_image()

    def redo(self):
        if len(self.redo_stack) > 0:
            next_action = self.redo_stack.pop()
            self.undo_stack.append(self.current_image)
            self.current_image = next_action
            self.update_image()

    def adjust_color_balance(self, r, g, b):
        self.push_to_undo()
        if self.current_image:
            image = self.current_image.convert('RGBA')
            red, green, blue, alpha = image.split()

            red = ImageEnhance.Brightness(red).enhance(r)
            green = ImageEnhance.Brightness(green).enhance(g)
            blue = ImageEnhance.Brightness(blue).enhance(b)

            self.current_image = Image.merge('RGBA', (red, green, blue, alpha))
            self.update_image()

    def adjust_saturation(self, value):
        self.push_to_undo()
        if self.current_image:
            enhancer = ImageEnhance.Color(self.current_image)
            self.current_image = enhancer.enhance(float(value))
            self.update_image()

    def apply_noise_reduction(self):
        self.push_to_undo()
        self.current_image = self.current_image.filter(ImageFilter.MedianFilter(size=3))
        self.update_image()

    def invert_colors(self):
        self.push_to_undo()
        if self.current_image is None:
            return

        # Konvertirai kum RGB format, ako e v drug format
        if self.current_image.mode != 'RGB':
            self.current_image = self.current_image.convert('RGB')

        self.current_image = ImageOps.invert(self.current_image)
        self.update_image()

    def add_text_to_image(self):
        self.push_to_undo()
        if self.current_image is None:
            return

        dialog = tk.Toplevel(self)

        tk.Label(dialog, text="Enter the text to add to the image:").grid(row=0, column=0)
        text_entry = tk.Entry(dialog)
        text_entry.grid(row=0, column=1)

        tk.Label(dialog, text="Enter the X coordinate for the text:").grid(row=1, column=0)
        x_entry = tk.Entry(dialog)
        x_entry.grid(row=1, column=1)

        tk.Label(dialog, text="Enter the Y coordinate for the text:").grid(row=2, column=0)
        y_entry = tk.Entry(dialog)
        y_entry.grid(row=2, column=1)

        tk.Label(dialog, text="Enter the font size (max 30):").grid(row=3, column=0)
        font_size_entry = tk.Entry(dialog)
        font_size_entry.grid(row=3, column=1)

        def submit():
            text = text_entry.get()
            x_coord = int(x_entry.get())
            y_coord = int(y_entry.get())
            font_size = int(font_size_entry.get())

            if font_size > 30:
                font_size = 30

            default_font = ImageFont.load_default()
            font = ImageFont.ImageFont()

            draw = ImageDraw.Draw(self.current_image)
            draw.text((x_coord, y_coord), text, fill=(255, 255, 255))

            self.update_image()
            dialog.destroy()

        submit_button = tk.Button(dialog, text="Submit", command=submit)
        submit_button.grid(row=4, columnspan=2)

        dialog.mainloop()

    def show_image_histogram(self):
        self.push_to_undo()
        if self.current_image is None:
            return

        # Konvertirai kum grayscale
        gray_image = self.current_image.convert("L")
        pixel_values = gray_image.getdata()

        # Plot za histogram
        plt.hist(pixel_values, bins=256, range=(0, 256), density=True)
        plt.xlabel("Pixel Values")
        plt.ylabel("Frequency")
        plt.title("Image Histogram")
        plt.show()

    def blend_images(self):
        self.push_to_undo()
        if self.current_image is None:
            return

        second_image_path = filedialog.askopenfilename(title="Select Second Image")
        if not second_image_path:
            return

        try:
            second_image = Image.open(second_image_path)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open image: {e}")
            return

        # Upravlenie na razmera na vtorata snimka
        second_image = second_image.resize(self.current_image.size, Image.ANTIALIAS)

        # Konvertirane na vtorata snimka v RGB format
        second_image = second_image.convert(self.current_image.mode)

        alpha = simpledialog.askfloat("Blend Images", "Enter the blend factor (0.0 to 1.0):", minvalue=0.0,
                                      maxvalue=1.0)

        if alpha is None:
            return

        blended_image = Image.blend(self.current_image, second_image, alpha)

        self.undo_stack.append(self.current_image)
        self.redo_stack.clear()
        self.current_image = blended_image
        self.update_image()

    def adjust_opacity(self):
        self.push_to_undo()
        if self.current_image is None:
            return

        opacity = simpledialog.askfloat("Adjust Opacity", "Enter opacity value (0.0 to 1.0):", minvalue=0.0,
                                        maxvalue=1.0)
        if opacity is None:
            return

        # Konvertirai kum RGBA format, ako e v drug format
        if self.current_image.mode != 'RGBA':
            self.current_image = self.current_image.convert('RGBA')

        alpha_layer = Image.new('L', self.current_image.size, int(opacity * 255))
        self.current_image.putalpha(alpha_layer)
        self.update_image()

    def adjust_hsl(self, image: Image.Image, hue: int, saturation: int, lightness: int) -> Image.Image:
        self.push_to_undo()
        # Kovertirai PIL snimkata v NumPy matrica v BGR format
        image_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Konvertirai matricata v HSV format
        hsv_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)

        # Izmeni hue, saturation i lightness
        hsv_image[..., 0] = np.mod(hsv_image[..., 0] + hue, 180).astype(np.uint8)
        hsv_image[..., 1] = np.clip(hsv_image[..., 1] * (1 + saturation / 100), 0, 255).astype(np.uint8)
        hsv_image[..., 2] = np.clip(hsv_image[..., 2] * (1 + lightness / 100), 0, 255).astype(np.uint8)

        # Konvertirai snimkata v BGR format
        bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

        # Kongvertirai matricata v PIL snimka v RGB format
        return Image.fromarray(cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB))

    def show_hsl_sliders(self):
        def apply_hsl_adjustment():
            hue_value = hue_slider.get()
            saturation_value = saturation_slider.get()
            lightness_value = lightness_slider.get()

            self.push_to_undo()
            self.current_image = self.adjust_hsl(self.current_image, hue_value, saturation_value, lightness_value)
            self.update_image()

        hsl_window = tk.Toplevel(self)
        hsl_window.title("Adjust HSL")

        hue_label = tk.Label(hsl_window, text="Hue")
        hue_label.grid(row=0, column=0)
        hue_slider = tk.Scale(hsl_window, from_=-180, to=180, orient=tk.HORIZONTAL)
        hue_slider.grid(row=0, column=1)

        saturation_label = tk.Label(hsl_window, text="Saturation")
        saturation_label.grid(row=1, column=0)
        saturation_slider = tk.Scale(hsl_window, from_=-100, to=100, orient=tk.HORIZONTAL)
        saturation_slider.grid(row=1, column=1)

        lightness_label = tk.Label(hsl_window, text="Lightness")
        lightness_label.grid(row=2, column=0)
        lightness_slider = tk.Scale(hsl_window, from_=-100, to=100, orient=tk.HORIZONTAL)
        lightness_slider.grid(row=2, column=1)

        apply_button = tk.Button(hsl_window, text="Apply", command=apply_hsl_adjustment)
        apply_button.grid(row=3, column=0, columnspan=2)

    def red_eye_reduction(self, image):
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30))

        for (x, y, w, h) in eyes:
            eye = image_cv[y:y + h, x:x + w]
            b, g, r = cv2.split(eye)
            r = cv2.addWeighted(r, 1.5, g, -0.5, 0)
            eye = cv2.merge((b, g, r))
            image_cv[y:y + h, x:x + w] = eye

        return Image.fromarray(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))

    def apply_red_eye_reduction(self):
        self.push_to_undo()
        self.current_image = self.red_eye_reduction(self.current_image)
        self.update_image()

    def get_straighten_angle(self):
        self.push_to_undo()
        angle = simpledialog.askfloat("Straighten Image", "Enter the angle to rotate (in degrees):",
                                      minvalue=-360, maxvalue=360, initialvalue=0)
        if angle is not None:
            self.apply_straighten_image(angle)

    def create_vignette_mask(self, width, height, intensity):
        intensity = 255 - int(intensity * 255)
        vignette_mask = Image.new('L', (width, height), 0)
        draw = ImageDraw.Draw(vignette_mask)
        draw.ellipse((0, 0, width, height), fill=intensity)
        return vignette_mask

    def apply_vignette(self):
        self.push_to_undo()
        if self.current_image is None:
            return

        intensity = simpledialog.askfloat("Vignette Intensity", "Enter the vignette intensity (0-1):", minvalue=0,
                                          maxvalue=1)

        if intensity is None:
            return

        width, height = self.current_image.size
        vignette_mask = self.create_vignette_mask(width, height, intensity)

        # Konvertirai maskata v istiq format kato snimkata
        vignette_mask = vignette_mask.convert(self.current_image.mode)

        # Syzdai novata snimka
        vignette_image = ImageChops.multiply(self.current_image, vignette_mask)

        # Zameni snimkata
        self.update_image(new_image=vignette_image)

    def apply_straighten_image(self, angle):
        self.push_to_undo()
        self.current_image = self.straighten_image(self.current_image, angle)
        self.update_image()

    def straighten_image(self, image, angle):
        return image.rotate(angle, resample=Image.BICUBIC, expand=True)

    #exit function
    def quit_app(self):
        self.destroy()
        self.quit()

if __name__ == "__main__":
    app = ImageViewerApp()
    app.mainloop()
