# app/handlers/task_b5.py
import sqlite3, os

async def handle(task_description: str) -> str:
    # For demonstration, assume a SQLite database exists at data/business.db.
    db_path = os.path.abspath("data/business.db")
    output_path = os.path.abspath("data/business_query_result.txt")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Sample query: count the number of tables in the database.
        query = "SELECT COUNT(*) FROM sqlite_master"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        conn.close()
    except Exception as e:
        raise Exception("Database query failed: " + str(e))
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(result))
    return "Task B5 completed: SQL query executed and result saved to data/business_query_result.txt."
