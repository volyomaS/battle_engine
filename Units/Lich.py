from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *

@dataclass(frozen=True)
class Lich(Unit):
    def __init__(self):
        Unit.__init__(self, "Lich", 50, 15, 15, (12, 17), 10, list([DefBuff()]), None)
