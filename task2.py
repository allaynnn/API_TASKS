class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"Engine started for {self.brand} {self.model}")

#istifade
my_car = Car("Mercedess", "Benz", 2021)
my_car.start_engine()    
