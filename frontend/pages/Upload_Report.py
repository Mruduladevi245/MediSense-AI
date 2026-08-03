import streamlit as st
import requests
from PIL import Image
import time
import os

st.set_page_config(
    page_title="MediSense Hospital Upload Report",
    page_icon="📄",
    layout="wide"
)

# ----------------------------------------------------
# Authentication
# ----------------------------------------------------
if "token" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/Login.py")

token = st.session_state["token"]

headers = {
    "Authorization": f"Bearer {token}"
}

# ----------------------------------------------------
# Image Helper
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

IMAGE_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "images",
    "medisense-medical-laboratory.jpg"
)

if os.path.exists(IMAGE_PATH):

    st.image(
        IMAGE_PATH,
        use_container_width=True
    )

else:

    st.markdown("""
    <div style="
    background:linear-gradient(90deg,#1565C0,#42A5F5);
    padding:30px;
    border-radius:12px;
    text-align:center;
    color:white;
    ">
    <h1>📄 MediSense Hospital</h1>
    <h3>Medical Report Upload</h3>
    <p>Upload your medical reports for AI-powered analysis.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ----------------------------------------------------
# Title
# ----------------------------------------------------
st.title("📄 Medical Report Upload")

st.caption(
    "Upload your medical reports and let MediSense AI analyze your health information."
)

st.info("""
### Supported Documents

- 🩸 Blood Test
- 📄 CBC Report
- 🩻 X-Ray
- 🧠 MRI Scan
- 🩺 CT Scan
- 💊 Prescription
- 🧪 Laboratory Reports
""")

st.divider()

# ----------------------------------------------------
# File Upload
# ----------------------------------------------------
uploaded_file = st.file_uploader(
    "📤 Choose Medical Report",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:

    st.success("✅ Medical report selected.")

    col1, col2 = st.columns([2, 1])

    with col1:

        if uploaded_file.type.startswith("image"):

            image = Image.open(uploaded_file)

            st.image(
                image,
                caption="Report Preview",
                use_container_width=True
            )

        else:

            st.info("📄 PDF selected successfully.")

    with col2:

        st.subheader("📋 File Details")

        st.write(f"**Name:** {uploaded_file.name}")
        st.write(f"**Type:** {uploaded_file.type}")
        st.write(f"**Size:** {round(uploaded_file.size/1024,2)} KB")

st.divider()

# ----------------------------------------------------
# Upload Button
# ----------------------------------------------------
if uploaded_file:

    if st.button(
        "🚀 Upload & Start AI Analysis",
        use_container_width=True
    ):

        progress = st.progress(0)
        status = st.empty()

        steps = [
            "📤 Uploading Report...",
            "🔍 Running OCR...",
            "🧠 Preparing AI Analysis...",
            "✅ Finalizing..."
        ]

        for i in range(100):

            time.sleep(0.01)

            progress.progress(i + 1)

            if i < 25:
                status.info(steps[0])
            elif i < 50:
                status.info(steps[1])
            elif i < 75:
                status.info(steps[2])
            else:
                status.success(steps[3])

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        try:

            response = requests.post(
                "http://127.0.0.1:5000/upload-report",
                headers=headers,
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                st.session_state["report_id"] = result.get("report_id")
                st.session_state["ocr_text"] = result.get("ocr_text", "")

                st.success("🎉 Report uploaded successfully!")

                time.sleep(1)

                st.switch_page("pages/OCR_Result.py")

            else:

                try:
                    message = response.json().get(
                        "message",
                        "Upload failed."
                    )
                except:
                    message = "Upload failed."

                st.error(message)

        except Exception:

            st.error(
                "Unable to connect to the backend server.\n\nPlease make sure Flask is running."
            )

st.divider()

st.info("""
### 📌 Supported Formats

- PDF
- JPG
- JPEG
- PNG

**Maximum recommended file size:** 10 MB
""")

st.warning("""
⚠️ **Medical Disclaimer**

MediSense AI provides educational assistance for understanding medical reports.
It is not a substitute for professional medical diagnosis or treatment.
""")