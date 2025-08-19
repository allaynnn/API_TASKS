from abc import ABC, abstractmethod

class Payment(ABC):
    def pay(self, amount):
      pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class BankTransferPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using BankTransferPayment")   

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

