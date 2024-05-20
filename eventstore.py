from abc import ABC, abstractmethod

from typing import List, Dict
from common.event import Event

class EventStore:
    def __init__(self):
        self.events: Dict[str, List[Event]] = {}

    def append(self, aggregate_id: str, event: Event):
        if aggregate_id not in self.events:
            self.events[aggregate_id] = []
        self.events[aggregate_id].append(event)

    def get_events(self, aggregate_id: str) -> List[Event]:
        return self.events.get(aggregate_id, [])
