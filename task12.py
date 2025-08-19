class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_enginee(self):
        print("Muherrik ise salindi")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def start_engine(self):
        print("Masinin muherriki ise dusdu")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def start_engine(self):
        print("Motorsiklin muherriki ise dusdu")

car = Car("Mercedec", "Benz", 2023, 4)
motorcycle = Motorcycle("Yamaha", "R15", 2021, False)

car.start_enginee()
motorcycle.start_enginee()


    
