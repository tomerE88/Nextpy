def len_all_names(path):
    # returns the len of every name in the file in different lines
    names = open(path, "r").read().splitlines()
    return '\n'.join([str(len(name)) for name in names])


def main():
    print("len of al names:\n" + len_all_names("Chapter1\\SummaryExercize1.5\\names.txt"))


if __name__ == '__main__':
    main()