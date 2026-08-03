import streamlit as st
import requests
from PIL import Image
import time

st.set_page_config(
    page_title="MediSense Hospital Prescription AI",
    page_icon="💊",
    layout="wide"
)

# -----------------------------
# Authentication
# -----------------------------
if "token" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/Login.py")

token = st.session_state["token"]

headers = {
    "Authorization": f"Bearer {token}"
}

# -----------------------------
# Header (No Image Required)
# -----------------------------
st.markdown("""
<div style='background:linear-gradient(90deg,#1565C0,#42A5F5);
padding:25px;border-radius:12px;color:white;text-align:center'>
<h1>💊 MediSense Hospital AI Prescription Analyzer</h1>
<p>Upload a doctor's prescription and receive AI-powered medicine explanations.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.info("""
AI can analyze:

✅ Medicine Names

✅ Dosage Instructions

✅ Frequency

✅ Duration

✅ Side Effects

✅ Precautions

✅ Food Interactions
""")

st.divider()

# -----------------------------
# Upload Prescription
# -----------------------------
uploaded_file = st.file_uploader(
    "📄 Upload Prescription",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:

    col1, col2 = st.columns([2,1])

    with col1:

        if uploaded_file.type.startswith("image"):

            image = Image.open(uploaded_file)

            st.image(
                image,
                caption="Uploaded Prescription",
                use_container_width=True
            )

        else:

            st.success("📄 PDF Prescription Uploaded Successfully")

    with col2:

        st.subheader("📋 File Details")

        st.write(f"**Name:** {uploaded_file.name}")
        st.write(f"**Type:** {uploaded_file.type}")
        st.write(f"**Size:** {round(uploaded_file.size/1024,2)} KB")

st.divider()

# -----------------------------
# Analyze
# -----------------------------
if uploaded_file:

    if st.button("🤖 Analyze Prescription", use_container_width=True):

        progress = st.progress(0)
        status = st.empty()

        steps = [
            "📄 Reading Prescription...",
            "🔍 Detecting Medicines...",
            "💊 Checking Dosage...",
            "🤖 AI Generating Report..."
        ]

        for i in range(100):

            time.sleep(0.02)

            progress.progress(i + 1)

            if i < 30:
                status.info(steps[0])
            elif i < 60:
                status.info(steps[1])
            elif i < 85:
                status.info(steps[2])
            else:
                status.info(steps[3])

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        try:

            response = requests.post(
                "http://127.0.0.1:5000/analyze-prescription",
                files=files,
                headers=headers
            )

            if response.status_code == 200:

                st.session_state["prescription"] = response.json()

                st.success("✅ Prescription Analysis Completed")

            else:

                st.error(
                    response.json().get(
                        "message",
                        "Analysis failed"
                    )
                )

        except Exception as e:

            st.error(f"Backend Error: {e}")

# -----------------------------
# Results
# -----------------------------
result = st.session_state.get("prescription")

if result:

    st.divider()

    st.subheader("📋 AI Prescription Summary")

    st.info(result.get("summary", "No summary available."))

    st.divider()

    st.subheader("💊 Medicines")

    medicines = result.get("medicines", [])

    if medicines:

        for med in medicines:

            with st.expander(f"💊 {med.get('name','Medicine')}"):

                st.write(f"**Purpose:** {med.get('purpose','-')}")
                st.write(f"**Dosage:** {med.get('dosage','-')}")
                st.write(f"**Frequency:** {med.get('frequency','-')}")
                st.write(f"**Duration:** {med.get('duration','-')}")
                st.write(f"**Instructions:** {med.get('instructions','-')}")
                st.write(f"**Side Effects:** {med.get('side_effects','-')}")
                st.write(f"**Food Advice:** {med.get('food','-')}")

    else:

        st.info("No medicines detected.")

    st.divider()

    st.subheader("⚠ Warnings")

    warnings = result.get("warnings", [])

    if warnings:

        for item in warnings:
            st.warning(item)

    else:

        st.success("No major warnings detected.")

    st.divider()

    st.subheader("💡 AI Health Advice")

    advice = result.get("advice", [])

    if advice:

        for tip in advice:
            st.success(tip)

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⏰ Medicine Reminders"):
            st.switch_page("pages/Medicine_Reminders.py")

    with col2:

        if st.button("💊 Medicine Scanner"):
            st.switch_page("pages/Medicine_Scanner.py")

st.divider()

st.warning("""
⚠️ **Medical Disclaimer**

This AI provides educational information only.
Always follow your doctor's prescription and consult a healthcare professional before making any medical decisions.
""")