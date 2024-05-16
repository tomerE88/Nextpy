
def two_letters(my_str):
    return my_str * 2

def double_letters(my_str):
    # double each letter in a string
    return ''.join(map(two_letters, my_str))



def main():
    print(double_letters('hello world'))


if __name__ == '__main__':
    main()