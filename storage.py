import sqlite3
import os

# Trouve le chemin du dossier actuel pour créer la BDD au bon endroit
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS runs 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
                     success_rate REAL, 
                     avg_latency REAL, 
                     details TEXT)''')
        conn.commit()

def save_run(success_rate, avg_latency, details):
    with get_db_connection() as conn:
        conn.execute("INSERT INTO runs (success_rate, avg_latency, details) VALUES (?, ?, ?)",
                     (success_rate, avg_latency, details))
        conn.commit()

def get_runs():
    with get_db_connection() as conn:
        return conn.execute("SELECT * FROM runs ORDER BY id DESC LIMIT 10").fetchall()
