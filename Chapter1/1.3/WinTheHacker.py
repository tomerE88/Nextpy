def crack_code(password):
    # returns the message before encryption
    return ''.join([chr(ord(letter) + 2) if letter.isalpha() else letter for letter in password])


def main():
    print(crack_code("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))


if __name__ == '__main__':
    main()