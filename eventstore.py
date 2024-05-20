from abc import ABC, abstractmethod


class EventStore:
    def __init__(self):
        self.events = []

    def save(self, event):
        self.events.append(event)

    def get_all(self):
        return self.events



#event abstraction
# accountCreatedEvent inherits from Event

#command abstraction
# createAccountCommand inherits from Command

#readmodel abstraction
# accountDetails inherits from ReadModel


class Event(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def apply(self, model):
        pass


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class ReadModel:
    def __init__(self):
        self.state = {}

    def apply(self, event):
        event.apply(self.state)
