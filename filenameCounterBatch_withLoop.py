#!/usr/bin/env python3
#V1.02 (18 January 2024)
#Added folder directory

import os
from tkinter import filedialog

print('This character counter script counts the number of characters in a filename sans extension.'
      + ' Names are sorted in numerical ascending order.')

while True:
    try:
        x = filedialog.askdirectory()
        folderName = os.listdir(x)
        try: 
            folderName.remove('.DS_Store')
        except ValueError:
            print('')

        folderNameSorted = sorted(folderName, key=len)

        print('Folder selected: ' + x + '\n')

        for i in range(len(folderNameSorted)):
            nameSplit = os.path.splitext(str(folderNameSorted[i]))
            print('The filename contains ' + str(len(nameSplit[0])) + ' characters from [' + folderNameSorted[i] +'].'
                        + ' File type: ' + nameSplit[1])

        print('\nThere are ' + str(len(folderNameSorted)) + ' files in this folder.')
    except FileNotFoundError:
            print('Program ended. Please run again.')
            break
