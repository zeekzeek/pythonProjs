import os
import fnmatch
from tkinter import filedialog

print('which program to execute?\n'
        + '1. add name\n'
          + '2. remove name')
userInput = input()

if userInput == '1':
    print('debug no. 1')
elif userInput == '2':
    print('debug no. 2')
else:
    print('you suck')
