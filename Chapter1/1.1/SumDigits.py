import functools

def add(x, y):
    return x + y

def sum_digits(number):
    # sum all the digits of a number
    # map the number to a string, then map the string to an integer
    return functools.reduce(add, map(int, str(number)))

def main():
    print(sum_digits(1047))


if __name__ == '__main__':
    main()