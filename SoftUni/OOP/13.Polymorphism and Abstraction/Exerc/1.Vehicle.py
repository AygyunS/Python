from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.__fuel_quantity = fuel_quantity
        self.__fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_consumed = (self.__fuel_consumption + 0.9) * distance
        if fuel_consumed <= self.__fuel_quantity:
            self.__fuel_quantity -= fuel_consumed
            return True
        return False

    def refuel(self, fuel):
        self.__fuel_quantity += fuel

    @property
    def fuel_quantity(self):
        return self.__fuel_quantity


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.__fuel_quantity = fuel_quantity
        self.__fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_consumed = (self.__fuel_consumption + 1.6) * distance
        if fuel_consumed <= self.__fuel_quantity:
            self.__fuel_quantity -= fuel_consumed
            return True
        return False

    def refuel(self, fuel):
        self.__fuel_quantity += fuel * 0.95

    @property
    def fuel_quantity(self):
        return self.__fuel_quantity


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)