from books_db import BooksDatabase
from clients_db import ClientsDatabase
from reservations_db import ReservationsDatabase
from ReservationClass import Reservation
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
                f"+ADDED BOOK: '{book.title}' by {book.author} | ISBN: {book.isbn} | PRICE: {book.price} | CAT: {book.category} | AVAILABLE: {book.available}")
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
        self.db.update_book_availability(isbn, available)
        print(
            f">Target ISBN {isbn} changed availability to: {available}")

    def get_book_by_isbn(self, isbn):
        book_data = self.db.get_book_by_isbn(isbn)
        return Book(*book_data)


inventory = Inventory()
inventory.db.clear_books()

book1 = Book('The Sound and the Fury', 'Gustave Flaubert', '9781234567890', 27.00, 'Fiction', 4)
book2 = Book('Sentimental Education', 'William Faulkner', '9781234567892', 45.00, 'Fiction', 2)
book3 = Book('The recognition of Shakuntala', 'Kālidāsa', '9781234567893', 39.00, 'Fiction', 8)
book4 = Book('Memoirs of Hadrian', 'Marguerite Yourcenar', '9781234567894', 32.00, 'Fiction', 12)
book5 = Book('Middlemarch', 'George Eliot', '9781234567895', 21.00, 'Fiction', 15)

inventory.add_book(book1)
inventory.add_book(book2)
inventory.add_book(book3)
inventory.add_book(book4)
inventory.add_book(book5)

inventory.update_book_availability('9781234567890', 1)
inventory.update_book_availability('9781234567892', 52)


class Users:
    def __init__(self):
        self.db = ClientsDatabase('clients')

    def add_client(self, client):
        self.db.add_client(client)
        print(
            f"+ADDED USER: {client.name} | EMAIL: {client.email} | ID: {client.clientID} | CAN RENT: {client.canRent} | PENALTIES:{client.penalties} | signed: {client.dateCreated}")

    def get_clients(self):
        return self.db.get_clients()

    def get_client_by_code(self, id):
        client_data = self.db.get_client_by_code(id)
        return Client(*client_data)

    def update_client_penalty(self, client, penalty):
        print(f">Updated user {client.name} with {penalty} penalty.")
        self.db.update_client_penalty(client.clientID, penalty)

    def delete_client(self, id):
        self.db.delete_client(id)


client1 = Client('Gheorghe', 'gheorghe@gmail.com', 1)
client2 = Client('Simona', 'simona@gmail.com', 5)
client3 = Client('Liviu', 'liviu@gmail.com', 9)

users = Users()
users.db.clear_clients()

users.add_client(client1)
users.add_client(client2)
users.add_client(client3)

users.update_client_penalty(client1, 3)
print(users.get_client_by_code(5))
users.update_client_penalty(client1, 1)


class Reservations:
    def __init__(self):
        self.db = ReservationsDatabase('reservations')

    def make_reservation(self, client, book):
        if book.available > 0:
            reservation = Reservation(client.clientID, book.isbn)
            self.db.make_reservation(reservation)
            print(
                f"+RESERVATION CREATED SUCCESFULLY! Client: {client.name} | Client ID: {client.clientID} | Book: '{book.title}' | Book ISBN: {book.isbn} | Available: {book.available}")
            inventory.update_book_availability(book.isbn, book.decrement_quantity())
        else:
            print(f"'{book.title}' by {book.author}, ISBN {book.isbn} is out of stock!")

    def get_reservation_by_client(self, client):
        reservation_data = self.db.get_reservation_by_client(client.clientID)
        if reservation_data:
            return Reservation(id=reservation_data[0], clientID=reservation_data[1], isbn=reservation_data[2],
                               dateReserved=reservation_data[3], dueDate=reservation_data[4])
        return None

    def get_reservations(self):
        return self.db.get_reservations()


reservation_ledger = Reservations()
reservation_ledger.db.clear_reservations()

reservation_ledger.make_reservation(users.get_client_by_code(9), inventory.get_book_by_isbn(9781234567890))
reservation_ledger.make_reservation(users.get_client_by_code(5), inventory.get_book_by_isbn(9781234567893))
reservation_ledger.make_reservation(users.get_client_by_code(1), inventory.get_book_by_isbn(9781234567894))


print(reservation_ledger.get_reservation_by_client(client1))
