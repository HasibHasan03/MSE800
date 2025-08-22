import sqlite3

DB_NAME = "school.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def execute_query(query, params=()):
    conn = get_connection()
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, params=()):
    conn = get_connection()
    c = conn.cursor()
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    return rows
