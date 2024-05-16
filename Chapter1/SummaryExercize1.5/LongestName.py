def longest_name(path):
    """
    Reads all names from a file and returns the longest name found.

    Param:
    path (str): The file path from which to read the names.

    Returns:
    str: The longest name found in the file.
    """
    # Read all names from the file and store them as a list of strings
    names = open(path, "r").read().splitlines()
    # Return the name with the maximum length from the list of names
    return max(names, key=len)


def main():
    print("Longest name:", longest_name("Chapter1\\SummaryExercize1.5\\names.txt"))


if __name__ == '__main__':
    main()