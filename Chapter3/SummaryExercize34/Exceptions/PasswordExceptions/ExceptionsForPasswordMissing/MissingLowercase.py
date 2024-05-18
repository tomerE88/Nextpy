from PasswordMissingCharacter import PasswordMissingCharacter

class MissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + f" (Lowercase) {self.get_password()}"
    