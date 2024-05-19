class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password
    
    def __str__(self):
        return f"The password is too short: {self._password}"
    
    def get_password(self):
        return self._password