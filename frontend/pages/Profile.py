import streamlit as st
import requests

st.set_page_config(
    page_title="MediSense Hospital Profile",
    page_icon="👤",
    layout="wide"
)

# -----------------------------------
# Authentication
# -----------------------------------
if "token" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/Login.py")

token = st.session_state["token"]

headers = {
    "Authorization": f"Bearer {token}"
}

# -----------------------------------
# Header (No Image Required)
# -----------------------------------
st.markdown("""
<div style="
background:linear-gradient(90deg,#1565C0,#42A5F5);
padding:25px;
border-radius:12px;
color:white;
text-align:center;
">
<h1>👤 MediSense Hospital Patient Profile</h1>
<p>Manage your personal information, health records and AI healthcare settings.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

st.caption("Manage your personal details and health information.")

st.divider()

# -----------------------------------
# Fetch Profile
# -----------------------------------
try:

    response = requests.get(
        "http://127.0.0.1:5000/profile",
        headers=headers
    )

    if response.status_code == 200:
        user = response.json()
    else:
        user = {}
        st.error("Unable to fetch profile.")

except Exception:
    user = {}
    st.error("Backend server is not running.")

# -----------------------------------
# Personal Information
# -----------------------------------
st.subheader("👤 Personal Information")

col1, col2 = st.columns([1, 2])

with col1:

    uploaded_image = st.file_uploader(
        "Upload Profile Photo",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image:
        st.image(
            uploaded_image,
            width=180,
            caption="Profile Photo"
        )
    else:
        st.markdown(
            """
            <div style="
            width:180px;
            height:180px;
            border-radius:50%;
            background:#E3F2FD;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:80px;
            margin:auto;
            ">
            👤
            </div>
            """,
            unsafe_allow_html=True
        )

with col2:

    name = st.text_input(
        "Full Name",
        value=user.get("name", "")
    )

    email = st.text_input(
        "Email",
        value=user.get("email", ""),
        disabled=True
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=int(user.get("age", 18))
    )

    gender_options = ["Male", "Female", "Other"]

    saved_gender = user.get("gender", "Male")

    gender = st.selectbox(
        "Gender",
        gender_options,
        index=gender_options.index(saved_gender) if saved_gender in gender_options else 0
    )

st.divider()

# -----------------------------------
# Health Information
# -----------------------------------
st.subheader("🏥 Health Information")

c1, c2 = st.columns(2)

with c1:

    height = st.number_input(
        "Height (cm)",
        value=float(user.get("height", 170))
    )

    weight = st.number_input(
        "Weight (kg)",
        value=float(user.get("weight", 65))
    )

with c2:

    blood_groups = [
        "A+", "A-", "B+", "B-",
        "AB+", "AB-", "O+", "O-"
    ]

    saved_group = user.get("blood_group", "O+")

    blood = st.selectbox(
        "Blood Group",
        blood_groups,
        index=blood_groups.index(saved_group) if saved_group in blood_groups else 6
    )

    allergies = st.text_area(
        "Allergies",
        value=user.get("allergies", "")
    )

st.divider()

# -----------------------------------
# BMI Calculator
# -----------------------------------
st.subheader("⚖ Body Mass Index (BMI)")

try:
    bmi = weight / ((height / 100) ** 2)
except ZeroDivisionError:
    bmi = 0

st.metric("BMI", f"{bmi:.2f}")

if bmi == 0:
    st.info("Enter valid height and weight.")
elif bmi < 18.5:
    st.info("Underweight - Consider balanced nutrition.")
elif bmi < 25:
    st.success("Healthy BMI Range.")
elif bmi < 30:
    st.warning("Overweight - Regular exercise is recommended.")
else:
    st.error("High BMI - Please consult a healthcare professional.")

st.divider()

# -----------------------------------
# Save Profile
# -----------------------------------
if st.button(
    "💾 Save Health Profile",
    use_container_width=True
):

    profile = {
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "blood_group": blood,
        "allergies": allergies
    }

    try:

        response = requests.put(
            "http://127.0.0.1:5000/profile",
            json=profile,
            headers=headers
        )

        if response.status_code == 200:
            st.success("✅ Profile updated successfully!")
        else:
            st.error(
                response.json().get(
                    "message",
                    "Profile update failed."
                )
            )

    except Exception:
        st.error("Backend server is not running.")

st.divider()

st.warning("""
⚠️ **Privacy & Medical Notice**

Your health information is used only to personalize MediSense AI healthcare services.
Always consult a qualified healthcare professional for medical decisions.
""")