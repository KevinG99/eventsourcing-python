from common.readmodel import ReadModel
from common.event import Event
from features.analytics.modifyItem import ItemModified as ItemModifiedAnalytics
from features.analytics.modificationHistory import ModificationHistoryEvent
from datetime import datetime
from typing import Any, Dict, List

class AnalyticsReadModel(ReadModel):
    def __init__(self):
        self.modifications: Dict[str, List[str]] = {}  # item_id -> list of modification timestamps
        self.history: Dict[str, List[Dict[str, Any]]] = {}  # item_id -> list of modification details

    def project(self, events: List[Event]):
        for event in events:
            if isinstance(event, ItemModifiedAnalytics):
                if event.item_id not in self.modifications:
                    self.modifications[event.item_id] = []
                self.modifications[event.item_id].append(event.modification_time)

            if isinstance(event, ModificationHistoryEvent):
                if event.item_id not in self.history:
                    self.history[event.item_id] = []
                self.history[event.item_id].append({
                    "old_name": event.old_name,
                    "new_name": event.new_name,
                    "modification_time": event.modification_time
                })

    def get_modification_count(self, item_id: str) -> int:
        return len(self.modifications.get(item_id, []))

    def get_modification_history(self, item_id: str) -> List[str]:
        return self.modifications.get(item_id, [])

    def get_detailed_modification_history(self, item_id: str) -> List[Dict[str, Any]]:
        return self.history.get(item_id, [])
