class Reservation:
    def __init__(self, clientID, isbn, dateReserved=None, dueDate=None, id=None):
        self.id = id
        self.clientID = clientID
        self.isbn = isbn
        self.dateReserved = dateReserved
        self.dueDate = dueDate

    def __str__(self):
        return f"Reservation {self.id} (ClientID: {self.clientID}, Book ISBN: {self.isbn}, Date Reserverd: {self.dateReserved}, Due Date: {self.dueDate})"
