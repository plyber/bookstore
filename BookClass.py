class Book:
    def __init__(self, title, author, isbn, price, category, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.category = category
        self.stock = available

    def __str__(self):
        return f"Book(Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: {self.price}, Category: {self.category}, Available: {self.stock})"