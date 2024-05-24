from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
from eventstore import EventStore
from features.createItem import CreateItem
from features.modifyItem import ModifyItem
from features.itemDecider import ItemDecider
from features.itemReadmodel import ItemReadModel
from features.analytics.analyticsReadmodel import AnalyticsReadModel
from features.history.itemHIstoryReadModel import ItemHistoryReadModel

app = FastAPI()

# Initialize components
event_store = EventStore()
decider = ItemDecider()
read_model = ItemReadModel()
analytics_read_model = AnalyticsReadModel()
history_read_model = ItemHistoryReadModel()

class CreateItemRequest(BaseModel):
    name: str

class ModifyItemRequest(BaseModel):
    item_id: str
    new_name: str

@app.post("/items/")
def create_item(request: CreateItemRequest):
    item_id = str(uuid.uuid4())
    create_command = CreateItem(item_id=item_id, name=request.name)
    create_events = decider.decide(create_command)

    aggregate_id = str(uuid.uuid4())
    for event in create_events:
        event_store.append(aggregate_id, event)

    # Project events to read models
    events = event_store.get_events(aggregate_id)
    read_model.project(events)
    analytics_read_model.project(events)
    history_read_model.project(events)

    return {"item_id": item_id}

@app.put("/items/")
def modify_item(request: ModifyItemRequest):
    modify_command = ModifyItem(item_id=request.item_id, new_name=request.new_name)
    modify_events = decider.decide(modify_command)

    aggregate_id = str(uuid.uuid4())  # Assuming the aggregate ID is related to the item ID
    for event in modify_events:
        event_store.append(aggregate_id, event)

    # Project events to read models
    events = event_store.get_events(aggregate_id)
    read_model.project(events)
    analytics_read_model.project(events)
    history_read_model.project(events)

    return {"item_id": request.item_id}

@app.get("/items/")
def get_items():
    return {"items": read_model.items}

@app.get("/analytics/{item_id}/modification_count")
def get_modification_count(item_id: str):
    return {"modification_count": analytics_read_model.get_modification_count(item_id)}

@app.get("/analytics/{item_id}/modification_history")
def get_modification_history(item_id: str):
    return {"modification_history": analytics_read_model.get_modification_history(item_id)}

@app.get("/history/{item_id}")
def get_item_history(item_id: str):
    return {"history": history_read_model.get_history(item_id)}

@app.get("/history/{item_id}/comparison")
def compare_histories(item_id: str):
    return {"comparison": history_read_model.compare_histories(item_id)}

# Run the server using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
