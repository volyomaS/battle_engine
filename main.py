import os
from UI import UI
from UnitsStack import UnitsStack
from BattleUnitsStack import BattleUnitsStack
from BattleArmy import BattleArmy
from Battle import Battle
from Units import *
from LoadMod import LoadMod

if __name__ == "__main__":
    lang = 'en'
    mods = []
    units = [Angel, BoneDragon, Crossbowman, Cyclops, Devil, Fury, Gryphon, Hydra, Lich, Shaman, Skeleton]
    army1 = []
    army2 = []

    os.system("cls")
    UI.print_greeting(lang=lang)
    while True:
        UI.print_help(lang=lang)
        UI.print_prompt(lang=lang)
        cmd = input()
        os.system("cls")
        if cmd == '4' or cmd.lower() == 'exit':
            UI.print_exit(lang=lang)
            input()
            exit()
        elif cmd == '2' or cmd.lower() == 'battle':
            if len(army1) < 1 or len(army2) < 1:
                UI.print_not_enough_stacks(lang=lang)
                continue
            b_army1 = BattleArmy(*list(map(lambda x: BattleUnitsStack(x), army1)))
            b_army2 = BattleArmy(*list(map(lambda x: BattleUnitsStack(x), army2)))
            battle = Battle(b_army1, b_army2)
            while True:
                battle.print_status()
                if battle.status:
                    break
                UI.print_battle(lang=lang)
                UI.print_prompt(lang=lang)
                cmd = input()
                os.system("cls")
                if cmd == '1' or cmd.lower() == 'attack':
                    print(f"Select unit to attack (e.g. 'Skeleton')")
                    battle.print_turn()
                    unit = input("Type: ")
                    battle.do_action('attack', unit)
                elif cmd == '4' or cmd.lower() == 'cast':
                    print(f"Select unit and army to cast (e.g. 'Skeleton 2')")
                    battle.print_turn()
                    unit = input("Type: ").split()
                    battle.do_action('cast', unit[0], unit[1])
                elif cmd == '5' or cmd.lower() == 'surrender':
                    battle.do_action("surrender")
                    break
                elif cmd == '2' or cmd.lower() == 'defend':
                    battle.do_action("defend")
                elif cmd == '3' or cmd.lower() == 'wait':
                    battle.do_action("wait")
                elif cmd.lower() == 'pt':
                    battle.print_turn()
                elif cmd.lower() == 'ps':
                    battle.print_status()
                # TODO delete units stack
            new_army1 = []
            new_army2 = []
            os.system("cls")
            UI.print_results(lang=lang)
            UI.print_for_army(1, lang=lang)
            for a, b in zip(army1, b_army1.stacks):
                if not b.isAlive:
                    UI.print_dead(b.type, lang=lang)
                else:
                    UI.print_quantity_diff(a.quantity, b.quantity, a.unit.type, lang=lang)
                    UI.print_hp_diff(a.unit.hp, b.hp, a.unit.type, lang=lang)
                    new_army1.append(UnitsStack(a.unit, b.quantity))
            print()
            UI.print_for_army(2)
            for a, b in zip(army2, b_army2.stacks):
                if not b.isAlive:
                    UI.print_dead(b.type, lang=lang)
                else:
                    UI.print_quantity_diff(a.quantity, b.quantity, a.unit.type, lang=lang)
                    UI.print_hp_diff(a.unit.hp, b.hp, a.unit.type, lang=lang)
                    new_army2.append(UnitsStack(a.unit, b.quantity))
            print()
            army1 = list(new_army1)
            army2 = list(new_army2)
        elif cmd == '1' or cmd.lower() == 'add':
            UI.print_add(lang=lang)
            for i in range(len(units)):
                print(f"{i+1}. {units[i].__name__}")
            for i in range(len(mods)):
                print(f"{i + 1 + len(units)}. {mods[i].__name__}")
            ind, count, army = map(int, input().split())
            if army == 1:
                if ind <= len(units):
                    army1.append(UnitsStack(units[ind-1](), count))
                else:
                    army1.append(UnitsStack(mods[ind-1-len(units)](), count))
            elif army == 2:
                if ind <= len(units):
                    army2.append(UnitsStack(units[ind-1](), count))
                else:
                    army2.append(UnitsStack(mods[ind-1-len(units)](), count))
            else:
                UI.print_wrong_army(lang=lang)
                continue
            os.system("cls")
            UI.print_succ_add(lang=lang)
        elif cmd == '5' or cmd.lower() == 'load':
            UI.print_load(lang=lang)
            mods.append(LoadMod.load(input()))
            os.system("cls")
            UI.print_succ_add(lang=lang)
        elif cmd == '3' or cmd.lower() == 'get':
            UI.print_for_army(1, lang=lang)
            for stack in army1:
                UI.print_stack(stack.unit.type, stack.quantity, lang=lang)
            UI.print_for_army(2, lang=lang)
            for stack in army2:
                UI.print_stack(stack.unit.type, stack.quantity, lang=lang)
        else:
            UI.print_unexpected(lang=lang)
