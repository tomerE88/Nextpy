def is_funny(string):
    # return True if the string contains only the letters 'h' and 'a', False otherwise
    return [letter.lower() == 'h' or letter.lower() == 'a' for letter in string] == [True] * len(string)


def main():
    print(is_funny("ahahahhha"))
    print(is_funny("ahhdha"))


if __name__ == '__main__':
    main()