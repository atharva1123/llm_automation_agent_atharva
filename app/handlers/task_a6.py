# app/handlers/task_a6.py
import os, json

async def handle(task_description: str) -> str:
    docs_dir = "data/docs"
    index = {}
    
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("#"):
                            title = line.lstrip("#").strip()
                            relative_path = os.path.relpath(file_path, docs_dir)
                            index[relative_path] = title
                            break
    output_path = os.path.join(docs_dir, "index.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
    return "Task A6 completed: Markdown index created at data/docs/index.json."
