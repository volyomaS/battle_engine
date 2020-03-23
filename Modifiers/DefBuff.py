from Modifiers.BaseModifier import BaseModifier


class DefBuff(BaseModifier):
    @staticmethod
    def calc_def(defend):
        return defend * 1.3
