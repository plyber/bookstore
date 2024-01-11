class Book:
    def __init__(self, title, author, isbn, price, category, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.category = category
        self.available = available

    def decrement_quantity(self):
        if self.available > 0:
            self.available -= 1
            return self.available
        else:
            print("Out of stock!")

    def add_quantity(self,value):
        self.available+=value
        return self.available

    def __str__(self):
        return f"Book(Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: {self.price}, Category: {self.category}, Available: {self.available})"
