from Animal import Animal

class Dragon(Animal):
    def __init__(self, name, hunger, color = "Green"):
        """
        Initializes the Dragon object with a name, hunger level and color.
        Params:
        name (str): The name of the dragon.
        hunger (int): The hunger level of the dragon.
        color (str): The color of the dragon, default is "Green".
        """
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        return "Raaaawr"
    
    def breathe_fire(self):
        """
        Returns the anger of the dragon before breathing fire.
        """
        return "$@#$#@$"
    
    def get_color(self):
        """
        Returns the color of the dragon.
        """
        return self._color