import streamlit as st

st.set_page_config(
    page_title="About MediSense Hospital",
    page_icon="🏥",
    layout="wide"
)

# Page Title
st.title("🏥 About MediSense Hospital")

# Hospital Image
st.image(
    "assets/images/medisense-hospital-staff.jpg.png",
    caption="MediSense Hospital",
    use_container_width=True
)

st.subheader("Welcome to MediSense Hospital")

st.write("""
**MediSense Hospital** is an AI-powered healthcare platform designed to make healthcare
smarter, faster, and more accessible.

Our intelligent system helps patients and healthcare professionals with:
""")

# Features
col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
🩺 **Medical Report Analysis**

Upload medical reports and get AI-powered insights and explanations.
"""
    )

with col2:
    st.info(
        """
🤖 **AI Health Assistant**

Get instant health guidance and answers through our intelligent chatbot.
"""
    )

with col3:
    st.info(
        """
💊 **Smart Prescription Management**

Track medicines, reminders, and healthcare schedules easily.
"""
    )


st.divider()


# Vision Section
st.subheader("🌟 Our Vision")

st.write("""
At MediSense Hospital, our vision is to combine Artificial Intelligence and healthcare
technology to provide personalized, reliable, and patient-friendly healthcare solutions.

We aim to support early health awareness, better medical understanding, and smarter
health management.
""")


# Mission Section
st.subheader("🎯 Our Mission")

st.write("""
✅ Make medical information easier to understand

✅ Provide AI-based healthcare assistance

✅ Help users maintain better health records

✅ Improve healthcare accessibility through technology
""")


st.divider()


# Healthcare Team
st.subheader("👨‍⚕️ MediSense Hospital Healthcare Team")

st.image(
    "assets/images/medisense-hospital-staff.jpg.png",
    caption="MediSense Hospital Healthcare Team",
    use_container_width=True
)


st.divider()


# Hospital Facility Image
st.subheader("🏥 MediSense Hospital Infrastructure")

st.image(
    "assets/images/medisense-hospital-exterior.jpg.png",
    caption="Modern MediSense Hospital Facility",
    use_container_width=True
)


st.success(
    "🏥 MediSense Hospital — AI Powered Healthcare for a Healthier Future"
)