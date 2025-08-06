class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author 
        self.year = year

    def get_info(self):
        print(f"{self.title} by {self.author}, published in {self.year}")
my_book = Book("Human", "Gabriel Marsel", 1951)
print(my_book.get_info())