import sys

from UsernameTooLong import UsernameTooLong
from UsernameTooShort import UsernameTooShort
from UsernameContainsIllegalCharacter import UsernameContainsIllegalCharacter
from PasswordTooShort import PasswordTooShort
from PasswordTooLong import PasswordTooLong
from PasswordMissingCharacter import PasswordMissingCharacter
from ExceptionsForPasswordMissing.MissingLowercase import MissingLowercase
from ExceptionsForPasswordMissing.MissingUppercase import MissingUppercase
from ExceptionsForPasswordMissing.MissingDigit import MissingDigit
from ExceptionsForPasswordMissing.MissingSpecial import MissingSpecial



def check_input(username, password):
    try:
        # check username
        check_illeagal_in_username(username)
        check_illegal_username_length(username)

        # check password
        check_password_requirements(password)
        check_password_length(password)
        
    except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong) as e:
        print(f"Username Error: {e}")
    # except (PasswordMissingCharacter, PasswordTooShort, PasswordTooLong) as e:
    #     print(f"Password Error: {e}")
    except (PasswordMissingCharacter, PasswordTooShort, PasswordTooLong) as e:
        print(f"Password Error: {e}")
    else:
        # both username and password are valid
        print("Username and password are valid - OK")

    

def check_illeagal_in_username(username):
    # check if the characters in the username are only letters, digits, or underscores
    check = [ (char.isalpha() or char.isdigit() or char == '_') for char in username] == [True] * len(username)
    if not check:
        raise UsernameContainsIllegalCharacter(username)

def check_illegal_username_length(username):
    if len(username) < 3:
        raise UsernameTooShort(username)
    if len(username) > 16:
        raise UsernameTooLong(username)

def check_password_length(password):
    if len(password) < 8:
        raise PasswordTooShort(password)
    if len(password) > 40:
        raise PasswordTooLong(password)

def check_password_requirements(password):
    if not at_least_one_lower(password):
        raise MissingLowercase(password)
    if not at_least_one_letter_upper(password):
        raise MissingUppercase(password)
    if not at_least_one_digit(password):
        raise MissingDigit(password)
    if not at_least_one_special_character(password):
        raise MissingSpecial(password)

def at_least_one_lower(password):
    """
    Check if the password contains at least one lower case letter
    :param password: the password to check
    :return: True if the password contains at least one lower case , False otherwise
    """
    return [char.islower() for char in password] != [False] * len(password)

def at_least_one_letter_upper(password):
    """
    Check if the password contains at least one upper case letter
    :param password: the password to check
    :return: True if the password contains at least one upper case , False otherwise
    """
    return [char.isupper() for char in password] != [False] * len(password)

def at_least_one_digit(password):
    """
    Check if the password contains at least one digit
    :param password: the password to check
    :return: True if the password contains at least one digit, False otherwise
    """
    check = [char.isdigit() for char in password] == [False] * len(password)
    return not check

def at_least_one_special_character(password):
    """
    Check if the password contains at least one special character
    :param password: the password to check
    :return: True if the password contains at least one special character, False otherwise
    """
    check = [char in r"""!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~""" for char in password] == [False] * len(password)
    return not check




def main():
    check_input("tomer", "Hello!123password") # Username and password are valid
    check_input("to&mer", "Hello!123password") # "Username contains wrong character"
    check_input("tr", "Hello!123password") # Username too short
    check_input("tofdfdfdfdfdfdfdmer", "Hello!123password") # Username too long
    check_input("tomer", "H!!o1") # Password too short
    # password too long
    check_input("tomer", "Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo123!")
    # password missing character
    check_input("tomer", "hellooooooo123@#") # Password dont have uppercase
    check_input("tomer", "HELLOOOOOOO123@#") # Password dont have lowercase
    check_input("tomer", "Helloooooooooo@#") # Password dont have digit
    check_input("tomer", "Helloooooooooo123") # Password dont have special character


if __name__ == "__main__":
    main()