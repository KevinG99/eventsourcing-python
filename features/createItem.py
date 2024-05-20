from common.command import Command
from common.event import Event
from typing import Dict, Any

class CreateItem(Command):
    def __init__(self, item_id: str, name: str):
        self.item_id = item_id
        self.name = name

    def to_dict(self) -> Dict[str, Any]:
        return {"item_id": self.item_id, "name": self.name}



class ItemCreated(Event):
    def __init__(self, item_id: str, name: str):
        self.item_id = item_id
        self.name = name

    def to_dict(self) -> Dict[str, Any]:
        return {"item_id": self.item_id, "name": self.name}
