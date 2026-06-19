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

    patient = st.text_input("Patient Name")

    email = st.text_input("Email Address")

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

            # Save appointment in database
            book_appointment(
                patient,
                doctor,
                str(date),
                str(time)
            )

            # Send confirmation email
            email_sent = send_confirmation_email(
                email,
                patient,
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

    st.subheader("Admin Dashboard")

    admin_panel()