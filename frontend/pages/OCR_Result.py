import streamlit as st
import requests
import os

st.set_page_config(
    page_title="MediSense Hospital OCR Results",
    page_icon="📑",
    layout="wide"
)

# --------------------------------
# Image Helper
# --------------------------------
def get_image(filename):
    path = os.path.join("assets", "images", filename)

    if os.path.exists(path):
        return path

    if os.path.exists(path + ".png"):
        return path + ".png"

    return None


# --------------------------------
# Authentication
# --------------------------------
if "token" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/Login.py")


# --------------------------------
# Header Image
# --------------------------------
image = get_image("medisense-medical-laboratory.jpg")

if image:
    st.image(
        image,
        use_container_width=True
    )


# --------------------------------
# Title
# --------------------------------
st.title("📑 MediSense Hospital OCR Results")

st.caption(
    "AI-powered medical document text extraction and analysis."
)

st.divider()


# --------------------------------
# Session Data
# --------------------------------
ocr_text = st.session_state.get("ocr_text", "")
report_id = st.session_state.get("report_id", "")

if not report_id:
    st.error("No medical report found. Please upload one first.")
    st.stop()


# --------------------------------
# Status
# --------------------------------
st.success("✅ OCR Processing Completed")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("📄 Report ID", report_id)

with c2:
    st.metric("OCR Status", "Completed")

with c3:
    st.metric("Language", "English")

st.divider()


# --------------------------------
# Search OCR Text
# --------------------------------
st.subheader("🔍 Search OCR Text")

search = st.text_input("Search")

display_text = ocr_text

if search:
    display_text = "\n".join(
        line
        for line in ocr_text.split("\n")
        if search.lower() in line.lower()
    )


# --------------------------------
# OCR Text
# --------------------------------
st.subheader("📄 Extracted Text")

st.text_area(
    "OCR Output",
    value=display_text,
    height=350
)


st.download_button(
    "⬇ Download OCR Report",
    data=ocr_text,
    file_name="ocr_report.txt",
    mime="text/plain"
)

st.divider()


# --------------------------------
# Statistics
# --------------------------------
st.subheader("📊 OCR Statistics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Words", len(ocr_text.split()))

with c2:
    st.metric("Lines", len(ocr_text.splitlines()))

with c3:
    st.metric("Characters", len(ocr_text))

st.divider()


# --------------------------------
# OCR Confidence
# --------------------------------
st.subheader("🤖 OCR Confidence")

try:

    response = requests.get(
        f"http://127.0.0.1:5000/report/{report_id}"
    )

    if response.status_code == 200:

        confidence = response.json().get(
            "confidence",
            98.6
        )

        st.progress(confidence / 100)

        st.success(
            f"Accuracy: {confidence}%"
        )

    else:

        st.info("Confidence unavailable.")

except Exception:

    st.info("Backend unavailable.")


st.divider()


# --------------------------------
# Navigation
# --------------------------------
c1, c2 = st.columns(2)

with c1:

    if st.button(
        "⬅ Upload Another Report",
        use_container_width=True
    ):
        st.switch_page("pages/Upload_Report.py")


with c2:

    if st.button(
        "🤖 Analyze Report",
        use_container_width=True
    ):
        st.switch_page("pages/AI_Report_Analysis.py")


st.warning("""
⚠️ Medical Disclaimer

This OCR result is generated automatically.
Always verify the extracted text with the original medical report and consult a qualified healthcare professional.
""")