from common.readmodel import ReadModel
from common.event import Event
from features.analytics.modifyItem import ItemModified
from datetime import datetime
from typing import Any, Dict, List


class AnalyticsReadModel(ReadModel):
    def __init__(self):
        self.modifications: Dict[str, List[str]] = {}  # item_id -> list of modification timestamps

    def project(self, events: List[Event]):
        for event in events:
            if isinstance(event, ItemModified):
                if event.item_id not in self.modifications:
                    self.modifications[event.item_id] = []
                self.modifications[event.item_id].append(event.modification_time)

    def get_modification_count(self, item_id: str) -> int:
        return len(self.modifications.get(item_id, []))

    def get_modification_history(self, item_id: str) -> List[str]:
        return self.modifications.get(item_id, [])
