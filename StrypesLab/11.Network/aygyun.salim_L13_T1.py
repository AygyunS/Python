import tkinter as tk
from bs4 import BeautifulSoup
from urllib.request import urlopen


class NewsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("News scraper App")
        self.geometry("900x600")

        self.listbox = tk.Listbox(self, font=("Arial", 14), width=40)
        self.listbox.grid(row=0, column=0, sticky="nsew")

        self.text = tk.Text(self, wrap=tk.WORD, font=("Arial", 14))
        self.text.grid(row=0, column=1, sticky="nsew")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        self.listbox.bind("<<ListboxSelect>>", self.on_listbox_select)

        self.articles = []
        self.load_news()

    def load_news(self):
        url = "https://slashdot.org"
        html = urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        articles = soup.find_all('article')

        for article in articles:
            title = article.find('span', class_='story-title')
            if title:
                title = title.text
            else:
                continue

            description_div = article.find('div', class_='p')
            if description_div:
                description = description_div.get_text(separator='\n', strip=True)
            else:
                description = 'No description available.'

            self.listbox.insert(tk.END, title)
            self.articles.append((title, description))

    def on_listbox_select(self, event):
        index = self.listbox.curselection()[0]
        title, description = self.articles[index]

        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, f"{title}\n\n{description}")


if __name__ == "__main__":
    app = NewsApp()
    app.mainloop()
