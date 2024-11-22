import re
import os
import fnmatch
from tkinter import filedialog
from tkinter import *
import tkinter as tk

root = tk.Tk()

w = 350
h = 290

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Sound Content File Checker')

initz = "/Users/haziqkhalid/Desktop/workspace"

def beginWord():
        fname = filedialog.askdirectory(initialdir = initz)
        os.chdir(fname)
        print('\nFolder selected:' + str(fname) + '\n')
        for prt, pdr, pfn in os.walk(fname):
            for pfns in pfn:
                if fnmatch.fnmatch(pfns, '*.wav'):
                    print(pfns)
        
        print('\nType below to insert word at the beginning (leave blank to bypass):')
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
        print('RESULTS:\n')
        for lrt, ldr, lfn in os.walk(fname):
            print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
        print('Changes made. Please check. :)\n')
        print('====================\n')

def removeWord():
        fname = filedialog.askdirectory(initialdir = initz)
        os.chdir(fname)
        print('\nFolder selected:' + str(fname) + '\n')
        for prt, pdr, pfn in os.walk(fname):
            for pfns in pfn:
                if fnmatch.fnmatch(pfns, '*.wav'):
                    print(pfns)
        
        print('\nType below to indicate word to remove (leave blank to bypass):')
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
        print('RESULTS:\n')
        for lrt, ldr, lfn in os.walk(fname):
            print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
        print('Changes made. Please check. :)\n')
        print('====================\n')

def textReplace():
        fname = filedialog.askdirectory(initialdir = initz)
        os.chdir(fname)
        print('\nFolder selected: \n' + str(fname) + '\n')
        for prt, pdr, pfn in os.walk(fname):
            for pfns in pfn:
                if fnmatch.fnmatch(pfns, '*.wav'):
                    print(pfns)
        
        print('\nType name to replace (leave blank to bypass):')
        preName = input()

        print('\nReplace with this word (leave blank to bypass):')
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
        print('RESULTS:\n')
        for lrt, ldr, lfn in os.walk(fname):
            print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
        print('Changes made. Please check. :)\n')
        print('====================\n')

def dsstoreDel():
        fname = filedialog.askdirectory(initialdir = initz)
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

        print('.DS_Store removed. Please check.\n')
        print('====================\n')

def directoryChecker():
        directory = filedialog.askdirectory(initialdir = initz)
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
            print('FAIL: No IMAGE detected, please indicate in Airtable and inform Brian or Aurial.')
        else:
            print('Pass: ' + '.jpg images detected: ' + str(no_of_imgs))
        print('---------------------------------------------------------------------\n')

def keyConverter():
        sampleFile = filedialog.askdirectory(initialdir = initz)
        os.chdir(sampleFile)
        print('\nFolder selected:' + str(sampleFile) + '\n')
        for parent, sibling, children in os.walk(sampleFile):
            for child in children:
                if fnmatch.fnmatch(child, '*.wav'):
                    print(child)

        def defineFormat():
            sampleTitleRegex = re.compile(r'_([A-G]#?b?m?(maj|min)?)_')
            return sampleTitleRegex

        def keyConverter(convert):
            if convert == r"_Db_" or convert == r"_Dbmaj_":
                sampleFileNew1 = r"_C#_"
                return sampleFileNew1
            elif convert == "_D#_" or convert == r"_D#maj_":
                sampleFileNew2 = r"_Eb_"
                return sampleFileNew2
            elif convert == r"_Gb_" or convert == r"_Gbmaj_":
                sampleFileNew3 = r"_F#_"
                return sampleFileNew3
            elif convert == r"_G#_" or convert == r"_G#maj_":
                sampleFileNew4 = r"_Ab_"
                return sampleFileNew4
            elif convert == r"_A#_" or convert == r"_A#maj_":
                sampleFileNew5 = r"_Bb_"
                return sampleFileNew5
            elif convert == "_Dbm_" or convert == r"_Dbmin_":
                sampleFileNew6 = r"_C#m_"
                return sampleFileNew6
            elif convert == r"_Ebm_" or convert == r"_Ebmin_":
                sampleFileNew7 = r"_D#m_"
                return sampleFileNew7
            elif convert == r"_Gbm_" or convert == r"_Gbmin_":
                sampleFileNew8 = r"_F#m_"
                return sampleFileNew8
            elif convert == r"_Abm_" or convert == r"_Abmin_":
                sampleFileNew9 = r"_G#m_"
                return sampleFileNew9
            elif convert == r"_A#m_" or convert == r"_A#min_":
                sampleFileNew10 = r"_Bbm_"
                return sampleFileNew10
            else:
                pass

        print('\nCONVERSION:')

        for prt, pdr, pfn in os.walk(sampleFile):
            for pfns in pfn:
                if fnmatch.fnmatch(pfns, '*.wav') and not pfns.startswith('._'):
                    mo = defineFormat().search(pfns)
                    name, ext = os.path.splitext(pfns)
                    if mo != None:
                        oldKey = mo.group()
                        newKey = keyConverter(oldKey)
                        try:
                            os.rename(prt + '/' + pfns, prt + '/' + pfns.replace(oldKey, newKey))
                            print('[' + pfns + '] '"Key converted from " + oldKey + ' to ' + newKey)
                        except TypeError:
                            print('[' + pfns + "] Unchanged.")

        print ('\nRESULTS:')

        for lrt, ldr, lfn in os.walk(sampleFile):
            for p in lfn:
                if fnmatch.fnmatch(p, '*.wav'):
                    print(p)
            
button0 = tk.Button(root, text="Directory Checker", command=directoryChecker)
button0.pack(padx=20, pady=10)
button0 = tk.Button(root, text="Key Conversion", command=keyConverter)
button0.pack(padx=20, pady=10)
button1 = tk.Button(root, text="Add Word at Beginning", command=beginWord)
button1.pack(padx=20, pady=10)
button2 = tk.Button(root, text="Remove Word in filenames", command=removeWord)
button2.pack(padx=20, pady=10)
button3 = tk.Button(root, text="Text Replacer", command=textReplace)
button3.pack(padx=20, pady=10)
button4 = tk.Button(root, text="Remove .DS_Store", command=dsstoreDel)
button4.pack(padx=20, pady=10)
root.mainloop()
