import datetime


class Client:
    def __init__(self, name, email, clientID, canRent=True, penalties=0, dateCreated=None):
        self.name = name
        self.email = email
        self.clientID = clientID
        self.canRent = canRent
        self.penalties = penalties
        self.dateCreated = dateCreated if dateCreated else datetime.datetime.now().strftime('%D %H:%M')

    def __str__(self):
        return f"Client(Name: {self.name}, Email: {self.email}, ID: {self.clientID}, Can Rent: {self.canRent}, Penalties: {self.penalties}, Date Created: {self.dateCreated})"
