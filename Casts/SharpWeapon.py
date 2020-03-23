from Casts.BaseCast import BaseCast
from Modifiers.AttackBuff import AttackBuff


class SharpWeapon(BaseCast):
    @staticmethod
    def cast(actor, target):
        target.add_buff(AttackBuff(3))
