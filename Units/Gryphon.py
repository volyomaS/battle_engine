from Unit import Unit
from dataclasses import dataclass
from Modifiers import *
from Casts import *


@dataclass(frozen=True)
class Gryphon(Unit):
    def __init__(self):
        Unit.__init__(self, "Gryphon", 30, 7, 5, (5, 10), 15, list([]), None)
