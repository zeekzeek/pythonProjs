import re
import os
import fnmatch
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import re, os

'''
Notes to convert: 
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

sampleFile = filedialog.askdirectory()
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
        if fnmatch.fnmatch(pfns, '*.wav'):
            print(p)


