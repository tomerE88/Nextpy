from PasswordMissingCharacter import PasswordMissingCharacter
class MissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + f" (Digit) {self.get_password()}"