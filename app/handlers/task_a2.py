# app/handlers/task_a2.py
import subprocess, os

async def handle(task_description: str) -> str:
    file_path = os.path.abspath("data/format.md")
    if not os.path.exists(file_path):
        raise Exception("File /data/format.md does not exist.")
    
    # Run prettier version 3.4.2 using npx
    command = ["npx", "prettier@3.4.2", "--write", file_path]
    proc = subprocess.run(command, capture_output=True, text=True)
    if proc.returncode != 0:
        raise Exception(f"Prettier formatting failed: {proc.stderr}")
    return "Task A2 completed: /data/format.md formatted successfully."
