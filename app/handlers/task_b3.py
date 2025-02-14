# app/handlers/task_b3.py
import requests, os, json

async def handle(task_description: str) -> str:
    # For demonstration, we fetch data from a public API.
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from API")
    
    data = response.json()
    output_path = os.path.abspath("data/api_data.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return "Task B3 completed: Data fetched from API and saved to data/api_data.json."
