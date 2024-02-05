import os
import fnmatch
from tkinter import filedialog

def count_wav_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, '*.wav'):
                count += 1
                print(file)
    return count

directory = filedialog.askdirectory()
wav_count = count_wav_files(directory)
print(f"Number of .wav files in {directory} and its subdirectories: {wav_count}")
print(wav_count)
