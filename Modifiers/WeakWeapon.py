from Modifiers.BaseModifier import BaseModifier


class WeakWeapon(BaseModifier):
    @staticmethod
    def calc_attack(attack):
        return attack * 0.6
