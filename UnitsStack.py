from dataclasses import dataclass
from Unit import Unit


@dataclass(frozen=True)
class UnitsStack:
    unit: Unit
    quantity: int
