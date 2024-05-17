from Animal import Animal

class Skunk(Animal):
    def __init__(self, name, hunger, stink_count = 6):
        """
        Initializes the Skunk object with a name, hunger level and stink count.
        Params:
        name (str): The name of the skunk.
        hunger (int): The hunger level of the skunk.
        stink_count (int): The stink count of the skunk, default is 6.
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count


    def talk(self):
        return "tsssss"
    
    def stink(self):
        """
        Returns my reaction to the smell of a skunk.
        """
        return "Dear lord!"
    
    def get_stink_count(self):
        """
        Returns the stink count of the skunk.
        """
        return self._stink_count