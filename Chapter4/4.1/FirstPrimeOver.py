def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def first_prime_over(n):
    """
    Find the first prime number greater than n using generator expressions
    :param n: An integer
    """
    while True:
        if is_prime(n):
            yield n
        n += 1


def main():
    print(next(first_prime_over(1000000)))


if __name__ == "__main__":
    main()