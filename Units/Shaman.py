from Unit import Unit
from dataclasses import dataclass
from Casts import *


@dataclass(frozen=True)
class Shaman(Unit):
    def __init__(self):
        Unit.__init__(self, "Shaman", 40, 12, 10, (7, 12), 10.5, list([]), RestoreHP)
