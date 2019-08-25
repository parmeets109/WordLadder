import re  # importing re for regular expressions library which helps to check a specified pattern of string
import sys  # importing re module  which is used to provide access to functions used by interpreter


def build(pattern, words, seen, list):              # Defining build function.
    return [word for word in words
            if re.search(pattern, word) and word not in seen.keys() and
            word not in list]


def checkFile(file_name):  # This function handle all the file name input errors, and opens and return the file
    try:
        file = open(file_name)
    except IOError:  # The IOError is expected when some operation fails as file cannot open if does not exist
        print("The  file does not exist or incorrect name.")
        file_name = input("Please Enter a correct file name: ")
        try:
            file = open(file_name)
        except FileNotFoundError:
            sys.exit("File does not exist. Please run program again!")
            # This function is used to exit from python after making two wrong attempts
    return file
