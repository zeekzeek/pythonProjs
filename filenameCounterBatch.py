import os
from tkinter import filedialog

print('This character counter script is only accurate with filenames that end with formats with 4 characters.')

#x = os.listdir('../workspace/SPROKITBEATS presents TRAPNBLAP/LOOPS')
x = filedialog.askdirectory()
folderName = os.listdir(x)

for i in range(len(folderName)): 
    print('The filename contains ' + str(len(folderName[i])-4) + ' characters from [' + folderName[i] +'].')
    print (folderName[0])
