from BattleArmy import BattleArmy
from collections import deque
from Modifiers import *
from termcolor import colored
from UI import UI
import numpy as np


class Battle:
    __army1: BattleArmy
    __army2: BattleArmy
    __current_round = 1
    __isCompleted: bool
    __winner: int
    __init: deque
    __waiting: deque

    def __init__(self, army1: BattleArmy, army2: BattleArmy):
        self.__army1 = army1
        self.__army2 = army2
        self.__current_round = 1
        self.__isCompleted = False
        self.__winner = None
        arr = []
        for army in [army1, army2]:
            for stack in army.stacks:
                if army == army1 and stack.isAlive:
                    arr.append([stack.init, stack.type, 1])
                elif stack.isAlive:
                    arr.append([stack.init, stack.type, 2])
        arr.sort(reverse=True, key=lambda x: x[0])
        self.__init = deque(arr)
        self.__waiting = deque(list())

    def get_init(self):
        arr = []
        for army in [self.__army1, self.__army2]:
            for stack in army.stacks:
                if army == self.__army1 and stack.isAlive:
                    arr.append([stack.init, stack.type, 1])
                elif stack.isAlive:
                    arr.append([stack.init, stack.type, 2])
        arr.sort(reverse=True, key=lambda x: x[0])
        return deque(arr)

    @property
    def current_round(self):
        return self.__current_round

    def next_round(self):
        self.__current_round += 1

    @property
    def current_turn(self):
        return self.__init[0]

    def print_turn(self):
        print(f"{self.__init[0][1]}({self.__init[0][2]})", end=" ")
        for i in range(1, len(self.__init)):
            print(f"-> {self.__init[i][1]}({self.__init[i][2]})", end=" ")
        for i in range(0, len(self.__waiting)):
            print(f"-> {self.__waiting[i][1]}({self.__waiting[i][2]})", end=" ")
        print("|", end=" ")
        arr = self.get_init()
        print(f"{arr[0][1]}({arr[0][2]})", end=" ")
        for i in range(1, len(arr)):
            print(f"-> {arr[i][1]}({arr[i][2]})", end=" ")
        print()

    @property
    def status(self):
        return self.__isCompleted

    def print_status(self):
        if self.__isCompleted:
            print(colored(f"Battle is over, winner is {self.__winner} army!", 'red'))
        else:
            print(colored("Battle is going!", 'red'))

    def do_action(self, action, *params):
        if self.__isCompleted:
            self.print_status()
        elif action == "attack":
            self.attack(self.current_turn, (0, params[0], self.current_turn[2] % 2 + 1)) if len(params) == 1 and type(params[0]) == str else print("Wrong params for attack")
        elif action == "wait":
            self.wait()
        elif action == "defend":
            self.defend()
        elif action == "surrender":
            self.surrender()
        elif action == "cast":
            self.cast(self.current_turn, (0, params[0], params[1]))

        if len(self.__init) == 0 and len(self.__waiting) == 0:
            self.__init = self.get_init()
            self.next_round()
            for stack in self.__army1.stacks:
                stack.retaliate = True
            for stack in self.__army2.stacks:
                stack.retaliate = True
        elif len(self.__init) == 0 and len(self.__waiting) != 0:
            self.__init = self.__waiting
            self.__waiting = deque(list())

    def attack(self, attack, defend, retaliate = False):
        ind1, ind2 = None, None

        if attack[2] == 1:
            army_a = self.__army1
            army_d = self.__army2
        else:
            army_a = self.__army2
            army_d = self.__army1

        for i in range(0, len(army_a.stacks)):
            if attack[1] == army_a.stacks[i].type:
                ind1 = i
                break
        for i in range(0, len(army_d.stacks)):
            if defend[1] == army_d.stacks[i].type:
                ind2 = i
                break

        if army_a.stacks[ind1].attack > army_d.stacks[ind2].defence:
            damage = army_a.stacks[ind1].quantity * \
                     np.random.choice(np.linspace(army_a.stacks[ind1].dmg[0],
                                                  army_a.stacks[ind1].dmg[1], 100)) * \
                     (1 + 0.05 * (army_a.stacks[ind1].attack - army_d.stacks[ind2].defence))
        else:
            damage = army_a.stacks[ind1].quantity * \
                     np.random.choice(np.linspace(army_a.stacks[ind1].dmg[0],
                                                  army_a.stacks[ind1].dmg[1], 100)) / \
                     (1 + 0.05 * (army_d.stacks[ind2].defence - army_a.stacks[ind1].attack))
        UI.print_dmg(damage, army_a.stacks[ind1].type)
        least_hp = (((army_d.stacks[ind2].quantity - 1) * army_d.stacks[ind2].base_hp) +
                    army_d.stacks[ind2].hp) - damage
        if least_hp > 0:
            UI.print_quantity_diff(army_d.stacks[ind2].quantity, least_hp // army_d.stacks[ind2].base_hp + 1,
                                   army_d.stacks[ind2].type)
            army_d.stacks[ind2].quantity = least_hp // army_d.stacks[ind2].base_hp + 1
            army_d.stacks[ind2].hp = least_hp % army_d.stacks[ind2].base_hp
            if army_d.stacks[ind2].retaliate and retaliate is False:
                army_d.stacks[ind2].retaliate = False
                self.attack(defend, attack, retaliate=True)
        else:
            UI.print_dead(army_d.stacks[ind2].type)
            army_d.stacks[ind2].kill()
            for i in range(0, len(self.__init)):
                if self.__init[i][1] == defend[1] and self.__init[i][2] == defend[2]:
                    arr = list(self.__init)
                    self.__init = deque(arr[0:i] + arr[i + 1:])
                    break
            if self.count_stacks(defend[2]) == 0:
                self.__isCompleted = True
                self.__winner = attack[2]

        if retaliate is False and len(self.__init) != 0 and self.__init[0] == attack:
            self.__init.popleft()

    def wait(self):
        self.__waiting.appendleft(self.__init.popleft())

    def defend(self):
        ct = self.current_turn
        if ct[2] == 1:
            army = self.__army1
        else:
            army = self.__army2
        for i in range(0, len(army.stacks)):
            if ct[1] == army.stacks[i].type:
                ind = i
                break
        army.stacks[ind].add_buff(DefBuff(1))
        self.__init.popleft()

    def surrender(self):
        ct = self.current_turn
        self.__isCompleted = True
        self.__winner = (ct[2] % 2) + 1
        self.print_status()

    def count_stacks(self, num):
        if num == 1:
            army = self.__army1
        else:
            army = self.__army2
        count = 0
        for stack in army.stacks:
            if stack.isAlive:
                count += 1
        return count

    def cast(self, attack, defend):
        ind1, ind2 = None, None

        if int(attack[2]) == 1:
            army_a = self.__army1
        else:
            army_a = self.__army2
        if int(defend[2]) == 1:
            army_d = self.__army1
        else:
            army_d = self.__army2

        for i in range(0, len(army_a.stacks)):
            if attack[1] == army_a.stacks[i].type:
                ind1 = i
                break
        for i in range(0, len(army_d.stacks)):
            if defend[1] == army_d.stacks[i].type:
                ind2 = i
                break

        if army_a.stacks[ind1].cast is not None:
            army_a.stacks[ind1].cast.cast(army_a.stacks[ind1], army_d.stacks[ind2])
        else:
            print("This UnitStack has no casts")

        self.__init.popleft()
