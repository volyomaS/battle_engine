from termcolor import colored


class UI:
    @staticmethod
    def print_greeting(lang='en'):
        if lang == 'en':
            print(colored("Hello! It's my battle engine.", 'blue', attrs=['bold']))

    @staticmethod
    def print_help(lang='en'):
        if lang == 'en':
            print(colored("""Available commands (num or string):
            1. Add units stack to an army
            2. Battle
            3. Get armies
            4. Exit
            5. Load mod (for developers)""", 'blue'))

    @staticmethod
    def print_prompt(lang='en'):
        if lang == 'en':
            print(colored("Type a command: ", 'green'))

    @staticmethod
    def print_exit(lang='en'):
        if lang == 'en':
            print(colored("Thanks for using!", 'red', attrs=['bold']))

    @staticmethod
    def print_unexpected(lang='en'):
        if lang == 'en':
            print(colored("Unexpected command, try again", 'red'))

    @staticmethod
    def print_add(lang='en'):
        if lang == 'en':
            print(colored("Type unit's num, count and number of army (e.g. Skeleton 2 1)", 'blue'))
            print(colored("Available units:", 'blue'))

    @staticmethod
    def print_succ_add(lang='en'):
        if lang == 'en':
            print(colored("Successfully added!", 'blue'))

    @staticmethod
    def print_load(lang='en'):
        if lang == 'en':
            print(colored("Type name of unit (e.g. Module.***.Class): ", 'blue'))

    @staticmethod
    def print_battle(lang='en'):
        if lang == 'en':
            print(colored("Type 'pt' for print turn", 'blue'))
            print(colored("Type 'ps' for print status", 'blue'))
            print(colored("""Available commands:
            1. Attack
            2. Defend
            3. Wait
            4. Cast
            5. Surrender""", 'blue'))

    @staticmethod
    def print_quantity_diff(old: int, new: int, utype: str, lang='en'):
        if lang == 'en':
            print(colored(f"Quantity of {utype} from {int(old)} to {int(new)}", 'blue'))

    @staticmethod
    def print_dmg(dmg: float, utype: str, lang='en'):
        if lang == 'en':
            print(colored(f"Damage is {dmg} from {utype}", 'blue'))

    @staticmethod
    def print_dead(utype: str, lang='en'):
        if lang == 'en':
            print(colored(f"{utype} is dead", 'red'))

    @staticmethod
    def print_results(lang='en'):
        if lang == 'en':
            print(colored("Results of the battle", 'blue', attrs=['bold']))

    @staticmethod
    def print_for_army(army: int, lang='en'):
        if lang == 'en':
            print(colored(f"For army {army}:", 'green'))

    @staticmethod
    def print_hp_diff(old: float, new: float, utype: str, lang='en'):
        if lang == 'en':
            print(colored(f"Hp of {utype} from {old} to {new}", 'blue'))

    @staticmethod
    def print_stack(utype: str, quantity: int, lang='en'):
        if lang == 'en':
            print(colored(f"{utype}, {int(quantity)}", 'yellow'))

    @staticmethod
    def print_not_enough_stacks(lang='en'):
        if lang == 'en':
            print(colored("Not enough stacks for battle!", 'red'))

    @staticmethod
    def print_wrong_army(lang='en'):
        if lang == 'en':
            print(colored("Wrong army!", 'red'))
