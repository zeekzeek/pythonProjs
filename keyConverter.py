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

sampleFile = 'Chevy_138_Dbmin_Bass'

def defineFormat():
    sampleTitleRegex = re.compile(r'_([A-G]#?b?m?(maj|min)?)_')
    mo = sampleTitleRegex.search(sampleFile)
    return mo

def keyConverter(convert):
    mo = defineFormat() # scoped here

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
        print('Key not found')

#cannot get key to match to new key after the first conditional
#solution: or statement was half-assed, did not include 'convert ==' in the latter
#also re compilers to include the 'maj?' input to register the filename
#use pipe and grouping with brackets to define conditional chunk of string characters (min|maj)?

keyy = defineFormat().group()
results = keyConverter(keyy)
print(results)
