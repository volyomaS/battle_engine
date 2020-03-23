from dataclasses import dataclass
from Casts.BaseCast import BaseCast


@dataclass(frozen=True)
class Unit:
    type: str
    hp: float
    attack: float
    defence: float
    dmg: tuple
    init: float
    buffs: list
    cast: BaseCast
