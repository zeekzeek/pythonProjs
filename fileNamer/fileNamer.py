#DS_Store blocks renaming

import os
import fnmatch
from tkinter import filedialog
window = filedialog.Tk()
window.wm_attributes('-topmost', 1)
window.withdraw()   # this supress the tk window

print('which program to execute?\n'
        + '1. add name\n'
          + '2. remove name\n'
          + '3. text replace')
userInput = input()

if userInput == '1':
    fname = filedialog.askdirectory()
    os.chdir(fname)
    print('\nFolder selected:' + str(fname) + '\n')
    for prt, pdr, pfn in os.walk(fname):
        print('Folder: ' + prt + '\n' + str(pfn) + '\n')
    
    print('Insert word to rename in the beginingniniging')
    preName = input()

    def add_wav_files(fname):
        for root, dirs, files in os.walk(fname):
            for file in files:
                if fnmatch.fnmatch(file, '*.wav'):
                    name, ext = os.path.splitext(file)
                    os.rename(root + '/' + file, root + '/' + preName + file)
                else:
                    break

    result = add_wav_files(fname)
    print('\nName added\n')
    print('Name List:\n')
    for lrt, ldr, lfn in os.walk(fname):
        print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
    print('Name addition executed! Program closed.')
    
elif userInput == '2':
    fname = filedialog.askdirectory()
    os.chdir(fname)
    print('\nFolder selected:' + str(fname) + '\n')
    for prt, pdr, pfn in os.walk(fname):
        print('Folder: ' + prt + '\n' + str(pfn) + '\n')
    
    print('Insert word to rename in the beginingniniging')
    preName = input()

    def remove_wav_files(fname):
        for root, dirs, files in os.walk(fname):
            for file in files:
                if fnmatch.fnmatch(file, '*.wav'):
                    name, ext = os.path.splitext(file)
                    os.rename(root + '/' + file, root + '/' + file.replace(preName, ''))
                else:
                    break
                    
    result = remove_wav_files(fname)
    print('\nName removed.\n')
    print('Name List:\n')
    for lrt, ldr, lfn in os.walk(fname):
        print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
    print('Name removal executed! Program closed.')
    
elif userInput == '3':
    fname = filedialog.askdirectory()
    os.chdir(fname)
    print('\nFolder selected:' + str(fname) + '\n')
    for prt, pdr, pfn in os.walk(fname):
        print('Folder: ' + prt + '\n' + str(pfn) + '\n')
    
    print('Search for name to replace')
    preName = input()

    print('Replace with this word')
    replaceName = input()

    def replace_wav_files(fname):
        for root, dirs, files in os.walk(fname):
            for file in files:
                if fnmatch.fnmatch(file, '*.wav'):
                    name, ext = os.path.splitext(file)
                    os.rename(root + '/' + file, root + '/' + file.replace(preName, replaceName))
                else:
                    break

    result = replace_wav_files(fname)
    print('\nName Replaced\n')
    print('Name List:\n')
    for lrt, ldr, lfn in os.walk(fname):
        print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
    print('Name addition executed! Program closed.')
else:
    print('Invalid request. Program closed.')
