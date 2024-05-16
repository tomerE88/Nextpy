def intersection(list_1, list_2):
    # return a list of numbers that are in both lists, wont return duplicates
    return list(number for number in set(list_1) if number in set(list_2))



def main():
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))


if __name__ == '__main__':
    main()