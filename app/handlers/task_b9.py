# app/handlers/task_b9.py
import os, markdown

async def handle(task_description: str) -> str:
    # For demonstration, convert data/sample_markdown.md to HTML.
    input_path = os.path.abspath("data/sample_markdown.md")
    output_path = os.path.abspath("data/sample_markdown.html")
    
    if not os.path.exists(input_path):
        raise Exception("Markdown file not found at data/sample_markdown.md")
    
    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    
    html = markdown.markdown(md_text)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    return "Task B9 completed: Markdown converted to HTML and saved to data/sample_markdown.html."
