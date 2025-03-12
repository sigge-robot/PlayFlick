import os
import shutil
import urllib.request
import zipfile
import sys
        

# The path to the version.txt in github        
GITHUB_VERSION_URL = "https://raw.githubusercontent.com/sigge-robot/PlayFlick/refs/heads/main/PlayFlick/Main/version.txt"

#The local version file
LOCAL_VERSION_FILE = os.path.join(os.path.dirname(__file__), "version.txt")


# Get the path of the current script's directory (inside 'main')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)  # Playflick directory

# Define the 'main' folder path in Playflick
MAIN_DIR = os.path.join(PROJECT_DIR, "main")

# URL to the zipped main folder from GitHub 
GITHUB_ZIP_URL = "https://github.com/sigge-robot/PlayFlick/archive/refs/heads/main.zip"
TEMP_ZIP = "main_update.zip"


def update_main_folder():

    try:
        print("Checking for folder access...")
        
        # Check if the user has permission to write to the folder
        if not os.access(PROJECT_DIR, os.W_OK):
            print(f"Error: You do not have permission to write to {PROJECT_DIR}. Please check folder permissions.")
            sys.exit(1)

        print("Downloading the latest main folder from GitHub...")
        
        # Download the zip file of the main folder from GitHub
        urllib.request.urlretrieve(GITHUB_ZIP_URL, TEMP_ZIP)
        
        print("Download complete. Extracting contents...")

        # Extract the zip file to the parent directory (Playflick)
        with zipfile.ZipFile(TEMP_ZIP, 'r') as zip_ref:
            zip_ref.extractall(PROJECT_DIR)  # Extract into Playflick directory
        
        print("Extraction complete. Replacing old main folder...")

        # Delete the old 'main' folder if it exists
        if os.path.exists(MAIN_DIR):
            print(f"Removing old main folder at: {MAIN_DIR}")
            shutil.rmtree(MAIN_DIR)

        # Move the newly extracted 'main' folder to the correct location
        new_main_folder = os.path.join(PROJECT_DIR, "PlayFlick-main", "PlayFlick", "main")  # Adjust based on folder structure
        if not os.path.exists(new_main_folder):
            print("Error: New 'main' folder not found after extraction.")
            sys.exit(1)

        shutil.move(new_main_folder, MAIN_DIR)

        # Clean up the temporary files
        os.remove(TEMP_ZIP)
        shutil.rmtree(os.path.join(PROJECT_DIR, "PlayFlick-main"))

        print("Update complete! The 'main' folder has been successfully replaced.")

    except Exception as e:
        print("Error during update:", e)



def get_local_version():
    """Reads the local version file """

    if os.path.exists(LOCAL_VERSION_FILE):
        with open(LOCAL_VERSION_FILE, "r") as f:
            return f.read().strip()
    return "0"


def get_latest_version():
    """Gets the version file from GitHub"""

    try:
        response = urllib.request.urlopen(GITHUB_VERSION_URL)
        return response.read().decode().strip()
    except:
        return "0"



def check_for_updates():
    """Returns True if an update is available."""
    return get_latest_version() > get_local_version()
