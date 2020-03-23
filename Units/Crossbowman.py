from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *


@dataclass(frozen=True)
class Crossbowman(Unit):
    def __init__(self):
        Unit.__init__(self, "Crossbowman", 10, 4, 4, (2, 8), 8, list([AttackBuff()]), None)
