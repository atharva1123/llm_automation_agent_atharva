# app/handlers/task_a5.py
import os

async def handle(task_description: str) -> str:
    logs_dir = "data/logs"
    output_path = "data/logs-recent.txt"
    
    try:
        log_files = [os.path.join(logs_dir, f) for f in os.listdir(logs_dir) if f.endswith(".log")]
    except Exception:
        raise Exception("Failed to list files in data/logs")
    
    if not log_files:
        raise Exception("No .log files found in data/logs")
    
    log_files.sort(key=lambda f: os.path.getmtime(f), reverse=True)
    recent_files = log_files[:10]
    
    first_lines = []
    for file in recent_files:
        with open(file, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            first_lines.append(first_line)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(first_lines))
    return "Task A5 completed: First lines from recent log files written to data/logs-recent.txt."
