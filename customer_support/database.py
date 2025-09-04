import sqlite3
from datetime import datetime

DB_FILE = "chatbot.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Users table
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_active TIMESTAMP
    )
    """)

    # Chat history table
    c.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        sender TEXT CHECK(sender IN ('user','bot')),
        message_text TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
    """)

    conn.commit()
    conn.close()


def save_message(user_id, sender, message_text):
    conn = sqlite3.connect(DB_FILE)   # ✅ fixed DB_FILE
    c = conn.cursor()
    c.execute("""
        INSERT INTO chat_history (user_id, sender, message_text, timestamp)
        VALUES (?, ?, ?, ?)
    """, (user_id, sender, message_text, datetime.now()))
    conn.commit()
    conn.close()


def load_recent_history(user_id, limit=5):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        SELECT sender, message_text
        FROM chat_history
        WHERE user_id = ?
        ORDER BY timestamp DESC
        LIMIT ?
    """, (user_id, limit))
    rows = c.fetchall()
    conn.close()

    role_map = {"user": "user", "bot": "assistant"}

    # Convert DB rows into LLM-compatible messages
    history = [{"role": role_map.get(row[0], "user"), "content": row[1]} for row in rows[::-1]]
    return history
