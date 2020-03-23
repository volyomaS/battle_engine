from UnitsStack import UnitsStack


class Army:
    __stacks: tuple

    def __init__(self, *args: UnitsStack):
        if len(args) > 6:
            exit("Wrong count of stacks, maximum 6, got {}".format(len(args)))
        else:
            self.__stacks = tuple(args)

    @property
    def stacks(self):
        return self.__stacks

    def add_stack(self, stack: UnitsStack):
        if len(self.__stacks) < 6:
            self.__stacks = tuple([*self.__stacks, stack])
        else:
            exit("There is already 6 stacks")

    def del_stack(self, stack: UnitsStack):
        for s in range(0, len(self.__stacks)):
            if self.__stacks[s] == stack:
                self.__stacks = tuple([*self.__stacks[0:s], *self.__stacks[s+1:]])
                return
        exit("There is no such stack: {}".format(stack))
