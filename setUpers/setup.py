"""sometimes you may need some codes to run
before a special test. in that case you can use the
setup. the setups will be two optional functions.
one work for setting up the environment needed for
the test and another one change the situation to the
normal one. for making the setups and takedowns you
should make a function starts with one of the following names
and end with test name. for example if we have a test named A,
the setup and takedown is like this

setupA
takedownA

note for every setup a takedown is needed respectively
"""

# here methods refer to both function and method
import setUpers.errors as errors


class SetDown:

    names: list = {"setup": "setup", "takedown": "takedown"}
    SEARCH_NAMES = 0    # this is the value for searching among names
    SEARCH_ADDrESS = 1  # this is a value that determine search among addresses

    def __init__(self, allMethods):
        """these are the names of all  methods of class
        or functions containing both tests and other functions and methods"""

        self.__setDownMethods = []

        for method in allMethods:
            if method[0].startswith(self.names["setup"]) or method[0].startwith(self.names["takedown"]):
                self.__setDownMethods.append(method)

    def search(self, item, mode: int):
        """here item is something that we want to search in the list
        and the mode determines, where to search because the __SetDownMethods
        contain a tuple and each tuple have the name and address."""
        index = -1

        for method in self.__setDownMethods:
            index += 1
            if method[mode] == item:
                return index
        raise IndexError("item is not found")


    def runMethod(self, nameMethod):

        setupMethod = self.names["setup"]+str(nameMethod)
        takedownMethod = self.names["takedown"]+str(nameMethod)

        try:
            setupMethodIndex = self.search(setupMethod, self.SEARCH_NAMES)
        except IndexError:
            setupMethod = False

        try:
            takedownMethodIndex = self.search(takedownMethod, self.SEARCH_NAMES)
        except IndexError:
            takedownMethod = False

        if setupMethod is False and takedownMethod is False:
            return 0

        elif setupMethod != takedownMethod:
            raise errors.BothSetupTakedownError("expected to provide both setup and takedown method/function")

        else:
            return {"setup": self.__setDownMethods[setupMethodIndex],
                    "takedowen": self.__setDownMethods[takedownMethodIndex]}
