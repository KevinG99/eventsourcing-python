from eventstore import EventStore
from features.createItem import CreateItem
from features.modifyItem import ModifyItem
from features.itemDecider import ItemDecider
from features.itemReadmodel import ItemReadModel
from features.analytics.analyticsReadmodel import AnalyticsReadModel
from features.history.itemHIstoryReadModel import ItemHistoryReadModel
import uuid
# Initialize components
event_store = EventStore()
decider = ItemDecider()
read_model = ItemReadModel()
analytics_read_model = AnalyticsReadModel()
history_read_model = ItemHistoryReadModel()

# Handle a command to create an item
firstItemId = str(uuid.uuid4())
create_command = CreateItem(item_id=firstItemId, name="Sample Item")
create_events = decider.decide(create_command)

# Store events for creating an item
aggregate_id = str(uuid.uuid4())
for event in create_events:
    event_store.append(aggregate_id, event)

# Project events to read models after creation
events = event_store.get_events(aggregate_id)
read_model.project(events)
analytics_read_model.project(events)
history_read_model.project(events)

# Handle a command to modify the item
modify_command = ModifyItem(item_id=firstItemId, new_name="Modified Item")
modify_events = decider.decide(modify_command)

# Store events for modifying an item
for event in modify_events:
    event_store.append(aggregate_id, event)

# Project events to read models after modification
events = event_store.get_events(aggregate_id)
read_model.project(events)
analytics_read_model.project(events)
history_read_model.project(events)

# Modify the item again
another_modify_command = ModifyItem(item_id=firstItemId, new_name="Another Modified Name")
another_modify_events = decider.decide(another_modify_command)

# Store events for the second modification
for event in another_modify_events:
    event_store.append(aggregate_id, event)

# Project events to read models after the second modification
events = event_store.get_events(aggregate_id)
read_model.project(events)
analytics_read_model.project(events)
history_read_model.project(events)

# Access read models
print("Item Names:", read_model.items)
print("Modification Analytics:", analytics_read_model.modifications)
print("Modification Count:", analytics_read_model.get_modification_count(list(read_model.items.keys())[0]))
print("Modification History:", analytics_read_model.get_modification_history(list(read_model.items.keys())[0]))
print("Item Modification History:", history_read_model.get_history(firstItemId))
print("Comparison of Histories:", history_read_model.compare_histories(firstItemId))
