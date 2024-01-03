import sqlite3


class BooksDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup()

    def setup(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books
                                       (title TEXT, author TEXT, isbn TEXT PRIMARY KEY, 
                                        price REAL, category TEXT, available BOOLEAN)''')
        self.conn.commit()

    def add_book(self, title, author, isbn, price, category, available):
        try:
            self.cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)",
                                (title, author, isbn, price, category, available))
            self.conn.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def update_book_availability(self, isbn, available):
        try:
            self.cursor.execute("UPDATE books SET available = ? WHERE isbn = ?",
                                (available, isbn))
            self.conn.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def remove_book(self, isbn):
        try:
            self.cursor.execute("DELETE FROM books WHERE isbn = ?", (isbn,))
            self.conn.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def get_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def get_book_by_isbn(self, isbn):
        self.cursor.execute("SELECT * FROM books WHERE isbn = ?", (isbn,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

    def clear_books(self):
        self.cursor.execute("DELETE FROM books")
        self.conn.commit()
