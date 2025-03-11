from tkinter import *  # imports Tkinter
import os
import subprocess

#test
# Create main window
window = Tk()
theme = "#00bbff"

window.geometry("500x500")
window.title("Main Menu")
window.config(background=theme)
window.resizable(False, False)

titleLabel = Label(
    window,
    text="PlayFlick",
    font=('Arial', 40, 'bold'),
    bg=theme
)
titleLabel.pack(pady=10)  # Pack the label correctly

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

# Generate buttons for Python scripts
create_buttons()

# Start the main loop
window.mainloop()
