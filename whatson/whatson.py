#music events [esplanade]
#art events [national gallery, artscience museum, singapore art museum]

import webbrowser, bs4
import tkinter as tk

root = tk.Tk()

w = 350
h = 300

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("What's on?")


def artScience():
    webbrowser.open("https://www.marinabaysands.com/museum/whats-on.html")

def espy():    
    webbrowser.open("https://www.esplanade.com/whats-on")
    
def natGal():
    webbrowser.open("https://www.nationalgallery.sg/whats-on")

def projFilm():
    webbrowser.open("https://theprojector.sg/films")

def philStu():
    webbrowser.open("https://www.philstudio-events.com/blank-1")

def singExpo():
    webbrowser.open("https://www.singaporeexpo.com.sg/sg/what-s-on/events-expo")



button0 = tk.Button(root, text="ArtScience Museum", command=artScience)
button0.pack(padx=20, pady=10)
button1 = tk.Button(root, text="Esplanade", command=espy)
button1.pack(padx=20, pady=10)
button2 = tk.Button(root, text="National Gallery", command=natGal)
button2.pack(padx=20, pady=10)
button3 = tk.Button(root, text="Projector (Films)", command=projFilm)
button3.pack(padx=20, pady=10)
button4 = tk.Button(root, text="Phil Studio Gigs", command=philStu)
button4.pack(padx=20, pady=10)
button5 = tk.Button(root, text="Singapore Expo", command=singExpo)
button5.pack(padx=20, pady=10)
root.mainloop()

#https://www.marinabaysands.com/museum/whats-on.html
#https://theprojector.sg/films
#https://www.philstudio-events.com/blank-1
