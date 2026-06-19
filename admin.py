import streamlit as st
import pandas as pd
from appointment import get_appointments

def admin_panel():
    st.subheader("📊 Admin Dashboard")

    appointments = get_appointments()

    # Total appointments card
    st.metric("Total Appointments", len(appointments))

    st.markdown("---")

    st.subheader("📅 All Appointments")

    if appointments:

        # Create DataFrame
        df = pd.DataFrame(
            appointments,
            columns=[
                "ID",
                "Patient Name",
                "Doctor",
                "Date",
                "Time"
            ]
        )

        # Show table
        st.dataframe(df, use_container_width=True)

    else:
        st.info("No appointments found.")