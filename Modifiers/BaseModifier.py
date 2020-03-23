class BaseModifier:
    __time: int

    def __init__(self, time=None):
        self.__time = time

    def get_time(self):
        return self.__time

    def decrease_time(self):
        if self.__time is not None:
            self.__time -= 1

    @staticmethod
    def calc_def(defend):
        return defend

    @staticmethod
    def calc_attack(attack):
        return attack

    @staticmethod
    def calc_init(init):
        return init

    @staticmethod
    def calc_dmg(dmg):
        return dmg
