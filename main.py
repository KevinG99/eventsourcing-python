from createAccount import CreatedAccountCommand
from eventstore import EventStore, ReadModel
from reserveAccount import ReserveAccountCommand
from userAggregate import CreateUserCommand, ReserveUserCommand, UserAggregate


eventstore = EventStore()
readmodel = ReadModel()
aggregate = UserAggregate()

command = ReserveUserCommand("John")

event = command.execute(aggregate)
eventstore.save(event)
aggregate.apply(event)
readmodel.apply(event)


command = CreateUserCommand("Johne")
event = command.execute(aggregate)
eventstore.save(event)
readmodel.apply(event)

print(eventstore.get_all())

print(readmodel.state)
