from Modifiers.BaseModifier import BaseModifier


class DmgBuff(BaseModifier):
    @staticmethod
    def calc_dmg(dmg: tuple):
        return tuple([dmg[0] * 1.1, dmg[1] * 1.1])
