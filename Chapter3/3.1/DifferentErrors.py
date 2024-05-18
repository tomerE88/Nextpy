def stopIterationError():
    """
    This function will raise a StopIteration error
    """
    iterator = iter([1, 2, 3])
    while True:
        print(next(iterator))

def zeroDivisionError():
    """
    This function will raise a ZeroDivisionError
    """
    a = 1 / 0

def assertionError():
    """
    This function will raise an AssertionError
    Assert will raise error when the condition is False
    """
    assert False

def importError():
    """
    This function will raise an ImportError
    """
    # import doesnotexists

def keyError():
    """
    This function will raise a KeyError
    because key2 does not exist in the dictionary
    """
    dictionary = {"key": "value"}
    print(dictionary["key2"])

def syntaxError():
    """
    This function will raise a SyntaxError
    """
    # print"Hello world")

def indentationError():
    """
    This function will raise an IndentationError
    because tab does not match the indentation of the function
    """
    # for i in range(10):
    # print(i)

def typrError():
    """
    This function will raise a TypeError
    because we are trying to add a string to an integer
    """
    a = 1
    b = "2"
    print(a + b)

def main():
    """
    all the functions will raise different errors
    """
    # stopIterationError()
    # zeroDivisionError()
    # assertionError()
    # importError()
    # keyError()
    # syntaxError()
    # indentationError()
    typrError()


if __name__ == "__main__":
    main()