class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    get_name = lambda self: self.__name
    get_age = lambda self: self.__age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())

