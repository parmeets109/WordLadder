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
# This function is used to check the word that must exist on the path
def MustWordCheck(word):
    global start
    while True:
        if word.isdigit():  # checks that if the input is digit then program displays an error message
            print("Word should not be a numeric.")
            word = input("Please enter a valid word.\n:")
        elif len(word) !=0 and len(word) != len(start):  # checks that target word must of same length as start word. otherwise displays an error message
            print("Necessary Word must be of same length as start word.")
            word = input("Please enter valid word\n:")
        else:
            return word


# This function is used to create a list of words that should not exist in the path
def blacklisted(words):
    blacklist_words = words.split(',')
    return blacklist_words


# This function is used to provide a path selection for the user
def pathSelection(path):
    path.lower()
    while True:
        if path.isdigit():
            print(" Invalid")
            path = input("please select either longer(L) or shorter(S) ").lower()
        elif path == "":
            print("Invalid")
            path = input("please select either longer(L) or shorter(S)").lower()

        else:
            if path == 'l':
                return False
            elif path == 's':
                return True
            else:
                path = input("please select either longer(L) or shorter(S)").lower()
                continue


#  This function is used to  returns a number of letters and indexes for two words that  exactly same
def same(item, target):
    return len([item for (item, target) in zip(item, target) if item == target])

# this function starts the main task of program i.e. to find a path

def find(word, words, seen, target, path):
    global path_select  # global helps to choose a variable which is outside a function
    global counter  # global helps to choose a variable which is outside a function
    list = []
    for i in range(len(word)):
        list += build(word[:i] + "." + word[i + 1:], words, seen, list)  # uses '.' as a wild card
    if len(list) == 0:
        return False

    if path_select:
        list = sorted([(same(w, target), w) for w in list], reverse=True)
    else:
        counter = []
        list = sorted([(same(w, target), w) for w in list])
    for (match, item) in list:
        for letter in counter:
            if letter in item:
                list.remove((match, item))
        if match >= len(target) - 1:
            if match == len(target) - 1:
                path.append(item)
            return True
        seen[item] = True
    for (match, item) in list:
        path.append(item)
        if find(item, words, seen, target, path):
            return True
        path.pop()


# Input section
# here start all of the functions of the program


file_name = input("Enter dictionary name: ")  # allows the user to input the name of the dictionary file i.e. a txtfile
file = checkFile(file_name)  # checkFile returns the file if it exists or input correctly
lines = file.readlines()
cnt = 0
while True:

    # while loop include all the required inputs
    word = input("Please enter start word from dictionary:")  # allows the user to input  a start word from dictionary
    start = startWordCheck(word)  # return the start word if  valid

    word = input("please enter a word from dictionary that must exist and should be of same length as start word:")  # allows the user to input  a neccessary word from dictionary
    must = MustWordCheck(word)  # return the necessary word if  valid

    word = input("Please enter target word from dictionary of same length as start word:")  # allows the user to input  a target word from dictionary
    target = targetWordCheck(word)  # return the target word if  valid

    path = input("please select either a longer path or short path by selecting 'L' or 'S':")  # allows the user to select  desired path
    path_select = pathSelection(path.lower())  # pathSelection returns the path if valid

    wordsList = str(input("Please insert a list of words separated by commas that should not be on the path:")).replace(" ", "")  # allows the user to input  a list words from dictionary which should not be displayed on path
    blacklistWords = blacklisted(wordsList)
    words = []
    for line in lines:
        element = line.rstrip()
        if len(element) == len(start) and element not in blacklistWords and element.isalpha():
            words.append(element)

    break

count = 0
counter = []
path = [start]
seen = {start: True}

if len(must)==0:
    if find(start, words, seen, target, path):
        path.append(target)
        print(len(path) - 1, path)
else:
    if find(start, words, seen, must, path):
        path.append(must)
        if find(must, words, seen, target, path):
            path.append(target)
            print(len(path) - 1, path)
    else:
        print("No path found")
