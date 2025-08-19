from abc import ABC, abstractmethod

class Animal(ABC):
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def make_sound(self):
        print("Haw-Haw")

cat = Cat()
dog = Dog()

cat.make_sound()
dog.make_sound()