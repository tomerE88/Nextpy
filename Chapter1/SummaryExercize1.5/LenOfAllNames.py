def len_all_names(path):
    """
    Reads all names from a file, calculates the length of each name, and returns these lengths formatted 
    as a single string with each length on a new line.
    
    Param:
    path (str): The file path from which to read the names.

    Returns:
    str: A string containing the lengths of all names from the file, each length displayed on a new line.
    """
    # Read all names from the file and store them as a list of strings
    names = open(path, "r").read().splitlines()
    # Create a string from the lengths of each name, where each length is converted to string and 
    # joined into a single string with each length on a new line
    return '\n'.join([str(len(name)) for name in names])


def main():
    print("len of al names:\n" + len_all_names("Chapter1\\SummaryExercize1.5\\names.txt"))


if __name__ == '__main__':
    main()