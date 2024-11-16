import re
import os
import fnmatch
from tkinter import filedialog
from tkinter import *
import tkinter as tk

'''
C#maj
Ebmaj
F#maj
Abmaj
Bbmaj

C#min
D#min
F#min
G#min
Bbmin

'''


import re, os

sampleFile = filedialog.askdirectory()
os.chdir(sampleFile)
print('\nFolder selected:' + str(sampleFile) + '\n')
for parent, sibling, children in os.walk(sampleFile):
    for child in children:
        if fnmatch.fnmatch(child, '*.wav'):
            print(child)


#sampleFile = 'Chevy_138_A#min_Bass'


def defineFormat():
    sampleTitleRegex = re.compile(r'_([A-G]#?b?m?(maj|min)?)_')
    return sampleTitleRegex

'''
def keyConverter(convert):
    mo = defineFormat()
        
    if convert == r"_Db_" or convert == r"_Dbmaj_":
       sampleFileNew1 = sampleFile.replace(mo.group(), r"_C#maj_")
       return sampleFileNew1
    elif convert == "_D#_" or convert == r"_D#maj_":
       sampleFileNew2 = sampleFile.replace(mo.group(), r"_Ebmaj_")
       return sampleFileNew2
    elif convert == r"_Gb_" or convert == r"_Gbmaj_":
       sampleFileNew3 = sampleFile.replace(mo.group(), r"_F#maj_")
       return sampleFileNew3
    elif convert == r"_G#_" or convert == r"_G#maj_":
       sampleFileNew4 = sampleFile.replace(mo.group(), r"_Abmaj_")
       return sampleFileNew4
    elif convert == r"_A#_" or convert == r"_A#maj_":
       sampleFileNew5 = sampleFile.replace(mo.group(), r"_Bbmaj_")
       return sampleFileNew5
    elif convert == "_Dbm_" or convert == r"_Dbmin_":
       sampleFileNew6 = sampleFile.replace(mo.group(), r"_C#min_")
       return sampleFileNew6
    elif convert == r"_Ebm_" or convert == r"_Ebmin_":
       sampleFileNew7 = sampleFile.replace(mo.group(), r"_D#min_")
       return sampleFileNew7
    elif convert == r"_Gbm_" or convert == r"_Gbmin_":
       sampleFileNew8 = sampleFile.replace(mo.group(), r"_F#min_")
       return sampleFileNew8
    elif convert == r"_Abm_" or convert == r"_Abmin_":
       sampleFileNew9 = sampleFile.replace(mo.group(), r"_G#min_")
       return sampleFileNew9
    elif convert == r"_A#m_" or convert == r"_A#min_":
       sampleFileNew10 = sampleFile.replace(mo.group(), r"_Bbmin_")
       return sampleFileNew10
    else:
        pass
'''

def keyConverter(convert):
    if convert == r"_Db_" or convert == r"_Dbmaj_":
        sampleFileNew1 = r"_C#maj_"
        return sampleFileNew1
    elif convert == "_D#_" or convert == r"_D#maj_":
        sampleFileNew2 = r"_Ebmaj_"
        return sampleFileNew2
    elif convert == r"_Gb_" or convert == r"_Gbmaj_":
        sampleFileNew3 = r"_F#maj_"
        return sampleFileNew3
    elif convert == r"_G#_" or convert == r"_G#maj_":
        sampleFileNew4 = r"_Abmaj_"
        return sampleFileNew4
    elif convert == r"_A#_" or convert == r"_A#maj_":
        sampleFileNew5 = r"_Bbmaj_"
        return sampleFileNew5
    elif convert == "_Dbm_" or convert == r"_Dbmin_":
        sampleFileNew6 = r"_C#min_"
        return sampleFileNew6
    elif convert == r"_Ebm_" or convert == r"_Ebmin_":
        sampleFileNew7 = r"_D#min_"
        return sampleFileNew7
    elif convert == r"_Gbm_" or convert == r"_Gbmin_":
        sampleFileNew8 = r"_F#min_"
        return sampleFileNew8
    elif convert == r"_Abm_" or convert == r"_Abmin_":
        sampleFileNew9 = r"_G#min_"
        return sampleFileNew9
    elif convert == r"_A#m_" or convert == r"_A#min_":
        sampleFileNew10 = r"_Bbmin_"
        return sampleFileNew10
    else:
        pass

print('\nCONVERSION:')

for prt, pdr, pfn in os.walk(sampleFile):
    for pfns in pfn:
        if fnmatch.fnmatch(pfns, '*.wav') and not pfns.startswith('._'):
            mo = defineFormat().search(pfns)
            name, ext = os.path.splitext(pfns)
            oldKey = mo.group()
            newKey = keyConverter(oldKey)
            #print(pfns)
            #print(oldKey)
            #print(newKey)
            try:
                os.rename(prt + '/' + pfns, prt + '/' + pfns.replace(oldKey, newKey))
                print('[' + pfns + '] '"Key converted from " + oldKey + ' to ' + newKey)
            except TypeError:
                print('[' + pfns + "] Unchanged.")

print ('\nRESULTS:')

for lrt, ldr, lfn in os.walk(sampleFile):
    for p in lfn:
        if fnmatch.fnmatch(pfns, '*.wav'):
        #print('Folder: ' + lrt + '\n' + str(lfn) + '\n')
            print(p)

#keyy = defineFormat().group()
#print(keyy)
#cannot get key to match to new key after the first conditional
#solution: or statement was half-assed, did not include 'convert ==' in the latter
#also re compilers to include the 'maj?' input to register the filename
#use pipe and grouping with brackets to define conditional chunk of string characters (min|maj)?


#results = keyConverter(keyy)

#def replace_wav_files(sampleFile):
#    for root, dirs, files in os.walk(sampleFile):
#        for file in files:
#            if fnmatch.fnmatch(file, '*.wav') and not file.startswith('._'):
#                name, ext = os.path.splitext(file)
#                #print(file)
#                #os.rename(root + '/' + file, root + '/' + file.replace(keyy, results))
#            else:
#                break

#print(keyy)
