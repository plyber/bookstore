import sqlite3
from datetime import timedelta, datetime


class ReservationsDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup()

    def setup(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservations
                                       (clientID TEXT, isbn TEXT PRIMARY KEY, 
                                        dateReserved DATE, dueDate DATE)''')
        self.conn.commit()

    def make_reservation(self, client_id, book_isbn):
        date_reserved = datetime.now().strftime('%D %H:%M:%S')
        due_date = datetime.today() + timedelta(days=30)
        try:
            self.cursor.execute("INSERT INTO reservations VALUES (?, ?, ?, ?)",
                                (client_id, book_isbn, date_reserved, due_date))
            self.conn.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def get_reservations(self):
        self.cursor.execute("SELECT * FROM reservations")
        return self.cursor.fetchall()

    def get_reservation_by_client(self, client):
        self.cursor.execute("SELECT * FROM reservations WHERE clientID = ?", (client,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

    def clear_reservations(self):
        self.cursor.execute("DELETE FROM reservations")
        self.conn.commit()
