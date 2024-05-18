def len_all_names(path):
    """
    Reads all names from a file, calculates the length of each name, and writes the lengths to a new file.
    
    Param:
    path (str): The file path from which to read the names.
    """
    # open a file in write mode to store the lengths of the names
    names_file = open("Chapter1\\SummaryExercize1.5\\name_lenght.txt", "w")
    # Read all names from the file and store them as a list of strings, split by new lines
    # Create a string from the lengths of each name, where each length is converted to string and 
    # joined into a single string with each length on a new line
    names_file.write('\n'.join([str(len(name)) for name in open(path, "r").read().splitlines()]))


def main():
    len_all_names("Chapter1\\SummaryExercize1.5\\names.txt")
    print("created the file")


if __name__ == '__main__':
    main()