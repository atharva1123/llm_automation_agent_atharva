import os
import subprocess
import asyncio
import requests
import sys

# Set the correct data directory at the project root (not inside `app/`)
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data")  # Go up two levels
os.makedirs(DATA_DIR, exist_ok=True)  # Ensure the data folder exists

async def handle(task_description: str):
    user_email = "atharvaaathawale@gmail.com"

    # Download the datagen.py script
    url = "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to download datagen.py")
    
    # Save script inside the correct `data/` folder at project root
    script_path = os.path.join(DATA_DIR, "datagen.py")
    with open(script_path, "w") as file:
        file.write(response.text)

    print(f"Saved datagen.py to: {script_path}")
    
    # Run the script inside `data/`
    proc = await asyncio.create_subprocess_exec(
        sys.executable, script_path, user_email,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=DATA_DIR  # Ensure script runs in `data/`
    )
    stdout, stderr = await proc.communicate()
    
    if proc.returncode != 0:
        print(f"Error running datagen.py: {stderr.decode()}")
        raise Exception(f"datagen.py failed: {stderr.decode()}")

    print("✅ datagen.py executed successfully. Files should be in `data/` folder.")

# Run the async function
if __name__ == "__main__":
    asyncio.run(handle("task A1 - generate data"))
