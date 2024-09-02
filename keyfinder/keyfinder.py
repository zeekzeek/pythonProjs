#requires installation of pymusickit library
#source: https://pypi.org/project/pymusickit/

import os
import fnmatch
from tkinter import filedialog
from pymusickit.key_finder import KeyFinder
window = filedialog.Tk()
window.wm_attributes('-topmost', 1)
window.withdraw()   # this supress the tk window

while True:
    print('Hello, which program would you like to execute?\n'
            + '1. Key match + likely match\n'
            + '2. Chromatic analysis [Expanded results]\n'
            + '3. Stop program')
    userInput = input()

#------------------------------------------------------------------
    if userInput == '1':        
        directory = filedialog.askdirectory()

        print('Key detection initialized\n'
              + 'Loading...\n'
              + '====================')

        for root, dirs, files in os.walk(directory):
            for file in files:
                if fnmatch.fnmatch(file, '*.wav'):
                    fullpath = os.path.join(root,file)
                    print(file)
                    audio_path = fullpath
                    song = KeyFinder(audio_path)
                    print('--------------------')
                    song.print_key()
                    print('====================')
                else:
                    break
        continue
#------------------------------------------------------------------
    if userInput == '2':        
        directory = filedialog.askdirectory()
        
        print('Chromatic detection initialized\n'
              + 'Loading...\n'
              + '====================')
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if fnmatch.fnmatch(file, '*.wav'):
                    fullpath = os.path.join(root,file)
                    print(file)
                    audio_path = fullpath
                    song = KeyFinder(audio_path)
                    print('--------------------')
                    song.print_chroma()
                    song.print_key()
                    print('====================')
                else:
                    break
        continue
#------------------------------------------------------------------
    if userInput == '3':
        print('Program ended. Bye bye.\n')
        break
    else:
        print('Invalid request. Program restarted.\n\n')
        continue

