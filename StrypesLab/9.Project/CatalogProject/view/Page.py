class Item:
    def __init__(self, title, release_year, description):
        self.title = title
        self.release_year = release_year
        self.description = description

class Movie(Item):
    def __init__(self, title, release_year, description, director, duration):
        super().__init__(title, release_year, description)
        self.director = director
        self.duration = duration

class Game(Item):
    def __init__(self, title, release_year, description, developer, platform):
        super().__init__(title, release_year, description)
        self.developer = developer
        self.platform = platform

class Book(Item):
    def __init__(self, title, release_year, description, author, pages):
        super().__init__(title, release_year, description)
        self.author = author
        self.pages = pages


class CollectionManager:
    def __init__(self, items=None):
        self.items = items if items else []

    def add_item(self, item):
        self.items.append(item)

    def update_item(self, index, item):
        self.items[index] = item

    def delete_item(self, index):
        del self.items[index]

    def search_items(self, query):
        results = []
        for item in self.items:
            if query.lower() in item.title.lower():
                results.append(item)
        return results

