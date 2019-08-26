""" File_Name_Scrambler.

A simple python script that renames a specified file with a randomly generated name and file extension.
Operations conducted through a command line.

"""

__author__ = 'Anthony T. Nguyen'
__version__ = '1.0.1'
__date__ = '16.07.2019'

import optparse
import os
import string
import random

def file_name_generator():
    """ File name generator

    Function used to create a random string of characters for name and extension.

    Attributes:
        new_name: Used to store randomly created name.
        loop_number: Determines number of iterations for the for loop.
        letters: Stores single ascii letters one at a time.

    return:
        The new generated string/name.

    """
    new_name = ''
    current_loop = random.randint(1, 5)
    # Creates a new string consisting of 1 - 5 characters.
    for characters in range(current_loop):
        letters = random.choice(string.ascii_letters)
        new_name += letters
    new_name += '.'
    current_loop = random.randint(2, 3)
    # Creates a new string of 2 - 3 characters.
    for characters in range(current_loop):
        letters = random.choice(string.ascii_letters)
        new_name += letters
    return new_name

def locate_file(target_file):
    """ Locate file function.
    
    Attempts to rename the specified file.

    Attributes:
        new_name: Stores a randomly created name produced from the file_name_generator.
        
    Parameters:
        target_file: File name specified by the user.

    """
    try:
        new_name = file_name_generator()
        os.rename(target_file, new_name)
        print('[+] Target_File renamed')
    except Exception as errorMsg:
        print('[-] Unable to locate/rename target file')
        print('[-] Exact error message: ' + str(errorMsg))

def options():
    """ Options function.

    Function used to provide user options.

    """
    parser = optparse.OptionParser("usage%prog " +\
        "-t <target file>")
    parser.add_option('-t', dest='target_file', type='string', \
        help='specify target file please')
    (options, args) = parser.parse_args()
    target_file = options.target_file
    if (target_file == None):
        print("[-] Please specify a target file.")
        exit(0)
    elif (target_file == 'test.xyz'):
        print(file_name_generator())
    else:
        locate_file(target_file)

def main():
    """
    Begin
    """
    options()

if __name__ == '__main__':
    main()
