from Casts.BaseCast import BaseCast
from Modifiers.InitBuff import InitBuff


class Motivate(BaseCast):
    @staticmethod
    def cast(actor, target):
        target.add_buff(InitBuff())
