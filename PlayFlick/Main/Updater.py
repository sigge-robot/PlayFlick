import os
import shutil
import urllib.request
import zipfile
import sys

# Get the path of the current script's directory (inside 'main')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)  # Playflick directory

# Define the 'main' folder path in Playflick
MAIN_DIR = os.path.join(PROJECT_DIR, "main")

# URL to the zipped main folder from GitHub (replace with your actual URL)
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

# Run the update process
update_main_folder()
