from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *


@dataclass(frozen=True)
class Hydra(Unit):
    def __init__(self):
        Unit.__init__(self, "Hydra", 80, 15, 12, (7, 14), 7, list([DmgBuff()]), None)
