import streamlit as st
import requests
import time

st.set_page_config(
    page_title="MediSense Hospital Register",
    page_icon="📝",
    layout="centered"
)

# ---------------------------------------------------
# Header (No Image Required)
# ---------------------------------------------------
st.markdown("""
<div style="
background:linear-gradient(90deg,#1565C0,#42A5F5);
padding:30px;
border-radius:12px;
text-align:center;
color:white;
">
<h1>🏥 MediSense Hospital</h1>
<h3>Create Your Account</h3>
<p>Join our AI-powered healthcare platform.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

st.title("📝 Patient Registration")

st.caption(
    "Create your account to access AI Medical Report Analysis, Prescription AI, Medicine Scanner, Health Analytics, and more."
)

st.divider()

# ---------------------------------------------------
# Registration Form
# ---------------------------------------------------
name = st.text_input("👤 Full Name")

email = st.text_input("📧 Email Address")

password = st.text_input(
    "🔒 Password",
    type="password"
)

confirm_password = st.text_input(
    "🔒 Confirm Password",
    type="password"
)

age = st.number_input(
    "🎂 Age",
    min_value=1,
    max_value=120,
    value=18
)

gender = st.selectbox(
    "⚧ Gender",
    [
        "Male",
        "Female",
        "Other"
    ]
)

st.divider()

# ---------------------------------------------------
# Register Button
# ---------------------------------------------------
if st.button(
    "✅ Create Account",
    use_container_width=True
):

    if not name or not email or not password:

        st.error("Please fill all required fields.")

    elif password != confirm_password:

        st.error("Passwords do not match.")

    else:

        payload = {
            "name": name,
            "email": email,
            "password": password,
            "age": age,
            "gender": gender
        }

        try:

            with st.spinner("Creating your account..."):

                response = requests.post(
                    "http://127.0.0.1:5000/register",
                    json=payload
                )

            if response.status_code in [200, 201]:

                st.success("🎉 Registration Successful!")

                st.info("Redirecting to Login...")

                time.sleep(1)

                st.switch_page("pages/Login.py")

            else:

                try:
                    message = response.json().get(
                        "message",
                        "Registration failed."
                    )
                except:
                    message = "Registration failed."

                st.error(message)

        except Exception:

            st.error(
                "Unable to connect to the backend server.\n\nPlease make sure Flask is running."
            )

st.divider()

# ---------------------------------------------------
# Login Navigation
# ---------------------------------------------------
st.write("Already have an account?")

if st.button(
    "🔐 Login",
    use_container_width=True
):
    st.switch_page("pages/Login.py")

st.divider()

st.info("""
### 🚀 Features Available After Registration

✅ AI Medical Report Analysis

✅ AI Prescription Analyzer

✅ Medicine Scanner

✅ OCR Medical Report Extraction

✅ AI Healthcare Chatbot

✅ Diet Planner

✅ Health Analytics

✅ Medicine Reminders

✅ Personal Health Profile
""")

st.warning("""
⚠️ **Privacy Notice**

Your information is securely stored and used only to provide personalized healthcare features within MediSense Hospital.
""")