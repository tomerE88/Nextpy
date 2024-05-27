
def main():
    numbers = iter(list(range(1, 101)))
    
    # get every third number without using an if
    for i in numbers:
        print(i)
        next(numbers)
        next(numbers)


if __name__ == "__main__":
    main()