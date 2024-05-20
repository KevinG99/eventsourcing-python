from common.decider import Decider
from common.command import Command
from common.event import Event
from features.createItem import CreateItem, ItemCreated
from features.modifyItem import ModifyItem, ItemModified
from typing import List
import uuid

class ItemDecider(Decider):
    def decide(self, command: Command) -> List[Event]:
        if isinstance(command, CreateItem):
            item_id = str(uuid.uuid4())
            return [ItemCreated(item_id, command.name)]
        elif isinstance(command, ModifyItem):
            return [ItemModified(command.item_id, command.new_name)]
        return []
