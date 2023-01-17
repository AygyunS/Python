class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {car.name} {car.model} with engine {car.engine}"


car = Car(input(), input(), input())
print(car.get_info())
# car = Car("W124", "Mercedes", "Petrol l4")
# print(car.get_info())
