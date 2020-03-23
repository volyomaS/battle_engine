from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *


@dataclass(frozen=True)
class Skeleton(Unit):
    def __init__(self):
        Unit.__init__(self, "Skeleton", 5, 1, 2, (1, 1), 10, list([KingBuff()]), None)
