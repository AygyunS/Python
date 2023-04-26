from abc import ABC, abstractmethod


class Booth(ABC):
    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int):
        if capacity < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self._capacity = capacity

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass
