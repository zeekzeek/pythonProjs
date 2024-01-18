import os
from tkinter import filedialog

print('This character counter script counts the number of characters in a filename sans extension.'
      + ' Names are sorted in numerical ascending order.')

#x = os.listdir('../workspace/SPROKITBEATS presents TRAPNBLAP/LOOPS')
x = filedialog.askdirectory()
folderName = os.listdir(x)
try: 
    folderName.remove('.DS_Store')
except ValueError:
    print('')

folderNameSorted = sorted(folderName, key=len)

for i in range(len(folderNameSorted)):
    nameSplit = os.path.splitext(str(folderNameSorted[i]))
    print('The filename contains ' + str(len(nameSplit[0])) + ' characters from [' + folderNameSorted[i] +'].')

print('There are ' + str(len(folderNameSorted)) + ' files in this folder.')

