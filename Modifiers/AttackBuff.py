from Modifiers.BaseModifier import BaseModifier


class AttackBuff(BaseModifier):
    @staticmethod
    def calc_attack(attack):
        return attack * 1.2
