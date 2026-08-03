import streamlit as st
import plotly.graph_objects as go
from datetime import datetime


st.set_page_config(
    page_title="MediSense Hospital Dashboard",
    page_icon="🏥",
    layout="wide"
)


# ---------------------------
# Authentication Check
# ---------------------------

if "token" not in st.session_state:

    st.warning("Please login first.")

    st.switch_page(
        "pages/Login.py"
    )


# ---------------------------
# Hospital Banner
# ---------------------------

st.image(
    "assets/images/medisense-doctors-team.jpg.png",
    use_container_width=True
)

# ---------------------------
# Header
# ---------------------------

st.title(
    "🏥 MediSense Hospital Dashboard"
)


st.caption(
    f"Welcome back • {datetime.now().strftime('%d %B %Y')}"
)


st.divider()



# ---------------------------
# Health Cards
# ---------------------------

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "❤️ Health Score",
        "86%",
        "+4%"
    )


with c2:

    st.metric(
        "📄 Reports Uploaded",
        "8"
    )


with c3:

    st.metric(
        "💊 Medicines",
        "5"
    )


with c4:

    st.metric(
        "📅 Appointments",
        "2"
    )



st.divider()



# ---------------------------
# Health Analytics
# ---------------------------

col1, col2 = st.columns(
    [2,1]
)



with col1:

    st.subheader(
        "📈 Health Progress"
    )


    fig = go.Figure()


    fig.add_trace(

        go.Scatter(

            x=[
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun"
            ],

            y=[
                70,
                74,
                75,
                80,
                82,
                86
            ],

            mode="lines+markers",

            name="Health Score"

        )

    )


    fig.update_layout(
        height=350
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



with col2:

    st.subheader(
        "🤖 AI Health Summary"
    )


    st.success(
        "Blood pressure is stable."
    )


    st.info(
        "Maintain proper hydration."
    )


    st.warning(
        "Vitamin D level needs attention."
    )


    st.success(
        "Good sleep pattern detected."
    )



st.divider()



# ---------------------------
# Quick Actions
# ---------------------------

st.subheader(
    "⚡ Quick Actions"
)


a,b,c,d = st.columns(4)



with a:

    if st.button(
        "📄 Upload Report"
    ):

        st.switch_page(
            "pages/Upload_Report.py"
        )



with b:

    if st.button(
        "🧠 AI Report Analysis"
    ):

        st.switch_page(
            "pages/AI_Report_Analysis.py"
        )



with c:

    if st.button(
        "💊 Prescription AI"
    ):

        st.switch_page(
            "pages/Prescription_AI.py"
        )



with d:

    if st.button(
        "🤖 AI Chatbot"
    ):

        st.switch_page(
            "pages/AI_Chatbot.py"
        )



st.divider()



# ---------------------------
# Recent Reports
# ---------------------------

st.subheader(
    "📄 Recent Medical Reports"
)


st.dataframe(

    [

        {
            "Report":"Blood Test",
            "Date":"12/07/2026",
            "Status":"Analyzed"
        },

        {
            "Report":"CBC",
            "Date":"15/07/2026",
            "Status":"Analyzed"
        },

        {
            "Report":"Prescription",
            "Date":"18/07/2026",
            "Status":"Pending"
        }

    ],

    use_container_width=True

)



st.divider()



# ---------------------------
# Sidebar
# ---------------------------

with st.sidebar:


    st.image(
        "assets/images/medisense-hospital-staff.jpg.png"
    )


    st.title(
        "🏥 MediSense Hospital"
    )


    st.page_link(
        "pages/Dashboard.py",
        label="Dashboard"
    )


    st.page_link(
        "pages/Profile.py",
        label="Profile"
    )


    st.page_link(
        "pages/Upload_Report.py",
        label="Upload Report"
    )


    st.page_link(
        "pages/AI_Report_Analysis.py",
        label="AI Report Analysis"
    )


    st.page_link(
        "pages/Prescription.py",
        label="Prescription AI"
    )


    st.page_link(
        "pages/AI_Chatbot.py",
        label="AI Chatbot"
    )


    st.page_link(
        "pages/Health_Analytics.py",
        label="Analytics"
    )


    st.page_link(
        "pages/Diet_Planner.py",
        label="Diet Planner"
    )


    st.page_link(
        "pages/Medicine_Reminders.py",
        label="Medicine Reminder"
    )


    st.page_link(
        "pages/About.py",
        label="About MediSense"
    )


    st.divider()


    if st.button(
        "🚪 Logout"
    ):

        st.session_state.clear()

        st.switch_page(
            "pages/Login.py"
        )