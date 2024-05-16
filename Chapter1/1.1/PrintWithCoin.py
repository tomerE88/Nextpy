def combine_coins(coin, numbers):
    # returns the list with the coin before each number symbol and , between the numbers
    return ', '.join([coin + str(number) for number in numbers])


def main():
    print(combine_coins('$', range(5)))


if __name__ == '__main__':
    main()