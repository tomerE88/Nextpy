def all_shortest_names(path):
    """
    Reads all names from a file, finds the shortest names, and returns them formatted
    as a single string with each name on a new line.
    
    Param:
    path (str): The file path from which to read the names.

    Returns:
    str: A string containing the shortest names from the file, each on a new line.
    """
    # Read all names from the file and store them in a list
    names = open(path, "r").read().splitlines()
    # Create a single string from all names that are of minimum length, each separated by a newline
    return '\n'.join([name for name in names if len(name) == min(len(name) for name in names)])


def main():
    print("Shortest names:\n" + all_shortest_names("Chapter1\\SummaryExercize1.5\\names.txt"))


if __name__ == '__main__':
    main()