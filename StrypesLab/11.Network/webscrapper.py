import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk


# Function to fetch articles and titles
def fetch_articles():
    url = "https://slashdot.org"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="fhitem fhitem-story article usermode thumbs grid_24")

    data = []
    for article in articles:
        title = article.find("span", class_="story-title").get_text(strip=True)
        article_text = article.find("div", class_="p").get_text(strip=True)
        data.append((title, article_text))

    return data


# Function to show article in the text widget
def display_article():
    index = title_listbox.curselection()[0]
    article_text.delete(1.0, tk.END)
    article_text.insert(tk.END, articles[index][1])


# Create the main window
root = tk.Tk()
root.title("Slashdot Web Scraper")
root.geometry("800x600")

# Create listbox to display titles
title_listbox = tk.Listbox(root, width=80, height=20)
title_listbox.grid(row=0, column=0, padx=10, pady=10)

# Create a scrollbar for the listbox
scrollbar = ttk.Scrollbar(root, orient="vertical", command=title_listbox.yview)
scrollbar.grid(row=0, column=1, pady=10, sticky="ns")
title_listbox.configure(yscrollcommand=scrollbar.set)

# Create text widget to display article
article_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
article_text.grid(row=0, column=2, padx=10, pady=10)

# Fetch articles and titles
articles = fetch_articles()
for title, _ in articles:
    title_listbox.insert(tk.END, title)

# Bind listbox selection to the display_article function
title_listbox.bind("<<ListboxSelect>>", lambda _: display_article())

root.mainloop()
