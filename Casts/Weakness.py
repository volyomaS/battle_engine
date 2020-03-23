from Modifiers.WeakWeapon import WeakWeapon
from Casts.BaseCast import BaseCast


class Weakness(BaseCast):
    @staticmethod
    def cast(actor, target):
        target.add_buff(WeakWeapon(3))
