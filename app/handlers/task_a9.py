# app/handlers/task_a9.py
import numpy as np
from app.utils.llm_utils import call_llm

async def handle(task_description: str) -> str:
    input_path = "data/comments.txt"
    output_path = "data/comments-similar.txt"
    
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            comments = [line.strip() for line in f if line.strip()]
    except Exception:
        raise Exception("Failed to read data/comments.txt")
    
    if len(comments) < 2:
        raise Exception("Not enough comments to compare.")
    
    def get_embedding(text):
        prompt = f"Provide a comma-separated numeric vector for this comment:\n{text}"
        response = call_llm(prompt)
        try:
            vector = [float(x.strip()) for x in response.split(",") if x.strip()]
        except Exception:
            vector = [0.0] * 5  # Fallback vector
        return np.array(vector)
    
    embeddings = [get_embedding(comment) for comment in comments]
    
    best_similarity = -1
    best_pair = (None, None)
    for i in range(len(embeddings)):
        for j in range(i+1, len(embeddings)):
            vec1, vec2 = embeddings[i], embeddings[j]
            norm1 = np.linalg.norm(vec1)
            norm2 = np.linalg.norm(vec2)
            if norm1 == 0 or norm2 == 0:
                continue
            similarity = np.dot(vec1, vec2) / (norm1 * norm2)
            if similarity > best_similarity:
                best_similarity = similarity
                best_pair = (comments[i], comments[j])
    if best_pair[0] is None or best_pair[1] is None:
        raise Exception("Failed to determine similar comments.")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(best_pair[0] + "\n" + best_pair[1])
    return "Task A9 completed: Most similar comments written to data/comments-similar.txt."
