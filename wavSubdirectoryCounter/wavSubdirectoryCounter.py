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
