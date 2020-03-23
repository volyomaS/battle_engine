from Modifiers.BaseModifier import BaseModifier


class KingBuff(BaseModifier):
    @staticmethod
    def calc_def(defend):
        return defend + 3

    @staticmethod
    def calc_dmg(dmg: tuple):
        return tuple([dmg[0] + 3, dmg[1] + 3])

    @staticmethod
    def calc_init(init):
        return init + 3

    @staticmethod
    def calc_attack(attack):
        return attack + 3
