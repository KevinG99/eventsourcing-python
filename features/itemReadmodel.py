from common.readmodel import ReadModel
from common.event import Event
from features.createItem import ItemCreated
from features.modifyItem import ItemModified
from typing import Any, Dict, List

class ItemReadModel(ReadModel):
    def __init__(self):
        self.items: Dict[str, str] = {}

    def project(self, events: List[Event]):
        for event in events:
            if isinstance(event, ItemCreated):
                self.items[event.item_id] = event.name
            elif isinstance(event, ItemModified):
                if event.item_id in self.items:
                    self.items[event.item_id] = event.new_name
