from abc import ABC, abstractmethod
from typing import List
from common.command import Command
from common.event import Event

class Decider(ABC):
    @abstractmethod
    def decide(self, command: Command) -> List[Event]:
        pass
