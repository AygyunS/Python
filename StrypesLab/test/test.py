import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import requests
import random


class MoviePoster(tk.Label):
    def __init__(self, parent, movie_data, width, height, click_callback):
        self.movie_data = movie_data
        self.click_callback = click_callback
        image = self.get_movie_image(movie_data['poster_path'], width, height)
        self.photo = ImageTk.PhotoImage(image)
        super().__init__(parent, image=self.photo, bg="white", borderwidth=2, relief="raised")
        self.bind("<Button-1>", self.on_click)
        self.is_selected = False

    def get_movie_image(self, poster_path, width, height):
        base_url = 'https://image.tmdb.org/t/p/w500'
        response = requests.get(base_url + poster_path)
        image = Image.open(BytesIO(response.content))
        image.thumbnail((width, height))
        return image

    def on_click(self, event):
        self.click_callback(self)

    def select(self):
        self.is_selected = True
        self.config(bg="blue")

    def deselect(self):
        self.is_selected = False
        self.config(bg="white")



class MovieApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.root = tk.Tk()
        self.root.title('Movie Recommendations')
        self.root.geometry('1400x800')

        self.create_menu()
        self.create_widgets()

        self.root.mainloop()

    def create_menu(self):
        self.menu_frame = tk.Frame(self.root, width=200)
        self.menu_frame.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky='ns')

        home_button = tk.Button(self.menu_frame, text="Home", command=self.show_home)
        home_button.pack(fill=tk.X)

        popular_button = tk.Button(self.menu_frame, text="Popular Recommendations", command=self.change_movies)
        popular_button.pack(fill=tk.X)

        imdb_button = tk.Button(self.menu_frame, text="IMDB Top 250", command=self.show_imdb_top250)
        imdb_button.pack(fill=tk.X)

        self.info_label = tk.Label(self.menu_frame, wraplength=180, justify=tk.LEFT)
        self.info_label.pack(pady=(10, 0))

    def show_home(self):
        self.info_label.config(text="Welcome to the Movie Recommendation App! Here you can find popular movies, and get recommendations based on your preferences.")

    def show_imdb_top250(self):
        imdb_top250_movies = self.get_imdb_top250_movies()
        self.display_movies(imdb_top250_movies)

    def get_imdb_top250_movies(self, count=10):
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&sort_by=vote_average.desc&vote_count.gte=10000'
        response = requests.get(url)
        data = response.json()
        imdb_top250_movies = data['results']
        return imdb_top250_movies[:count]

    def get_movie_data(self, movie_id):
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data

    def get_movie_image(self, poster_path):
        base_url = 'https://image.tmdb.org/t/p/w500'
        response = requests.get(base_url + poster_path)
        return Image.open(BytesIO(response.content))

    def get_movie_recommendations(self, movie_id, language='en-US', page=1):
        url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={self.api_key}&language={language}&page={page}'
        response = requests.get(url)
        data = response.json()
        return data['results']

    def show_recommendations(self):
        selected_movie_ids = [poster.movie_data['id'] for poster in self.selected_movie_posters]
        recommended_movie_ids = set()
        for movie_id in selected_movie_ids:
            recommended_movies = self.get_movie_recommendations(movie_id)
            for movie in recommended_movies:
                recommended_movie_ids.add(movie['id'])

        recommended_movie_ids = list(recommended_movie_ids)
        self.display_movies(recommended_movie_ids[:10])

    def display_movies(self, movie_list):
        for widget in self.recommendation_frame.winfo_children():
            widget.destroy()

        for index, movie_data in enumerate(movie_list):
            movie_info = f"{movie_data['title']} ({movie_data['release_date'][:4]})"
            info_label = tk.Label(self.recommendation_frame, text=movie_info, wraplength=120)
            info_label.grid(row=0, column=index, padx=(10, 0))

            poster_path = movie_data['poster_path']
            if poster_path:
                image = self.get_movie_image(poster_path)
                image.thumbnail((120, 180))
                photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(self.recommendation_frame, image=photo)
                image_label.image = photo
                image_label.grid(row=1, column=index, padx=(0, 10))

    def get_random_popular_movies(self, count=10):
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&sort_by=popularity.desc'
        response = requests.get(url)
        data = response.json()
        popular_movies = data['results']
        return random.sample(popular_movies, count)

    def change_movies(self):
        random_popular_movies = self.get_random_popular_movies()
        self.display_movies(random_popular_movies)

    def on_movie_poster_click(self, movie_poster):
        if movie_poster in self.selected_movie_posters:
            movie_poster.deselect()
            self.selected_movie_posters.remove(movie_poster)
        else:
            if len(self.selected_movie_posters) >= 3:
                movie_poster_to_remove = self.selected_movie_posters.pop()
                movie_poster_to_remove.deselect()
            movie_poster.select()
            self.selected_movie_posters.add(movie_poster)

    def create_widgets(self):
        random_popular_movies = self.get_random_popular_movies()

        movie_posters_frame = tk.Frame(self.root)
        movie_posters_frame.grid(row=0, column=1, padx=(10, 0), pady=10, sticky='nsew')

        movie_posters_canvas = tk.Canvas(movie_posters_frame, width=800, height=400)
        movie_posters_scrollbar = tk.Scrollbar(movie_posters_frame, orient='vertical',
                                               command=movie_posters_canvas.yview)
        movie_posters_scrollable_frame = tk.Frame(movie_posters_canvas)

        movie_posters_scrollable_frame.bind(
            '<Configure>',
            lambda e: movie_posters_canvas.configure(scrollregion=movie_posters_canvas.bbox('all'))
        )
        movie_posters_canvas.create_window((0, 0), window=movie_posters_scrollable_frame, anchor='nw')
        movie_posters_canvas.configure(yscrollcommand=movie_posters_scrollbar.set)

        movie_posters_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        movie_posters_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        posters_per_row = 5
        for index, movie_data in enumerate(random_popular_movies):
            row = index // posters_per_row
            col = index % posters_per_row
            movie_poster = MoviePoster(movie_posters_scrollable_frame, movie_data, 120, 180,
                                       click_callback=self.on_movie_poster_click)
            movie_poster.grid(row=row, column=col, padx=(10, 0), pady=(10, 0))

        recommendation_button = tk.Button(self.root, text='Show Recommendations', command=self.show_recommendations)
        recommendation_button.grid(row=1, column=1, pady=(0, 10))

        self.recommendation_frame = tk.Frame(self.root)
        self.recommendation_frame.grid(row=2, column=1, sticky='nsew')




# Replace 'your_api_key' with your actual API key
API_KEY = '609834a5198ca5e58bdf56df2eb285ee'
app = MovieApp(API_KEY)
