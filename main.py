from books_db import BooksDatabase
from clients_db import ClientsDatabase
from BookClass import Book
from ClientClass import Client
import re


class Inventory:
    def __init__(self):
        self.db = BooksDatabase('books_inventory')

    def validate_isbn(self, isbn):
        return bool(re.match(
            r"^(?:ISBN(?:-1[03])?:?\ )?(?=\d{9}[\dX]|(?=(?:\d+[-\ ]){3})[-\ 0-9]{13}$)(?:97[89][-\ ]?)?\d{1,5}[-\ ]?\d{1,7}[-\ ]?\d{1,6}[-\ ]?[\dX]$",
            isbn))

    def add_book(self, book):
        if self.validate_isbn(book.isbn):
            self.db.add_book(book.title, book.author, book.isbn, book.price, book.category, book.available)
            print(
                f"{book.title} by {book.author} | ISBN: {book.isbn} | PRICE: {book.price} | CAT: {book.category} | AVAILABLE: {book.available}")
        else:
            print(f"{book.isbn} Invalid Code!")

    def remove_book(self, isbn):
        if self.validate_isbn(isbn):
            target = self.get_book_by_isbn(isbn)
            self.db.remove_book(isbn)
            print(
                f"Target Book: {target.title} by {target.author} | ISBN: {target.isbn} | AVAILABLE: {target.available} >>>>> REMOVED!")
        else:
            print(f"{isbn.isbn} Invalid Code!")

    def update_book_availability(self, isbn, available):
        target = self.get_book_by_isbn(isbn)
        self.db.update_book_availability(isbn, available)
        print(
            f"Target Book {isbn} changed availability to: {available}")

    def get_book_by_isbn(self, isbn):
        return self.db.get_book_by_isbn(isbn)


inventory = Inventory()
inventory.db.clear_books()

# Adding books
book1 = Book('The Sound and the Fury', 'Gustave Flaubert', '9781234567890', 27.00, 'Fiction')
book2 = Book('Sentimental Education', 'William Faulkner', '9781234567892', 45.00, 'Fiction')
book3 = Book('The recognition of Shakuntala', 'Kālidāsa', '9781234567893', 39.00, 'Fiction')
book4 = Book('Memoirs of Hadrian', 'Marguerite Yourcenar', '9781234567894', 32.00, 'Fiction')
book5 = Book('Middlemarch', 'George Eliot', '9781234567895', 21.00, 'Fiction')

inventory.add_book(book1)
inventory.add_book(book2)
inventory.add_book(book3)
inventory.add_book(book4)
inventory.add_book(book5)

inventory.update_book_availability('9781234567890', 0)


class Users:
    def __init__(self):
        self.db = ClientsDatabase('clients')

    def add_client(self, client):
        self.db.add_client(client)
        print(
            f">ADDED: {client.name} | EMAIL: {client.email} | ID: {client.clientID} | CAN RENT: {client.canRent} | PENALTIES:{client.penalties} | signed: {client.dateCreated}")

    def get_clients(self):
        return self.db.get_clients()

    def get_client_by_code(self, id):
        return self.db.get_client_by_code(id)

    def update_client_penalty(self, id, penalty):
        print(f"Updated user {id} with {penalty} penalty.")
        self.db.update_client_penalty(id, penalty)

    def delete_client(self, id):
        self.db.delete_client(id)


client1 = Client('Gheorghe', 'gheorghe@gmail.com', '1')
client2 = Client('Simona', 'simona@gmail.com', '5')
client3 = Client('Liviu', 'liviu@gmail.com', '9')

users = Users()
users.db.clear_clients()

users.add_client(client1)
users.add_client(client2)
users.add_client(client3)

users.update_client_penalty('5', 3)
print(users.get_client_by_code('5'))
users.update_client_penalty('5', 0)
print(users.delete_client('1'))
print(users.get_clients())