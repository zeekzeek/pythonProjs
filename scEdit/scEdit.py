#.DS_Store blocks renaming

import os
import fnmatch
from tkinter import filedialog
window = filedialog.Tk()
window.wm_attributes('-topmost', 1)
window.withdraw()   # this supress the tk window

while True:
    print('Hello, which program would you like to execute?\n'
            + '1. Add word at the beginning\n'
              + '2. Remove word\n'
              + '3. Text replace\n'
              + '4. Remove .DS_Store\n'
              + '5. Check list of files with character count\n'
              + '6. Exit program')
    userInput = input()

#------------------------------------------------------------------------------    
    if userInput == '1':
        fname = filedialog.askdirectory()
        os.chdir(fname)
        print('\nFolder selected:' + str(fname) + '\n')
        for prt, pdr, pfn in os.walk(fname):
            print('Folder: ' + prt + '\n' + str(pfn) + '\n')
        
        print('Insert word at the beginning')
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

#------------------------------------------------------------------------------
    elif userInput == '2':
        fname = filedialog.askdirectory()
        os.chdir(fname)
        print('\nFolder selected:' + str(fname) + '\n')
        for prt, pdr, pfn in os.walk(fname):
            print('Folder: ' + prt + '\n' + str(pfn) + '\n')
        
        print('Please indicate word to remove')
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
#------------------------------------------------------------------------------
    elif userInput == '3':
        fname = filedialog.askdirectory()
        os.chdir(fname)
        print('\nFolder selected: \n' + str(fname) + '\n')
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
#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------
    if userInput == '5':
        directory = filedialog.askdirectory()
        def count_wav_files(directory):
            count = 0
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if fnmatch.fnmatch(file, '*.wav') and not file.startswith('._'):
                        count += 1
                        fullpath = os.path.join(root, file)
                        sizeText = os.path.getsize(fullpath) / 1000000
                        if len(file) - 4 >= 50 :
                            print(file + " [" + str(len(file) - 4) + f" characters]. Please shorten the filename to less than 50. ~Size: {sizeText:.2f}mb~")
                        else:
                            print(file + " [" + str(len(file) - 4) + f" characters]. ~Size: {sizeText:.2f}mb~")
            return count

        def get_size(start_path = '.'):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(directory):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    # skip if it is symbolic link
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)

            return total_size

        def detect_img(start_path = '.'):
            pic_img = 0
            for picpath, picdir, picfiles in os.walk(directory):
                for p in picfiles:
                    if fnmatch.fnmatch(p, '*.jpg'):
                        pic_img += 1
                        picPath = os.path.join(picpath, p)
                        print('[' + p + ']' + ' No. of files detected: ' + str(pic_img))
                    #else:
                        #print('No file detected, please indicate in Airtable and inform Brian.')
            return pic_img
                    

        getSize = get_size() / 1000000
        wav_count = count_wav_files(directory)
        print(f"\nNumber of .wav files in {directory} and its subdirectories: {wav_count}\nTotal size: {getSize:.2f}mb\n")

        print('---------------------------------------------------------------------')
        print('ALERTS: \n')

        print('Size checker:')
        if getSize > 2000:
            print('FAIL: SIZE NEEDS TO BE REDUCED TO UNDER 2GB.\n')
        else:
            print('Pass: Size is adequate.\n')

        print('Image checker:')
        no_of_imgs = detect_img()
        if no_of_imgs < 1:
            print('FAIL: No IMAGE detected, please indicate in Airtable and inform Brian.')
        else:
            print('Pass: ' + '.jpg images detected: ' + str(no_of_imgs))
        print('---------------------------------------------------------------------\n')
        continue
#------------------------------------------------------------------------------
    if userInput == '6':
        print('Program ended. Bye bye.\n')
        break
    
    else:
        print('Invalid request. Program restarted.\n\n')
        continue

