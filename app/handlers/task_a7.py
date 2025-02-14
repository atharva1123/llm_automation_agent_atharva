# app/handlers/task_a7.py
from app.utils.llm_utils import call_llm

async def handle(task_description: str) -> str:
    input_path = "data/email.txt"
    output_path = "data/email-sender.txt"
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            email_content = f.read()
    except Exception:
        raise Exception("Failed to read data/email.txt")
    
    prompt = f"Extract the sender's email address from the following email message. Return only the email address:\n\n{email_content}"
    sender_email = call_llm(prompt)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(sender_email)
    return "Task A7 completed: Email sender extracted and saved to data/email-sender.txt."
