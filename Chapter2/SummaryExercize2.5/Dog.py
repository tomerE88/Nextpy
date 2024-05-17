from Animal import Animal

class Dog(Animal):
    def talk(self):
        return "woof woof"
    
    def fetch_stick(self):
        """
        Returns the sound of a really polite dog,
        this dog is so polite that it will return the stick to you.
        """
        return "There you go, sir!"