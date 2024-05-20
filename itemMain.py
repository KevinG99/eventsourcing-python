from eventstore import EventStore
from features.createItem import CreateItem
from features.modifyItem import ModifyItem
from features.itemDecider import ItemDecider
from features.itemReadmodel import ItemReadModel
import uuid

# Initialize components
event_store = EventStore()
decider = ItemDecider()
read_model = ItemReadModel()

# Handle a command to create an item
create_command = CreateItem(name="Sample Item")
create_events = decider.decide(create_command)

# Store events for creating an item
aggregate_id = str(uuid.uuid4())
for event in create_events:
    event_store.append(aggregate_id, event)

# Project events to read models after creation
events = event_store.get_events(aggregate_id)
read_model.project(events)

# Handle a command to modify the item
modify_command = ModifyItem(item_id=list(read_model.items.keys())[0], new_name="Modified Item")
modify_events = decider.decide(modify_command)

# Store events for modifying an item
for event in modify_events:
    event_store.append(aggregate_id, event)

# Project events to read models after modification
events = event_store.get_events(aggregate_id)
read_model.project(events)

# Access read models
print("Item Names:", read_model.items)
