from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *


@dataclass(frozen=True)
class Fury(Unit):
    def __init__(self):
        Unit.__init__(self, "Fury", 16, 5, 3, (5, 7), 16, list([InitBuff()]), None)
