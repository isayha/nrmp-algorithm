# Sourced and modified from a previous (CPSC 300) assignment

import sys
import os

# Obtains the name of a desired input file from the user (unless the name is pre-specified via parameter desiredFile) 
# and returns said file as a file object (if it exists):
def getInputFile(desiredFile, specifier):
    inputFile = desiredFile
    fileFound = False
    displayHints = False
    while fileFound is False:
        # If variable inputFile holds/points to a value other than None and it's value corresponds to an existing file path:
        if not (inputFile is None) and (os.path.isfile(inputFile)):
            print("File found.")
            inputFile = open(inputFile, 'r')
            fileFound = True
        else:
            # If displayHints (used as a flag) is True, or, variable inputFile holds/points to a value other than None
            # and it's value DOES NOT correspond to an existing file path:
            if displayHints or (not (inputFile is None) and not (os.path.isfile(inputFile))):
                print("File not found.")
                print("NOTE: File must be in the same working directory as the program itself.")
                print("NOTE: File extension must be included in file name.")
            displayHints = True
            if not (specifier is None):
                print("Please enter the name of the desired input file containing " + specifier + ": ")
            else:
                print("Please enter the name of the desired input file: ")
            inputFile = input()
    return inputFile

# Main input file handling:
def getData(arguments):
    hospitalData = None
    studentData = None
    if len(arguments) > 1:
        print("1st argument (hospital data file name) detected.")
        print("Finding file...")
        hospitalData = getInputFile(arguments[1], "hospital data")
        if len(arguments) > 2:
            print("2nd argument (student data file name) detected.")
            print("Finding file...")
            studentData = getInputFile(arguments[2], "student data")
        else:
            print("2nd argument (student data file name) not detected.")
            studentData = getInputFile(None, "student data")
    else:
        print("No arguments detected.")
        hospitalData = getInputFile(None, "hospital data")
        studentData = getInputFile(None, "student data")
    return hospitalData, studentData

# Data formatting issue handling:
def handleDataIssue(issue, specifier):
    if issue:
        print("Data issue detected:")
        print(specifier)
        print("Please check and/or correct data.")
        print("Exiting...")
        sys.exit(1)