from common.command import Command
from typing import Dict, Any

class ModifyItem(Command):
    def __init__(self, item_id: str, new_name: str):
        self.item_id = item_id
        self.new_name = new_name

    def to_dict(self) -> Dict[str, Any]:
        return {"item_id": self.item_id, "new_name": self.new_name}


from common.event import Event

class ItemModified(Event):
    def __init__(self, item_id: str, new_name: str):
        self.item_id = item_id
        self.new_name = new_name

    def to_dict(self) -> Dict[str, Any]:
        return {"item_id": self.item_id, "new_name": self.new_name}
