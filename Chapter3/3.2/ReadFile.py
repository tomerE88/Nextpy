def read_file(file_name):
    """
    read the content of a file
    :param file_name: the name of the file to read
    """
    print("__CONTENT_START__")
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print(f"__NO_SUCH_FILE__")
    else:
        print(file.read())
    finally:
        print("__CONTENT_END__")

def main():
    """
    print one file that does not exist and one that does
    """
    read_file("nosuchfile.txt")
    print("*" * 50)
    read_file("Chapter3\\3.2\\names.txt")


if __name__ == "__main__":
    main()