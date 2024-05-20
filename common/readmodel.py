from abc import ABC, abstractmethod
from typing import List
from common.event import Event

class ReadModel(ABC):
    @abstractmethod
    def project(self, events: List[Event]):
        pass
