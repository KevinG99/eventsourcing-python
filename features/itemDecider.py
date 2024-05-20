from common.decider import Decider
from common.command import Command
from common.event import Event
from features.createItem import CreateItem, ItemCreated
from features.modifyItem import ModifyItem, ItemModified as ItemModifiedOriginal
from features.analytics.modifyItem import ItemModified as ItemModifiedAnalytics
from typing import List
import uuid
from datetime import datetime

class ItemDecider(Decider):
    def decide(self, command: Command) -> List[Event]:
        if isinstance(command, CreateItem):
            item_id = str(uuid.uuid4())
            return [ItemCreated(item_id, command.name)]
        elif isinstance(command, ModifyItem):
            modification_time = datetime.utcnow().isoformat()
            return [
                ItemModifiedOriginal(command.item_id, command.new_name),
                ItemModifiedAnalytics(command.item_id, command.new_name, modification_time)
            ]
        return []
