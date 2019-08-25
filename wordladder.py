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
# This function is used to check the validation of start word

def startWordCheck(word):
    while True:
        if word.isdigit():  # checks that if the input is digit then program displays an error message
            print("Word should not be a numeric.")
            word = input("Please enter a valid word:")
        elif word == "":  # checks that if input is empty then displays an error message
            print("It should not be blank.")
            word = input("please enter a valid word")
        elif len(word) < 2:  # check that if the input is less then two alphabetic characters then an error message is displayed
            print("The length of word should be greater then two alphabetic characters.")
            word = input("please enter a valid word:")
        elif word.isalpha():  # checks if word is alpha then returns the word
            word.replace(" ", "")
            return word


# This function is used to check the validation of target word
def targetWordCheck(word):
    global start  # global helps to choose a variable which is outside a function
    while True:
        if word.isdigit():  # checks that if the input is digit then program displays an error message
            print("Word should not be a numeric.")
            word = input("Please enter a valid word.\n:")
        elif word == "":  # checks that if input is empty then displays an error message
            print("It should not be blank\n")
        elif len(word) != len(
                start):  # checks that target word must of same length as start word. otherwise displays an error message
            print("Target Word must be of same length as start world.")
            word = input("Please enter valid word\n:")
        elif word.isalpha():  # checks if word is alpha then returns the word
            word.replace(" ", "")
            return word
