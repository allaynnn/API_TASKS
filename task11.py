class Employe:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} isleyir")

class Manager(Employe):
    def work(self):
        print(f"{self.name} isleyir")

class Developer(Employe):
    def work(self):
        print(f"{self.name} isleyir")

manager = Manager("Manager layiheni idare edir")
developer = Developer("Proqramci kod yazir")