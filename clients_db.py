import sqlite3

class ClientsDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup()

    def setup(self):
        self.cursor.execute("DROP TABLE IF EXISTS clients")
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clients
                                       (name TEXT, email TEXT, clientID INTEGER PRIMARY KEY, 
                                        canRent BOOLEAN, penalties INTEGER, dateCreated DATE)''')
        self.conn.commit()

    def add_client(self, client):
        try:
            self.cursor.execute("INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?)",
                                (client.name, client.email, client.clientID, client.canRent, client.penalties, client.dateCreated))
            self.conn.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def get_clients(self):
        self.cursor.execute("SELECT * FROM clients")
        return self.cursor.fetchall()

    def get_client_by_code(self, id):
        self.cursor.execute("SELECT * FROM clients WHERE clientID = ?", (id,))
        return self.cursor.fetchone()

    def update_client_penalty(self, clientID, penalty):
        try:
            self.cursor.execute("UPDATE clients SET penalties = ? WHERE clientID = ?",
                                (penalty, clientID))
            self.conn.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def delete_client(self, clientID):
        try:
            self.cursor.execute("DELETE FROM clients WHERE clientID = ?", (clientID,))
            self.conn.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def close(self):
        self.conn.close()

    def clear_clients(self):
        self.cursor.execute("DELETE FROM clients")
        self.conn.commit()
