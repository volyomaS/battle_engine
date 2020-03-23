from Casts.BaseCast import BaseCast
from Modifiers.DefBuff import DefBuff


class StrongDefence(BaseCast):
    @staticmethod
    def cast(actor, target):
        target.add_buff(DefBuff(3))
