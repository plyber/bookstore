import sqlite3
from datetime import timedelta, datetime


class ReservationsDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup()

    def setup(self):
        self.cursor.execute("DROP TABLE IF EXISTS reservations")
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservations
                                       (id INTEGER PRIMARY KEY, clientID TEXT, isbn INTEGER,
                                        dateReserved DATE, dueDate DATE)''')
        self.conn.commit()

    def make_reservation(self, reservation):
        date_reserved = datetime.today()
        due_date = datetime.today() + timedelta(days=30)
        try:
            self.cursor.execute("INSERT INTO reservations (clientID, isbn, dateReserved, dueDate) VALUES (?, ?, ?, ?)",
                                (reservation.clientID, reservation.isbn, date_reserved, due_date))
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
