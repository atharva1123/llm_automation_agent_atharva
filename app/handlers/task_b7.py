# app/handlers/task_b7.py
import os
from PIL import Image

async def handle(task_description: str) -> str:
    # For demonstration, resize an image found at data/sample_image.jpg.
    input_path = os.path.abspath("data/bird.jpg")
    output_path = os.path.abspath("data/bird_resized.jpg")
    
    if not os.path.exists(input_path):
        raise Exception("Input image not found at data/bird.jpg")
    
    img = Image.open(input_path)
    # Resize the image to half its width and height.
    new_size = (img.width // 2, img.height // 2)
    resized_img = img.resize(new_size)
    resized_img.save(output_path)
    return "Task B7 completed: Image resized and saved to data/bird_resized.jpg."
