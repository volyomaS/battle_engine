from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *


@dataclass(frozen=True)
class BoneDragon(Unit):
    def __init__(self):
        Unit.__init__(self, "BoneDragon", 150, 27, 28, (15, 30), 11, list([DefBuff()]), StrongDefence)
