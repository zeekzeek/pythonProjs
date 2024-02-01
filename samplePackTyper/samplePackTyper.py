import pyperclip

print("Hullo, how many packs would you like to print out?")
numberOfPacks = input()

for batch in range(int(numberOfPacks)):
    
    print("Hello there, what type is the filename? \n "
          + "Enter '1' for White Label \n Enter '2' for Artist Pack\n" +
          " Enter '3' for Label \n" +
          " Enter '4' for Licensed"
      )
    packType = input()

    if packType == '1':
        packType = "White Label"
    elif packType == '2':
        packType = "Artist"
    elif packType == '3':
        packType = "Label"
    elif packType == '4':
        packType = "Licensed"

    print('What is the pack name? Pack name will be formatted and copied')
    packName = input()

    print("What date is it scheduled for release?")
    dateReleased = input()

    result = "Sample Pack (" + packType + "): " + packName + " (due: " + dateReleased + ")\n"
    print("\n" + result)
    pyperclip.copy(result)
