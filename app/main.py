from fastapi import FastAPI, HTTPException, Query
import os
from app.task_parser import parse_and_execute_task

app = FastAPI()

# ✅ Set the correct absolute path for the data directory
DATA_DIR = os.path.abspath("E:/Atharva/Projects/llm_automation_agent_atharva/data")

def validate_path(path: str) -> str:
    """ Ensure that file requests are inside the allowed data directory. """
    
    # ✅ Convert relative paths to absolute paths safely
    safe_path = os.path.abspath(os.path.join(DATA_DIR, os.path.normpath(path)))

    # ✅ Allow paths only within the "data" directory
    if not safe_path.startswith(DATA_DIR):
        raise ValueError("Access denied: file outside of data directory is not allowed.")

    return safe_path

@app.post("/run")
async def run_task(task: str = Query(..., description="Plain-English task description")):
    try:
        result = await parse_and_execute_task(task)
        return {"status": "success", "message": result}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file(path: str = Query(..., description="File path relative to the data directory")):
    try:
        # ✅ Validate and resolve the requested file path
        safe_path = validate_path(path)

        # ✅ Check if the file exists
        if not os.path.exists(safe_path):
            raise HTTPException(status_code=404, detail="File not found.")

        # ✅ Read and return the file content
        with open(safe_path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"content": content}

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
