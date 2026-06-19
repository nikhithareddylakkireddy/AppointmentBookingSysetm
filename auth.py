import sqlite3

def register_user(username,password):
    conn=sqlite3.connect("appointment.db")
    c=conn.cursor()

    c.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username,password)
    )

    conn.commit()
    conn.close()

def login_user(username,password):
    conn=sqlite3.connect("appointment.db")
    c=conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )

    user=c.fetchone()

    conn.close()

    return user