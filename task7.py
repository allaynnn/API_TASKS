class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 
            print (f"{amount} AZN  elave edildi. Balans: {self.__balance} AZN")
        else:
            print("Xeta: Kifayet qeder balans yoxdur.")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Xeta: Kifayet qeder balans yoxdur")
        elif amount <= 0:
            print("Xeta: Mebleg musbet olmalidir")
        else:
            self.__balance -= amount
            print(f"{amount} AZN cixarildi. Balans: {self.__balance} AZN") 
    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
account.withdraw(50)
print("Balans:", account.get_balance())

                  
