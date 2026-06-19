import streamlit as st
from database import init_db
from auth import register_user, login_user
from appointment import book_appointment
from admin import admin_panel
from email_service import send_confirmation_email

# Initialize Database
init_db()

st.set_page_config(
    page_title="Doctor Appointment Booking System",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Doctor Appointment Booking System")

# Sidebar Menu
menu = ["Register", "Login", "Book Appointment", "Admin"]

choice = st.sidebar.selectbox("Menu", menu)

# ---------------- REGISTER ----------------

if choice == "Register":

    st.subheader("Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        try:
            register_user(username, password)
            st.success("Registration Successful")

        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- LOGIN ----------------

elif choice == "Login":

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = login_user(username, password)

        if user:
            st.success("Login Successful")
            st.balloons()

        else:
            st.error("Invalid Credentials")

# ---------------- BOOK APPOINTMENT ----------------

elif choice == "Book Appointment":

    st.subheader("Book Appointment")

    appointment_id = st.text_input("Appointment ID")

    patient = st.text_input("Patient Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        step=1
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    phone = st.text_input("Phone Number")

    email = st.text_input("Email Address")

    symptom = st.text_input("Symptoms")

    department = st.selectbox(
        "Department",
        [
            "General Medicine",
            "Cardiology",
            "Dentist",
            "Neurology",
            "Orthopedics"
        ]
    )

    doctor = st.selectbox(
        "Select Doctor",
        [
            "Dr. Smith",
            "Dr. John",
            "Dr. Priya",
            "Dr. Kumar",
            "Dr. Reddy"
        ]
    )

    date = st.date_input("Appointment Date")

    time = st.time_input("Appointment Time")

    if st.button("Book Appointment"):

        try:

            # Save Appointment
            book_appointment(
                appointment_id,
                patient,
                age,
                gender,
                phone,
                email,
                symptom,
                department,
                doctor,
                str(date),
                str(time)
            )

            # Send Email
            email_sent = send_confirmation_email(
                email,
                patient,
                appointment_id,
                symptom,
                department,
                doctor,
                str(date),
                str(time)
            )

            st.success("Appointment Booked Successfully ✅")

            if email_sent:
                st.success("Confirmation Email Sent 📧")
            else:
                st.warning(
                    "Appointment saved but email could not be sent."
                )

            st.balloons()

        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- ADMIN PANEL ----------------

elif choice == "Admin":

    admin_panel()