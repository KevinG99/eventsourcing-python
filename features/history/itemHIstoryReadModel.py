from typing import Dict, List
from common.readmodel import ReadModel
from common.event import Event
from features.createItem import ItemCreated
from features.modifyItem import ItemModified


class ItemHistoryReadModel(ReadModel):
    def __init__(self):
        self.history: Dict[str, List[Dict[str, str]]] = {}

    def project(self, events: List[Event]):
        for event in events:
            if isinstance(event, ItemCreated):
                self.history[event.item_id] = [{"name": event.name, "type": "Created"}]
            elif isinstance(event, ItemModified):
                if event.item_id in self.history:
                    self.history[event.item_id].append({"name": event.new_name, "type": "Modified"})

    def get_history(self, item_id: str) -> List[Dict[str, str]]:
        return self.history.get(item_id, [])

    def compare_histories(self, item_id: str) -> List[Dict[str, str]]:
        history = self.get_history(item_id)
        comparisons = []
        for i in range(1, len(history)):
            prev = history[i - 1]
            curr = history[i]
            comparisons.append({
                "previous_name": prev["name"],
                "current_name": curr["name"],
                "change_type": curr["type"]
            })
        return comparisons
