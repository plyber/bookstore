class Book:
    def __init__(self, title, author, isbn, price, category):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.category = category
        self.available = 1