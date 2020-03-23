from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *


@dataclass(frozen=True)
class Cyclops(Unit):
    def __init__(self):
        Unit.__init__(self, "Cyclops", 85, 20, 15, (18, 26), 10, list([]), None)
