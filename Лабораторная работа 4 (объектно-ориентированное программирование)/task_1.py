from abc import ABC, abstractmethod
from os import name


class Animal(ABC):
    def __init__(self, name, species):
        self._name = name
        self._species = species

    @abstractmethod
    def make_sound(self):
        pass

    def get_info(self):
        return f"{self._species} по имени {self._name}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Собака")
        self.__breed = breed

    def make_sound(self):
        return "Гав-гав!"

    def get_info(self):
        return f"Собака породы {self.__breed}, по имени {self._name}"


if name == "__main__":
    dog = Dog("Бобик", "Лабрадор")

    print(dog.get_info())
    print(dog.make_sound())
