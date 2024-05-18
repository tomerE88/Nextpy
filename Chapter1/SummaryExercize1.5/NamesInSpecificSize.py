def specific_size(path):
    """
    Reads all names from a file, filters, and returns those that match a specific length entered by the user.

    Param:
    path (str): The file path from which to read the names.

    Returns:
    str: A string containing all names from the file that have the specified length, each name on a new line.
    """
    # Prompt the user to enter the desired size of the names and convert the input to an integer
    size = int(input("Enter the size: "))
    # Open the file, read its contents, and split into lines to get individual names
    # Filter the names to only include those that match the specified size and join them with newlines
    return '\n'.join([name for name in open(path, "r").read().splitlines() if len(name) == size])


def main():
    print("specific size:\n" + specific_size("Chapter1\\SummaryExercize1.5\\names.txt"))
if __name__ == '__main__':
    main()