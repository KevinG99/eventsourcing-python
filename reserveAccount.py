from eventstore import Command
class AccountReservedEvent:
    def __init__(self, data):
        self.data = data

    def apply(self, model):
        email = self.data['email']
        model["reserved"] = {"email": email}


class ReserveAccountCommand (Command):
    def __init__(self, email):
        self.email = email

    def execute(self):
       # print(f"Reserve account for {self.email}")
        return AccountReservedEvent({"email": self.email})
