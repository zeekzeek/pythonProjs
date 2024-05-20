import os
import fnmatch
from tkinter import filedialog

def count_wav_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, '*.wav') and not file.startswith('._'):
                count += 1
                if len(file) - 4 >= 50 :
                    print(file + " [" + str(len(file) - 4) + " characters]. Please shorten the filename to less than 50.")
                else:
                    print(file + " [" + str(len(file) - 4) + " characters].")
    return count

directory = filedialog.askdirectory()
wav_count = count_wav_files(directory)
print(f"Number of .wav files in {directory} and its subdirectories: {wav_count}")
