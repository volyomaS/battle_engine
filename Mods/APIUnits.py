from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *


@dataclass(frozen=True)
class Imp(Unit):
    def __init__(self):
        Unit.__init__(self, "Imp", 1, 1, 1, (1, 1), 1, list([]), None)


@dataclass(frozen=True)
class Papich(Unit):
    def __init__(self):
        Unit.__init__(self, "Papich", 29, 29, 29, (28, 30), 29, list([KingBuff()]), Motivate)
