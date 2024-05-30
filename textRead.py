while True:
    print("\nHow may I help you today?\n"
          "1. List of alternatives other than watching lewd content\n"
          "\nEnter 'exit' to Exit program")
    x = input()

    if x == '1':        
        f = open(r"C:\Users\USER\Documents\journal\altp.txt", "r")
        # had to do double backslashes or raw string
        print(f.read())
        continue
    else:
        print('\nRequest invalid, program restarted.\n')
        continue

    if x == 'exit':
        print("Program ended. Bye.")
        break
        

