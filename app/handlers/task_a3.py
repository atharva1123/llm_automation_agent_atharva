# app/handlers/task_a3.py
from datetime import datetime

async def handle(task_description: str) -> str:
    input_path = "data/dates.txt"
    output_path = "data/dates-wednesdays.txt"
    
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        raise Exception("Failed to read data/dates.txt")
    
    wednesday_count = 0
    for line in lines:
        line = line.strip()
        try:
            date_obj = datetime.fromisoformat(line)
            if date_obj.weekday() == 2:  # Wednesday (Monday=0, Wednesday=2)
                wednesday_count += 1
        except Exception:
            continue
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(wednesday_count))
    return "Task A3 completed: Counted Wednesdays and updated data/dates-wednesdays.txt."
