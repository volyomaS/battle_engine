from Modifiers.BaseModifier import BaseModifier


class InitBuff(BaseModifier):
    @staticmethod
    def calc_init(init):
        return init + 5
