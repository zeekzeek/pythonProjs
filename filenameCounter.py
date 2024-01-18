#count number of characters in a string

while True:
    print('Input file name.')
    fileName = input()

    print('The file name has ' + str(len(fileName)) + ' characters.')
    #continue [not necessary to have continue] -- when is it necessary?
    #ans: to skip line in list is one example
    if fileName == '':
        break
print('Session ended.')
