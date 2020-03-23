from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *


@dataclass(frozen=True)
class Devil(Unit):
    def __init__(self):
        Unit.__init__(self, "Devil", 166, 27, 25, (36, 66), 11, list([KingBuff()]), None)
