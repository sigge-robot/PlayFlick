import urllib.request
import os
import time

# 🔹 Get the correct folder where both update.py and main.py are located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_PY_PATH = os.path.join(BASE_DIR, "main.py")

# 🔹 Replace with your raw GitHub URL
GITHUB_URL = "https://raw.githubusercontent.com/sigge-robot/PlayFlick/refs/heads/main/New%20minigames/Main/Main.py"

def update_main():
    try:
        print("Downloading new main.py...")
        
        # Download the file and save it to the correct folder
        urllib.request.urlretrieve(GITHUB_URL, MAIN_PY_PATH)
        
        print("Update successful! Restarting launcher...")

        # (Optional) Restart main.py
        time.sleep(1)
        os.system(f"python \"{MAIN_PY_PATH}\"")
    
    except Exception as e:
        print("Error updating:", e)

update_main()
