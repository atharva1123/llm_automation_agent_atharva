# app/task_parser.py
import re
from typing import Callable, Awaitable, Dict
from app.handlers import (
    task_a1, task_a2, task_a3, task_a4, task_a5, task_a6, task_a7, task_a8, task_a9, task_a10,
    task_b3, task_b4, task_b5, task_b6, task_b7, task_b8, task_b9, task_b10
)

# Mapping of keywords to their corresponding async handler functions.
TASK_MAP: Dict[str, Callable[[str], Awaitable[str]]] = {
    # Phase A mappings
    "uv": task_a1.handle,
    "datagen": task_a1.handle,
    "prettier": task_a2.handle,
    "format": task_a2.handle,
    "wednesday": task_a3.handle,
    "dates": task_a3.handle,
    "contacts": task_a4.handle,
    "sort": task_a4.handle,
    "log": task_a5.handle,
    "markdown": task_a6.handle,
    "docs": task_a6.handle,
    "email": task_a7.handle,
    "credit card": task_a8.handle,
    "comments": task_a9.handle,
    "ticket-sales": task_a10.handle,
    "gold": task_a10.handle,
    # Phase B mappings
    "api fetch": task_b3.handle,
    "git clone": task_b4.handle,
    "sql query": task_b5.handle,
    "scrape": task_b6.handle,
    "resize image": task_b7.handle,
    "transcribe": task_b8.handle,
    "markdown to html": task_b9.handle,
    "filter csv": task_b10.handle,
}

async def parse_and_execute_task(task_description: str) -> str:
    """
    Parses a plain-English task description and executes the corresponding task.

    The function searches for known keywords in the task description and delegates execution
    to the corresponding handler. If no keyword is found, it then checks for an explicit
    task number reference (e.g., "B3", "B4", etc.). If neither method identifies a valid
    task, a ValueError is raised.

    Args:
        task_description (str): A plain-English description of the task.

    Returns:
        str: The result from the executed task handler.

    Raises:
        ValueError: If the task is not recognized.
    """
    task_description_lower = task_description.lower()
    
    # Check for keyword-based tasks.
    for keyword, handler in TASK_MAP.items():
        if keyword in task_description_lower:
            return await handler(task_description)
    
    # Fallback: Look for explicit task number references (e.g., "B3")
    match = re.search(r"B(\d+)", task_description, re.IGNORECASE)
    if match:
        task_num = match.group(1)
        fallback_map: Dict[str, Callable[[str], Awaitable[str]]] = {
            "3": task_b3.handle,
            "4": task_b4.handle,
            "5": task_b5.handle,
            "6": task_b6.handle,
            "7": task_b7.handle,
            "8": task_b8.handle,
            "9": task_b9.handle,
            "10": task_b10.handle,
        }
        if task_num in fallback_map:
            return await fallback_map[task_num](task_description)
    
    raise ValueError("Task not recognized.")
