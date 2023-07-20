from collection import Collection, Item


def menu() -> None:
    print("Menu:")
    print("1. Add item")
    print("2. Delete item")
    print("3. Update item")
    print("4. Search items")
    print("5. Exit")


def add_item(collection: Collection) -> None:
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")
    genre = input("Enter genre: ")
    rating = input("Enter rating: ")
    item = Item(title, author, year, genre, rating)
    collection.add_item(item)
    print("Item added successfully.")


def delete_item(collection: Collection) -> None:
    title = input("Enter title of item to delete: ")
    results = collection.search_items(title)
    if len(results) == 0:
        print("Item not found.")
    elif len(results) == 1:
        collection.delete_item(results[0])
        print("Item deleted successfully.")
    else:
        print(f"{len(results)} items found.")
        for i, item in enumerate(results):
            print(f"{i+1}. {item.title} ({item.author})")
        choice = int(input("Enter number of item to delete: "))
        if choice < 1 or choice > len(results):
            print("Invalid choice.")
        else:
            collection.delete_item(results[choice-1])
            print("Item deleted successfully.")


def update_item(collection: Collection) -> None:
    title = input("Enter title of item to update: ")
    results = collection.search_items(title)
    if len(results) == 0:
        print("Item not found.")
    elif len(results) == 1:
        item = results[0]
        print(f"Current item: {item.title} ({item.author})")
        new_title = input("Enter new title (leave blank to keep current): ")
        if new_title == "":
            new_title = item.title
        new_author = input("Enter new author (leave blank to keep current): ")
        if new_author == "":
            new_author = item.author
        new_year = input("Enter new year (leave blank to keep current): ")
        if new_year == "":
            new_year = item.year
        new_genre = input("Enter new genre (leave blank to keep current): ")
        if new_genre == "":
            new_genre = item.genre
        new_rating = input("Enter new rating (leave blank to keep current): ")
        if new_rating == "":
            new_rating = item.rating
        collection.update_item(item, new_title, new_author, new_year, new_genre, new_rating)
        print("Item updated successfully.")
    else:
        print(f"{len(results)} items found.")
        for i, item in enumerate(results):
            print(f"{i+1}. {item.title} ({item.author})")
        choice = int(input("Enter number of item to update: "))
        if choice < 1 or choice > len(results):
            print("Invalid choice.")
        else:
            item = results[choice-1]
            print(f"Current item: {item.title} ({item.author})")
            new_title = input("Enter new title (leave blank to keep current): ")
            if new_title == "":
                new_title = item.title
            new_author = input("Enter new author (leave blank to keep current): ")
            if new_author == "":
                new_author = item.author
            new_year = input("Enter new year (leave blank to keep current): ")
            if new_year == "":
                new_year = item.year
            new_genre = input("Enter new genre (leave blank to keep current): ")
            if new_genre == "":
                new_genre = item.genre
            new_rating = input("Enter new rating (leave blank to keep current): ")
            if new_rating == "":
                new_rating = item.rating
            collection.update_item(item, new_title, new_author, new_year, new_genre, new_rating)
            print("Item updated successfully.")


def search_items(collection: Collection) -> None:
    keyword = input("Enter keyword to search for: ")
    results = collection.search_items(keyword)
    if len(results) == 0:
        print("No items found.")
    else:
        print(f"{len(results)} items found.")
        for item in results:
            print(f"{item.title} ({item.author}) - {item.year}, {item.genre}, {item.rating}")



