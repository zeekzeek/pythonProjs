#music events [esplanade]
#art events [national gallery, artscience museum, singapore art museum]

import webbrowser, bs4
import tkinter as tk

root = tk.Tk()

w = 350
h = 230

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("What's on?")

while True:
    print('What plans may you be interested in?\n' +
          '1. Nat Gal\n' +
          '2. Esplanade\n' +
          '3. Artscience Museum\n'
          '4. Projector (Films)')
    userInput = input()

    if userInput == '1':
    
        webbrowser.open("https://www.nationalgallery.sg/whats-on")

    elif userInput == '2':
        
        webbrowser.open("https://www.esplanade.com/whats-on")

    elif userInput == '3':

        webbrowser.open("https://www.marinabaysands.com/museum/whats-on.html")

    elif userInput == '4':

        webbrowser.open("https://theprojector.sg/films")

    else:
        continue

#https://www.marinabaysands.com/museum/whats-on.html
#https://theprojector.sg/films
#https://www.philstudio-events.com/blank-1
