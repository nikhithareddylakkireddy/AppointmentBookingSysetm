import streamlit as st
import pandas as pd
from appointment import get_appointments

def admin_panel():

    st.subheader("📊 Admin Dashboard")

    appointments = get_appointments()

    st.metric("Total Appointments", len(appointments))

    st.markdown("---")

    st.subheader("📅 All Appointments")

    if appointments:

        df = pd.DataFrame(
            appointments,
            columns=[
                "ID",
                "Appointment ID",
                "Patient",
                "Age",
                "Gender",
                "Phone",
                "Email",
                "Symptom",
                "Department",
                "Doctor",
                "Date",
                "Time"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        csv = df.to_csv(index=False)

        st.download_button(
            "📥 Download Appointments CSV",
            csv,
            "appointments.csv",
            "text/csv"
        )

    else:
        st.info("No appointments found.")