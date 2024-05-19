class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self.__password = password
        
    def __str__(self):
        return "Password missing character:"
    
    def get_password(self):
        return self.__password