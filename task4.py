class Cat:
    def __init__(self, name, age, breed, color):
      self.name = name 
      self.age = age 
      self.breed = breed 
      self.color = color 

    def meow(self):
        print(f"Meow! Menim adim {self.name}")

    def eat(self):
        print(f"{self.name} yemek yeyir")

    def play(self):
        print(f"{self.name} oynayir")

#Obyektler yaradilir: 
lisa = Cat ("Lisa", 1, "Persian", "Grey")
lila = Cat("Lila", 2, "Maine Coon", "White")

#Metodlardan istifade olunur:
lisa.meow()
lila.eat()
lila.play()