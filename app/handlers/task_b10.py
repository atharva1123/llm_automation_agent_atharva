# app/handlers/task_b10.py
import os, csv, json

async def handle(task_description: str) -> str:
    # For demonstration, read data/filter.csv, filter rows where "active" column equals "true",
    # and save the result as JSON to data/filter_result.json.
    input_path = os.path.abspath("data/filter.csv")
    output_path = os.path.abspath("data/filter_result.json")
    
    if not os.path.exists(input_path):
        raise Exception("CSV file not found at data/filter.csv")
    
    filtered_rows = []
    with open(input_path, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get("active", "").lower() == "true":
                filtered_rows.append(row)
    
    with open(output_path, "w", encoding="utf-8") as jsonfile:
        json.dump(filtered_rows, jsonfile, indent=2)
    
    return "Task B10 completed: Filtered CSV data saved to data/filter_result.json."
