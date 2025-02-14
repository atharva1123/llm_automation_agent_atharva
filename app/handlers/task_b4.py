import os
import subprocess
from fastapi import HTTPException

# Define the directory where repositories should be cloned
CLONE_DIR = os.path.abspath("data/repositories")

async def handle(task_description: str) -> str:
    """ Handles Git repository cloning """
    
    # Ensure the repositories directory exists
    os.makedirs(CLONE_DIR, exist_ok=True)

    # Extract the GitHub repository URL from the task description
    words = task_description.split()
    git_url = None

    for word in words:
        if word.startswith("https://github.com/") or word.endswith(".git"):
            git_url = word
            break

    if not git_url:
        raise HTTPException(status_code=400, detail="No valid GitHub repository URL found in the task description.")

    # Get repo name from URL
    repo_name = git_url.rstrip("/").split("/")[-1].replace(".git", "")
    repo_path = os.path.join(CLONE_DIR, repo_name)

    # Check if the repo already exists
    if os.path.exists(repo_path):
        return f"Repository {repo_name} already exists at {repo_path}."

    # Run git clone command
    try:
        subprocess.run(["git", "clone", git_url, repo_path], check=True, capture_output=True, text=True)
        return f"Repository {repo_name} cloned successfully to {repo_path}."
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Git clone failed: {e.stderr}")
