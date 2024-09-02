#requires installation of pymusickit library
#source: https://pypi.org/project/pymusickit/

import os
import fnmatch
from tkinter import filedialog
from pymusickit.key_finder import KeyFinder
window = filedialog.Tk()
window.wm_attributes('-topmost', 1)
window.withdraw()   # this supress the tk window

directory = filedialog.askdirectory()

for root, dirs, files in os.walk(directory):
    for file in files:
        if fnmatch.fnmatch(file, '*.wav'):
            fullpath = os.path.join(root,file)
            print(file)
            audio_path = fullpath
            song = KeyFinder(audio_path)
            song.print_key()
            print('====================')
