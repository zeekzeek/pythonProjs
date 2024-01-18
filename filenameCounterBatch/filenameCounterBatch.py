import os
from tkinter import filedialog

print('This character counter script is only accurate with filenames that end with formats with 4 characters.'
      + ' Names are sorted in ascending order.')

#x = os.listdir('../workspace/SPROKITBEATS presents TRAPNBLAP/LOOPS')
x = filedialog.askdirectory()
folderName = os.listdir(x)
folderNameSorted = sorted(folderName, key=len)

for i in range(len(folderNameSorted)): 
    print('The filename contains ' + str(len(folderNameSorted[i])-4) + ' characters from [' + folderNameSorted[i] +'].')
