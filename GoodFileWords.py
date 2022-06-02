# course: cmps3500
       # lab 8
       # date: 12/4/21
       # name: Tawfic Jobah
       # description: Exception Handling in python

#CMPS 3500

# Command line utility for creating a file that contains many copies of a single word. 
#
# Usage: filewords.py FILE_NAME WORD COUNT
#
# Example: 
# $ python3 filewords.py hellos.txt hello 3
#
# Would result in the creation of a file named 'hellos.txt' with the 
# contents: 
#
# hello
# hello
# hello
#
# This utility will do nothing if the file already exists.
#
# Author: Nathan Sprague

import sys


def print_words(file_name, word, count):
    # Prints a given word to a newly created file some number of times. 

    # Arguments:
        # file_name -- A string containing the file name. 
        # word      -- A string containing the word to write. 
        # count     -- An integer indicating how many times to write the word. 

    # No return value. 
    
    print("-start of the inside of the function-")
    try:
        # Possible PermissionError or FileExistsError!
        file_obj = open(file_name, 'x')  
        for _ in range(count):
            file_obj.write(word + "\n")
        file_obj.close()

    except FileExistsError:
        print("-The file already exists-")
        sys.exit()

    print("-end of the function-")

def main():
    # The main obtains command line arguments and makes an appropriate 
    # call to the print_words function.
    
    print("-start of main-")
    try:
        file_name = sys.argv[1]   # Possible IndexError!
        word = sys.argv[2]        # Possible IndexError!
        count = int(sys.argv[3])  # Possible IndexError or ValueError!
        print("-start of the function call-")
        print_words(file_name, word, count)
        print("-after the function call-")

    except IndexError:
        print("-Incorrect number of arguments-")
        sys.exit()
    except ValueError:
        print("-the third arguement must be a integer-")
        sys.exit()
    except FileExistsError:
        print("-The file out.txt already exists in this folder-")
        sys.exit()

    print("-End of the main loop-")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("-No file permission-")