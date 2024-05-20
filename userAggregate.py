from eventstore import Event, Command

class UserReservedEvent(Event):
    def apply(self, model):
        username = self.data['username']
        model[username] = {"username": username, "reserved": True}

class UserCreatedEvent(Event):
    def apply(self, model):
        username = self.data['username']
        name = self.data['name']
        model[username] = {"username": username, "name": name, "reserved": False}

class CreateUserCommand(Command):
    def __init__(self, username):
        self.username = username

    def execute(self, aggregate):
        return aggregate.create_user(self.username)

class ReserveUserCommand(Command):
    def __init__(self, username):
        self.username = username

    def execute(self, aggregate):
        return aggregate.reserve_user(self.username)


class UserAggregate:
    def __init__(self, username=None, reserved=False):
        self.username = username
        self.reserved = reserved

    def apply(self, event):
        if isinstance(event, UserCreatedEvent):
            self.username = event.data['username']
        elif isinstance(event, UserReservedEvent):
            self.username = event.data['username']
            self.reserved = True

    def create_user(self, username):
        if self.username is not None:
            raise ValueError("User already created")
        return UserCreatedEvent({"username": username})

    def reserve_user(self, username):
        if self.reserved:
            raise ValueError("User already reserved")
        return UserReservedEvent({"username": username})

    def create_account(self, username, name):
        if not self.reserved:
            raise ValueError("User not reserved")
        return UserCreatedEvent({"username": username, "name": name})
