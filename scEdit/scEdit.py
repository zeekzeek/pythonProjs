#.DS_Store blocks renaming

import os
import fnmatch
from tkinter import filedialog
window = filedialog.Tk()
window.wm_attributes('-topmost', 1)
window.withdraw()   # this supress the tk window

while True:
    print('Hello, which program would you like to execute?\n'
            + '1. Add word\n'
              + '2. Remove word\n'
              + '3. Text replace\n'
              + '4. Remove .DS_Store\n'
              + '5. Check list of files with character count\n'
              + '6. exit')
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
                    if fnmatch.fnmatch(file, '*.wav') and not file.startswith('._'):
                        name, ext = os.path.splitext(file)
                        os.rename(root + '/' + file, root + '/' + preName + file)
                    else:
                        break

        result = add_wav_files(fname)
        print('\nName added\n')
        print('Name List:\n')
        for lrt, ldr, lfn in os.walk(fname):
            print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
        print('Changes made. Please check. :)\n\n')
        continue
        
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
                    if fnmatch.fnmatch(file, '*.wav') and not file.startswith('._'):
                        name, ext = os.path.splitext(file)
                        os.rename(root + '/' + file, root + '/' + file.replace(preName, ''))
                    else:
                        break
                        
        result = remove_wav_files(fname)
        print('\nName removed.\n')
        print('Name List:\n')
        for lrt, ldr, lfn in os.walk(fname):
            print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
        print('Changes made. Please check. :)\n\n')
        continue
        
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
                    if fnmatch.fnmatch(file, '*.wav') and not file.startswith('._'):
                        name, ext = os.path.splitext(file)
                        os.rename(root + '/' + file, root + '/' + file.replace(preName, replaceName))
                    else:
                        break

        result = replace_wav_files(fname)
        print('\nName Replaced\n')
        print('Name List:\n')
        for lrt, ldr, lfn in os.walk(fname):
            print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
        print('Changes made. Please check. :)\n\n')
        continue

    if userInput == '4':
        fname = filedialog.askdirectory()
        os.chdir(fname)
        def remove_ds_store(fname):
        # Iterate over all files and directories in the given directory
            for root, dirs, files in os.walk(fname):
                for file in files:
                    if file == ".DS_Store":
                        # Create the file path
                        file_path = os.path.join(root, file)
                        # Remove the file
                        os.remove(file_path)
                        print(f"Removed: {file_path}")
                    else:
                        break

        # Specify the directory where you want to remove .DS_Store files
        directory_to_search = fname

        # Call the function to remove .DS_Store files
        remove_ds_store(directory_to_search)

        print('.DS_Store removed. Please check.\n\n')
        continue
    
    if userInput == '5':
        def count_wav_files(directory):
            count = 0
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if fnmatch.fnmatch(file, '*.wav') and not file.startswith('._'):
                        count += 1
                        if len(file) - 4 >= 50:
                            print(file + " [" + str(len(file) - 4) + " characters]. Please shorten the filename to less than 50.")
                        else:
                            print(file + " [" + str(len(file) - 4) + " characters].")
            return count

        directory = filedialog.askdirectory()
        wav_count = count_wav_files(directory)
        print(f"Number of .wav files in {directory} and its subdirectories: {wav_count}\n\n")
        continue

    if userInput == '6':
        print('Program ended. Bye bye.\n')
        break
    
    else:
        print('Invalid request. Program restarted.\n\n')
        continue

