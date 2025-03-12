from tkinter import *  # imports Tkinter
import os
import subprocess
import urllib.request
import zipfile
import sys
import Updater

# Create main window
window = Tk()
theme = "#00bbff"

window.geometry("500x500")
window.title("Main Menu")
window.config(background=theme)
window.resizable(False, False)

#makes the lable
titleLabel = Label(
    window,
    text="PlayFlick",
    font=('Arial', 40, 'bold'),
    bg=theme
)
titleLabel.pack(pady=10)  # Places the lable


# Get the current script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Move up one level and into the "Games" folder
SCRIPT_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "Games"))

def run_script(script_name):
    """Function to execute the selected script"""
    script_path = os.path.join(SCRIPT_FOLDER, script_name)
    if os.path.exists(script_path):
        subprocess.run(["python", script_path])  # Run the script
    else:
        print(f"Error: {script_path} not found!")

def create_buttons():
    """Scan folder and create buttons for each .py file"""
    if not os.path.exists(SCRIPT_FOLDER):
        print(f"Error: Folder '{SCRIPT_FOLDER}' not found.")
        return
    
    
    py_files = [f for f in os.listdir(SCRIPT_FOLDER) if f.endswith(".py")]

    if not py_files:
        label = Label(window, text="No games found!", font=("Arial", 12), bg=theme)
        label.pack(pady=10)

    for filename in py_files:
        button = Button(window, text=filename, command=lambda f=filename: run_script(f))
        button.pack(pady=5)

def restartMain():
    """Restarts the main script"""

    print("Restarting Main.py...") 

    # Get the current script's filename
    script_name = sys.argv[0]

    #opens a new script
    subprocess.Popen([sys.executable, script_name])

    #closes the current script
    sys.exit()

# Generate buttons for Python scripts
create_buttons()


#makes the reload button
reloadGames = Button(
    window,
    text="Reload games",
    command=restartMain,
)

#makes the Update/Repair button
UpdateRepair = Button(
    window,
    text="Update/Repair",
    command=lambda: (Updater.update_main_folder(), restartMain()),
)


#Places the reload button
reloadGames.pack(pady= 30)

#Places the Update/Repair button
UpdateRepair.pack()

# Start the main loop
window.mainloop()
