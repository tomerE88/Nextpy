from PasswordMissingCharacter import PasswordMissingCharacter
class MissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + f" (Special) {self.get_password()}"