import importlib

import Mods


class LoadMod:
    @staticmethod
    def load(module: str) -> object:
        try:
            components = module.split('.')
            mod = importlib.import_module(components[0], 'Mods')
            # mod = __import__()
            for comp in components[1:]:
                mod = getattr(mod, comp)
            return mod
        except AttributeError:
            exit("There is no such attribute")
        except ModuleNotFoundError:
            exit("There is no such module")
