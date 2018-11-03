import os
import sys
import fileinput
from os import listdir
from os.path import isfile, join
import glob

#Gets only file names present inside a directory
#onlyfiles = [f for f in listdir('C:\GitHub\Py-Scripts') if isfile(join('C:\GitHub\Py-Scripts',f))]

#Gets all the .txt file names from specified directory and their sub directories
#and stores it in an array
fileNames = glob.glob('Enter the path here' + '/**/*.txt', recursive=True)

for names in fileNames:
    # Read in the file
    with open(names, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('Enter the text to be matached', 'Enter the text to be replaced with')

    # Write the file out again
    with open(names, 'w') as file:
        file.write(filedata)
