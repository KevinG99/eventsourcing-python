
class AccountCreatedEvent:
    def __init__(self, data):
        self.data = data

    def apply(self, model):
        email = self.data['email']
        name = self.data['name']
        model["reserved"] = {"email": email}


class CreatedAccountCommand:
    def __init__(self, data):
        self.email = data['email']
        self.name = data['name']

    def execute(self):
       # print(f"Reserve account for {self.email}")
        return AccountCreatedEvent({"email": self.email, "name": self.name})
