import re, os, fnmatch
from tkinter import filedialog
from tkinter import *
import tkinter as tk

def removeWord():
    fname = filedialog.askdirectory()
    os.chdir(fname)
    
    def remove_wav_files(fname):
        for root, dirs, files in os.walk(fname):
            for file in files:
                if fnmatch.fnmatch(file, '*.wav') and not file.startswith('._'):
                    name, ext = os.path.splitext(file)
                    sampleTitleRegex = re.compile(r'\s\d\d.')
                    mo = sampleTitleRegex.search(file)
                    print(mo.group())
                    os.rename(root + '/' + file, root + '/' + file.replace(mo.group(), ''))
                else:
                    break

   # def defineFormat(sampleFile):
    #    sampleTitleRegex = re.compile(r'_([A-G]#?b?m?(maj|min)?)_')
     #   mo = sampleTitleRegex.search(sampleFile)
      #  return mo
                    
    result = remove_wav_files(fname)
    print('\nName removed.\n')
    print('RESULTS:\n')
    for lrt, ldr, lfn in os.walk(fname):
        print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
    print('Changes made. Please check. :)\n')
    print('====================\n')
removeWord()
