from tkinter import *  # imports Tkinter
import os
import subprocess
import urllib.request
import zipfile
import sys
import Updater



def restartMain():
    """Restarts the main script"""

    print("Restarting PlayFlick...") 

    # Get the current script's filename
    script_name = sys.argv[0]

    #opens a new script
    subprocess.Popen([sys.executable, script_name])

    #closes the current script
    sys.exit()


def auto_update():
    """Checks for updates and runs updater if needed."""
    try:
        if Updater.check_for_updates():  # This function should compare local vs. GitHub version
            print("New update available! Updating now...")
            Updater.update_main_folder()
            print("Update complete. Restarting PlayFlick...")
            restartMain()
        else:
            print("PlayFlick is up to date!")
    except Exception as e:
        print(f"Update check failed: {e}")




auto_update()


try:

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

    def openSettingsWindow():
        settingsWindow = Toplevel()  
        settingsWindow.geometry("500x700")
        settingsWindow.title("Settings")
        settingsWindow.config(background=theme)
        settingsWindow.resizable(False, False)

            #makes the lable
        settingsLabel = Label(
            settingsWindow,
            text="Settings",
            font=('Arial', 40, 'bold'),
            bg=theme
        )

        settingsLabel.pack(pady= 10)


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

    #makes the Settings button
    SettingsButton = Button(
        window,
        text="Settings",
        command= openSettingsWindow
    )



    #Places the reload button
    reloadGames.pack(pady= 10)

    #Places the Update/Repair button
    UpdateRepair.pack(pady= 10)

    #Places the Settings button
    SettingsButton.pack(pady= 10)

    # Start the main loop
    window.mainloop()


except Exception as e:
    print(f"Error detected: {e}")

    confirm = input("Do you want to repair the installation? (y/n): ").strip().lower()

    if confirm in ["y", "yes"]:
        # Run the update function
        print("Repairing...")
        Updater.update_main_folder()

        # Restart the script only if update was performed
        restartMain()
