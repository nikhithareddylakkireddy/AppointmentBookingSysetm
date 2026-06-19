import sqlite3

def init_db():
    conn = sqlite3.connect("appointment.db")
    c = conn.cursor()

    # Users Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    # Appointments Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS appointments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        appointment_id TEXT,
        patient TEXT,
        age INTEGER,
        gender TEXT,
        phone TEXT,
        email TEXT,
        symptom TEXT,
        department TEXT,
        doctor TEXT,
        date TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()