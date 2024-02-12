import os
import fnmatch
from tkinter import filedialog
window = filedialog.Tk()
window.wm_attributes('-topmost', 1)
window.withdraw()   # this supress the tk window

print('which program to execute?\n'
        + '1. add name\n'
          + '2. remove name')
userInput = input()

if userInput == '1':
    fname = filedialog.askdirectory()
    os.chdir(fname)
    print('\nFolder selected:' + str(fname) + '\n')
    print(str(os.listdir()) + '\n')
    
    print('Insert word to rename in the beginingniniging')
    preName = input()

    def add_wav_files(fname):
        for root, dirs, files in os.walk(fname):
            for file in files:
                if fnmatch.fnmatch(file, '*.wav'):
                    name, ext = os.path.splitext(file)
                    os.rename(fname + '/' + name + ext, fname + '/' + preName + name + ext)
                else:
                    break

    result = add_wav_files(fname)
    print('\nName added\n')
    print('Name List:\n')
    print(str(os.listdir()) + '\n')
    print('Name addition executed! Program closed.')
elif userInput == '2':
    fname = filedialog.askdirectory()
    os.chdir(fname)
    print('\nFolder selected:' + str(fname) + '\n')
    print(str(os.listdir()) + '\n')
    
    print('Insert word to rename in the beginingniniging')
    preName = input()

    def remove_wav_files(fname):
        for root, dirs, files in os.walk(fname):
            for file in files:
                if fnmatch.fnmatch(file, '*.wav'):
                    name, ext = os.path.splitext(file)
                    os.rename(fname + '/' + name + ext, fname + '/' + name.replace(preName, '') + ext)
                else:
                    break
                    
    result = remove_wav_files(fname)
    print('\nName removed.\n')
    print('Name List:\n')
    print(str(os.listdir()) + '\n')
    print('Name removal executed! Program closed.')
else:
    print('Invalid request. Program closed.')
