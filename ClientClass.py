import datetime

class Client:
    def __init__(self, name, email, clientID):
        self.name = name
        self.email = email
        self.clientID = clientID
        self.canRent = True
        self.penalties = 0
        self.dateCreated = datetime.datetime.now().strftime('%D %H:%M')


