# app/handlers/task_a8.py
from app.utils.llm_utils import call_llm
from PIL import Image
import pytesseract, os

async def handle(task_description: str) -> str:
    input_path = "data/credit-card.png"
    output_path = "data/credit-card.txt"
    
    try:
        img = Image.open(input_path)
    except Exception:
        raise Exception("Failed to open data/credit-card.png")
    
    try:
        ocr_text = pytesseract.image_to_string(img)
    except Exception:
        raise Exception("OCR extraction failed.")
    
    prompt = f"Extract the credit card number from the following text, remove spaces, and return only the number:\n\n{ocr_text}"
    card_number = call_llm(prompt)
    card_number = card_number.replace(" ", "")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(card_number)
    return "Task A8 completed: Credit card number extracted and saved to data/credit-card.txt."
