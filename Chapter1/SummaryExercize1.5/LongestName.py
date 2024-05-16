def longest_name(path):
    # returns the longest name in the file
    names = open(path, "r").read().splitlines()
    return max(names, key=len)


def main():
    print("Longest name:", longest_name("Chapter1\\SummaryExercize1.5\\names.txt"))


if __name__ == '__main__':
    main()