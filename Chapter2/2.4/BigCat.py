from BigThing import BigThing  # Import the BigThing class from the BigThing module

class BigCat(BigThing):
    def __init__(self, parameter, weight):
        """
        Initializes the BigCat object with a parameter and weight.
        Inherits the parameter handling from BigThing and adds weight management.

        Params:
        parameter: The data to store in the object, can be of any type.
        weight (float): The weight of the cat.
        """
        super().__init__(parameter)  # Correctly call the parent class's __init__ method
        self._weight = weight  # Initialize the weight attribute

    def size(self):
        """
        Returns the size of the cat based on its weight.
        """
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"
        

def main():
    my_cat = BigCat("Mitzi", 17.5)
    print("Size of my cat:", my_cat.size())

if __name__ == "__main__":
    main()
