def sum_len(path):
    """
    Reads all names from a file and calculates the total sum of the lengths of all names.

    Param:
    path (str): The file path from which to read the names.

    Returns:
    int: The total sum of the lengths of all names in the file.
    """
    # Open the file, read its contents, and split into lines to get individual names
    # Calculate and return the sum of the lengths of all names using a generator expression
    return sum(len(name) for name in open(path, "r").read().splitlines())


def main():
    print("Sum of length:", sum_len("Chapter1\\SummaryExercize1.5\\names.txt"))


if __name__ == '__main__':
    main()