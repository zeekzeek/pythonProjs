import os
import fnmatch
from tkinter import filedialog

def count_dsstore_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
            for di in dirs:
                for file in files:
                    if fnmatch.fnmatch(file, '*.DS_Store'):
                        count += 1
                        combo = os.path.join(root,di,file)
                        print(file)
                        #os.remove(root + '/' + file)
                        #print(file)
                        #print('.DS_Store eradicated.')
                        #if len(file) - 4 >= 50:
                            #print(file + " [" + str(len(file) - 4) + " characters]. Please shorten the filename to less than 50.")
                        #else:
                            #print(file + " [" + str(len(file) - 4) + " characters].")
                        print("Success.")
    return count

directory = filedialog.askdirectory()
dsstore_count = count_dsstore_files(directory)
print(f"Number of .DS_Store files in {directory} and its subdirectories: {dsstore_count}")
