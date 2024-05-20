import os
from tkinter import filedialog

fname = filedialog.askdirectory()

def remove_ds_store(fname):
    # Iterate over all files and directories in the given directory
    for root, dirs, files in os.walk(fname):
        for file in files:
            if file == ".DS_Store":
                # Create the file path
                file_path = os.path.join(root, file)
                # Remove the file
                os.remove(file_path)
                print(f"Removed: {file_path}")

# Specify the directory where you want to remove .DS_Store files
directory_to_search = "/path/to/your/directory"

# Call the function to remove .DS_Store files
remove_ds_store(directory_to_search)
