import sqlite3

def book_appointment(
    appointment_id,
    patient,
    age,
    gender,
    phone,
    email,
    symptom,
    department,
    doctor,
    date,
    time
):
    conn = sqlite3.connect("appointment.db")
    c = conn.cursor()

    c.execute(
        """
        INSERT INTO appointments(
            appointment_id,
            patient,
            age,
            gender,
            phone,
            email,
            symptom,
            department,
            doctor,
            date,
            time
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            appointment_id,
            patient,
            age,
            gender,
            phone,
            email,
            symptom,
            department,
            doctor,
            date,
            time
        )
    )

    conn.commit()
    conn.close()


def get_appointments():
    conn = sqlite3.connect("appointment.db")
    c = conn.cursor()

    c.execute("SELECT * FROM appointments")

    data = c.fetchall()

    conn.close()

    return data