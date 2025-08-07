class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} ses cixarir")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} ses cixarir: HAV-HAV")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} ses cixarir: MIYAW ")

dog = Dog("Lusi")
cat = Cat("Lisa")

dog.speak()
cat.speak()