from item import Item

class Collection:
    def __init__(self, name, filename, items=None):
        self.name = name
        self.filename = filename
        self.items = items or []
        self.load_from_file()

    def load_from_file(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                fields = line.strip().split(',')
                item = Item(fields[0], fields[1], int(fields[2]), fields[3], float(fields[4]))
                self.items.append(item)

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            for item in self.items:
                line = f"{item.title},{item.author},{item.year},{item.genre},{item.rating}\n"
                file.write(line)
