# app/handlers/task_b6.py
import requests, os
from bs4 import BeautifulSoup

async def handle(task_description: str) -> str:
    # For demonstration, scrape the title of https://example.com.
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch webpage")
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    output_path = os.path.abspath("data/scraped_data.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(title)
    return "Task B6 completed: Web page scraped and title saved to data/scraped_data.txt."
