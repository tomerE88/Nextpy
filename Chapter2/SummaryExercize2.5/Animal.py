

class Animal():
    zoo_name = "Hayaton"
    def __init__(self, name, hunger = 0):
        """
        Initializes the Animal object with a name and hunger level.
        Params:
        name (str): The name of the animal.
        hunger (int): The hunger level of the animal, default is 0.
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        Returns the name of the animal.
        """
        return self._name
    
    def is_hungry(self):
        """
        Returns True if the animal is hungry, False otherwise.
        """
        return self._hunger > 0
    
    def feed(self):
        """
        Decreases the hunger level of the animal by 1.
        """
        self._hunger -= 1

    def talk(self):
        pass

def main():
    from Cat import Cat
    from Dog import Dog
    from Dragon import Dragon
    from Skunk import Skunk
    from Unicorn import Unicorn
    # create all animals
    dog = Dog("Omega", 10)
    cat = Cat("Mitzi", 3)
    dragon = Dragon("Smaug", 0)
    skunk = Skunk("Dirty omega", 7)
    unicorn = Unicorn("Rainbow", 150)
    newdog = Dog("Doggo", 80)
    newcat = Cat("Kitty", 80)
    newdragon = Dragon("McFly", 80)
    newskunk = Skunk("Stinky Jr.", 80)
    newunicorn = Unicorn("Clair", 80)
    # list of all animals
    zoo_lst = [dog, cat, dragon, skunk, unicorn, newdog, newcat, newdragon, newskunk, newunicorn]

    
    for animal in zoo_lst:
        # print type of animal and name
        print(f"{type(animal).__name__} {animal.get_name()}")

        while animal.is_hungry():
            # feed the animal
            animal.feed()

        print(animal.talk())

        # check what is the animal and print the special method
        if isinstance(animal, Cat):
            print(animal.chase_laser())

        elif isinstance(animal, Dog):
            print(animal.fetch_stick())

        elif isinstance(animal, Dragon):
            print(animal.breathe_fire())
            print("Color:", animal.get_color())

        elif isinstance(animal, Skunk):
            print(animal.stink())
            print("Stink count:", animal.get_stink_count())

        elif isinstance(animal, Unicorn):
            print(animal.sing())


        print()
    
    # print the zoo name
    print(f"Welcome to the {Animal.zoo_name} zoo!")

if __name__ == "__main__":
    main()