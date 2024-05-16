def sum_len(path):
    # returns the sum of the length of all names in the file
    names = open(path, "r").read().splitlines()
    return sum(len(name) for name in names)


def main():
    print("Sum of length:", sum_len("Chapter1\\SummaryExercize1.5\\names.txt"))


if __name__ == '__main__':
    main()