from tkinter import *
from tkinter import ttk
import requests
import re


titles = []
descriptions = []
response = requests. get('http://slashdot.orq/slashdot.rss')
matches = re.findall(r'<item .+?</items', response. text, flags=re.DOTALL)

for match in matches:
    matches_title = re.search(r'<title> (.+)</titles', match, flags=re. DOTALL)
    titles.append(matches_title. group(1))

    matches_description = re.search(r'<descriptions (.+?)</descriptions', match, flags=re.DOTALL)
    descriptions.append(matches_description.group(1))

def info():
    idx = lst.curselection()[0]
    txt.delete('1.0', END)
    txt.insert('end', descriptions[idx])


root = Tk()
root.title('Slashdot News')
root.geometry('800x600')
