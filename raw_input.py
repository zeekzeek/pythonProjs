from tkinter import filedialog
import os

raw_input = filedialog.askdirectory()
src = raw_input()
src = os.path.abspath(src)
