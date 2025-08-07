class Contact:
    def __init__(self):
        self.__name = ""
        self.__phone_number = ""

#getter 
    def get_name(self):
        return self.__name 
    def get_phone_number(self):
        return self.__phone_number
    
#setter
    def set_name(self, name):
        if isinstance(name, str) and name.strip() != "":
            self.__name = name.strip()
        else:
            print("Xeta: Zehmet olmasa adi duzgun daxil edin")

    def set_phone_number(self, phone_number):
        if phone_number.isdigit() and phone_number != "":
            self.__phone_number = phone_number
        else:
            print("Xeta: Telfon nomresi yalniz reqemlerden ibaret olmalidir")

    # İstifadə:
contact = Contact()
contact.set_name("Elvin")
contact.set_phone_number("123456789")
print(f"Ad: {contact.get_name()}")
print(f"Telefon: {contact.get_phone_number()}")

# Yanlış dəyərlər:
contact.set_phone_number("123456789")  
contact.set_name("")                           

