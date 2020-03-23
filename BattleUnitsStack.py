from UnitsStack import UnitsStack
from Modifiers import *


class BattleUnitsStack:
    # __isAlive: bool
    # __quantity: int
    # __dmg: tuple
    # __type: str
    # __attack: float
    # __hp: float
    # __base_hp: float
    # __defence: float
    # __init: float
    # __buffs: list
    # __retaliate: bool

    def __init__(self, unitsstack: UnitsStack):
        self.__isAlive = True
        self.__quantity = unitsstack.quantity
        self.__dmg = unitsstack.unit.dmg
        self.__type = unitsstack.unit.type
        self.__hp = unitsstack.unit.hp
        self.__base_hp = unitsstack.unit.hp
        self.__attack = unitsstack.unit.attack
        self.__defence = unitsstack.unit.defence
        self.__init = unitsstack.unit.init
        self.__buffs = list(unitsstack.unit.buffs)
        self.__cast = unitsstack.unit.cast
        self.__retaliate = True

    @property
    def isAlive(self):
        return self.__isAlive

    def kill(self):
        self.__isAlive = False
        self.__quantity = 0

    def resurrect(self, hp):
        self.__isAlive = True
        self.__quantity = self.__hp // hp

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity: int):
        if new_quantity > 0:
            self.__quantity = new_quantity
        elif new_quantity == 0:
            exit("Error, use BattleUnitsStack.kill instead")
        else:
            exit("Your quantity is incorrect because of new_quantity < 0")

    @property
    def dmg(self):
        new_dmg = self.__dmg
        i = 0
        while i < len(self.__buffs):
            new_dmg = self.__buffs[i].calc_dmg(new_dmg)
            self.__buffs[i].decrease_time()
            if self.__buffs[i].get_time() == 0:
                self.__buffs = self.__buffs[:i] + self.__buffs[i + 1:]
            i += 1
        return new_dmg

    @dmg.setter
    def dmg(self, new_dmg: tuple):
        if len(new_dmg) == 2:
            self.__dmg = new_dmg
        else:
            exit("Your dmg is incorrect, because of len(new_dmg) != 2")

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type: str):
        self.__type = new_type

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, new_hp: float):
        if new_hp > 0:
            self.__hp = new_hp
        else:
            exit("Your hp is incorrect, because of new_hp <= 0")

    @property
    def base_hp(self):
        return self.__base_hp

    @property
    def attack(self):
        new_attack = self.__attack
        i = 0
        while i < len(self.__buffs):
            new_attack = self.__buffs[i].calc_attack(new_attack)
            self.__buffs[i].decrease_time()
            if self.__buffs[i].get_time() == 0:
                self.__buffs = self.__buffs[:i] + self.__buffs[i + 1:]
            i += 1
        return new_attack

    @attack.setter
    def attack(self, new_attack: float):
        if new_attack >= 0:
            self.__attack = new_attack
        else:
            exit("Your attack is incorrect, because of new_attack < 0")

    @property
    def defence(self):
        new_def = self.__defence
        i = 0
        while i < len(self.__buffs):
            new_def = self.__buffs[i].calc_def(new_def)
            self.__buffs[i].decrease_time()
            if self.__buffs[i].get_time() == 0:
                self.__buffs = self.__buffs[:i] + self.__buffs[i + 1:]
            i += 1
        return new_def

    @defence.setter
    def defence(self, new_defence: float):
        if new_defence >= 0:
            self.__attack = new_defence
        else:
            exit("Your defence is incorrect, because of new_defence < 0")

    @property
    def init(self):
        new_init = self.__init
        i = 0
        while i < len(self.__buffs):
            new_init = self.__buffs[i].calc_init(new_init)
            self.__buffs[i].decrease_time()
            if self.__buffs[i].get_time() == 0:
                self.__buffs = self.__buffs[:i] + self.__buffs[i + 1:]
            i += 1
        return new_init

    @init.setter
    def init(self, new_init: float):
        if new_init >= 0:
            self.__init = new_init
        else:
            exit("Your init is incorrect, because of new_init < 0")

    def add_buff(self, buff):
        self.__buffs.append(buff)

    def remove_buff(self, buff):
        i = 0
        while i < len(self.__buffs):
            if buff == self.__buffs[i]:
                self.__buffs = self.__buffs[:i] + self.__buffs[i + 1:]
            i += 1

    @property
    def cast(self):
        return self.__cast

    @property
    def retaliate(self):
        return self.__retaliate

    @retaliate.setter
    def retaliate(self, new: bool):
        self.__retaliate = new
