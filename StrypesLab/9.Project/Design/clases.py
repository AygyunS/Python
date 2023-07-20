from abc import ABC, abstractmethod
import os

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):

    def make_sound(self):
        return "Woof!"

    def move(self):
        return "The dog is running."

class Cat(Animal):

    def make_sound(self):
        return "Meow!"

    def move(self):
        return "The cat is jumping."

class Bird(Animal):

    def make_sound(self):
        return "Chirp!"

    def move(self):
        return "The bird is flying."

class AnimalFactory:

    @staticmethod
    def create_animal(animal_name):
        if animal_name == "Dog":
            return Dog()
        elif animal_name == "Cat":
            return Cat()
        elif animal_name == "Bird":
            return Bird()
        else:
            raise ValueError(f"Invalid animal name: {animal_name}")

def create_animals_from_file(filename):
    animals = []

    with open(filename, "r") as file:
        for line in file:
            animal_name = line.strip()
            animal = AnimalFactory.create_animal(animal_name)
            animals.append(animal)

    return animals


filename = "animals.txt"
animals = create_animals_from_file(filename)

for animal in animals:
    print(animal.make_sound())
    print(animal.move())
    print()
