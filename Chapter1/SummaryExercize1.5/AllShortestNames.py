def all_shortest_names(path):
    # returns all the shortest names in the file and print them in different lines
    names = open(path, "r").read().splitlines()
    return '\n'.join([name for name in names if len(name) == min(len(name) for name in names)])


def main():
    print("Shortest names:\n" + all_shortest_names("Chapter1\\SummaryExercize1.5\\names.txt"))


if __name__ == '__main__':
    main()