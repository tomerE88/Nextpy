from Exceptions.PasswordExceptions.PasswordMissingCharacter import PasswordMissingCharacter

class MissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + f" (Uppercase) {self.get_password()}"
