def is_prime(number):
    # return True if number is prime, False otherwise
    return [number % i == 0 for i in range(2, number)] == [False] * (number - 2)


def main():
    print(is_prime(7))


if __name__ == '__main__':
    main()