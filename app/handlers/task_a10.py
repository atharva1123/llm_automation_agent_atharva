# app/handlers/task_a10.py
import sqlite3

async def handle(task_description: str) -> str:
    db_path = "data/ticket-sales.db"
    output_path = "data/ticket-sales-gold.txt"
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = "SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        result = result if result is not None else 0
        conn.close()
    except Exception as e:
        raise Exception("Database query failed: " + str(e))
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(result))
    return "Task A10 completed: Total Gold ticket sales written to data/ticket-sales-gold.txt."
