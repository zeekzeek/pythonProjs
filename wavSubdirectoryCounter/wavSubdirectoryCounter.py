import os
import fnmatch
from tkinter import filedialog

def count_wav_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, '*.wav') and not file.startswith('._'):
                count += 1
                fullpath = os.path.join(root, file)
                sizeText = os.path.getsize(fullpath) / 1000000
                if len(file) - 4 >= 50 :
                    print(file + " [" + str(len(file) - 4) + " characters]. Please shorten the filename to less than 50. . ~Size: {sizeText:.2f}mb~")")
                else:
                    print(file + " [" + str(len(file) - 4) + f" characters]. ~Size: {sizeText:.2f}mb~")
    return count

directory = filedialog.askdirectory()
wav_count = count_wav_files(directory)
print(f"Number of .wav files in {directory} and its subdirectories: {wav_count}")
