def only_four(number):
    return number % 4 == 0

def four_dividers(number):
    # return a list of numbers that are divisible by 4
    return list(filter(only_four, range(1, number + 1)))



def main():
    print(four_dividers(9))


if __name__ == '__main__':
    main()