class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self._username = username
    
    def __str__(self):
        return f"The username contains illegal characters: {self._username}"
    
    def get_username(self):
        return self._username