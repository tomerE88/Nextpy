# my favorite animal is a GOAT so I will create a class for it
class Goat:
    count_animals = 0 # class variable to keep track of the number of animals
    def __init__(self, name = "Octavio"):
        """
        Initializes a Goat object with a name and age of 0.
        if no name is given, the default name is Octavio
        """
        # set the name of the goat as the given name
        self._name = name
        # set the age of the goat to 0
        self._age = 0
        Goat.count_animals += 1 # add one to the count of animals

    def birthday(self):
        """
        Increments the age of the goat by one.
        """
        self._age += 1
    
    def get_age(self):
        """"
        Returns the age of the goat.
        """
        return self._age
    
    def get_name(self):
        """
        Returns the name of the goat.
        """
        return self._name
    
    def set_name(self, name):
        """
        Sets the name of the goat to the given name.
        """
        self._name = name

def main():
    """
    Create two Goat objects and test the birthday method.
    Print the age of the first goat and the second goat.
    """
    # create two goat objects
    first_goat = Goat("Lebron")
    second_goat = Goat()

    first_goat.birthday() # increment the age of the first goat
    # print the age of the first and second goat
    print("Age of first GOAT:", first_goat.get_age())
    print("Age of second GOAT:", second_goat.get_age())

    # change the name of the first goat and print
    first_goat.set_name("Lebron James")
    print("Name of first GOAT:", first_goat.get_age())

    print("Number of GOATs", Goat.count_animals) # number of goats created

if __name__ == '__main__':
    main()