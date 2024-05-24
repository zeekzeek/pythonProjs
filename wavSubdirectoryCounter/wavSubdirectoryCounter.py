import os
import fnmatch
from tkinter import filedialog

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

getSize = get_size() / 1000000
wav_count = count_wav_files(directory)
print(f"\nNumber of .wav files in {directory} and its subdirectories: {wav_count}\nTotal size: {getSize:.2f}mb\n")

if getSize > 2000:
    print('SIZE NEEDS TO BE REDUCED TO UNDER 2GB.\n')
else:
    pass
