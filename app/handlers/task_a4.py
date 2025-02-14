# app/handlers/task_a4.py
import json, os

async def handle(task_description: str) -> str:
    input_path = "data/contacts.json"
    output_path = "data/contacts-sorted.json"
    
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            contacts = json.load(f)
    except Exception:
        raise Exception("Failed to read data/contacts.json")
    
    sorted_contacts = sorted(contacts, key=lambda x: (x.get("last_name", ""), x.get("first_name", "")))
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(sorted_contacts, f, indent=2)
    return "Task A4 completed: Contacts sorted and saved to data/contacts-sorted.json."
