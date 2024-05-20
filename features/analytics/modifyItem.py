from common.event import Event
from typing import Dict, Any

class ItemModified(Event):
    def __init__(self, item_id: str, new_name: str, modification_time: str):
        self.item_id = item_id
        self.new_name = new_name
        self.modification_time = modification_time

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item_id": self.item_id,
            "new_name": self.new_name,
            "modification_time": self.modification_time
        }
