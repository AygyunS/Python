from project.product import Product


class Drink(Product):
    quantity = 10

    def __init__(self, name: str):
        super().__init__(name, self.quantity)

    def __repr__(self):
        return f'{self.name}'
