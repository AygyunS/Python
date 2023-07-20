class Beverage:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Coffee(Beverage):
    def __init__(self):
        super().__init__("Coffee", 2.0)


class Decaf(Beverage):
    def __init__(self):
        super().__init__("Decaf", 1.5)


class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage
        super().__init__(beverage.description, beverage.cost)

    def get_description(self):
        return self.beverage.get_description()

    def get_cost(self):
        return self.beverage.get_cost()


class Cream(BeverageDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
        self.description = "Cream"
        self.cost = 0.5

    def get_description(self):
        return self.beverage.get_description() + ", " + self.description

    def get_cost(self):
        return self.beverage.get_cost() + self.cost


class VeganCream(Cream):
    def __init__(self, beverage):
        super().__init__(beverage)
        self.description = "Vegan Cream"
        self.cost = 0.7


class Cinnamon(BeverageDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)
        self.description = "Cinnamon"
        self.cost = 0.3

    def get_description(self):
        return self.beverage.get_description() + ", " + self.description

    def get_cost(self):
        return self.beverage.get_cost() + self.cost



beverage = Coffee()
beverage = Cream(beverage)
beverage = Cinnamon(beverage)
print(beverage.get_description())
print(beverage.get_cost())
