class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password
    
    def __str__(self):
        return f"The password is too Long: {self._password}"
    
    def get_password(self):
        return self._password