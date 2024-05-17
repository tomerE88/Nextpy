class BigThing:
    def __init__(self, parameter):
        self._parameter = parameter

    def size(self):
        # if parameter is an integer, set the parameter to the integer
        if isinstance(self._parameter, int):
            return self._parameter
        # if parameter is a list, dictionary, or string, set the parameter to the length of the parameter
        elif isinstance(self._parameter, (list, dict, str)):
            return len(self._parameter)
        # if parameter is not an integer, list, dictionary, or string, set the parameter to 0
        else:
            return 0

def main():
    my_thing = BigThing("Mitzi")
    print("Size:", my_thing.size())

if __name__ == "__main__":
    main()