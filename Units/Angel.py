from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *


@dataclass(frozen=True)
class Angel(Unit):
    def __init__(self):
        Unit.__init__(self, "Angel", 180, 27, 27, (45, 45), 11, list([KingBuff()]), Motivate)
