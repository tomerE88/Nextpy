def specific_size(path):
    # returns all the names in the file that have a specific size
    size = int(input("Enter the size: "))
    names = open(path, "r").read().splitlines()
    return '\n'.join([name for name in names if len(name) == size])


def main():
    print("specific size:\n" + specific_size("Chapter1\\SummaryExercize1.5\\names.txt"))
if __name__ == '__main__':
    main()