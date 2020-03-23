from Casts.BaseCast import BaseCast


class RestoreHP(BaseCast):
    @staticmethod
    def cast(actor, target):
        target.hp = target.base_hp
