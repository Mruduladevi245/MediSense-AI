import streamlit as st
import requests
from pathlib import Path


st.set_page_config(
    page_title="MediSense Hospital AI Chatbot",
    page_icon="🤖",
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
# Header Image
# -----------------------------

IMAGE_PATH = (
    Path(__file__).parent.parent
    / "assets"
    / "images"
    / "medisense-ai-hero-banner.jpg.png"
)


if IMAGE_PATH.exists():

    st.image(
        str(IMAGE_PATH),
        use_container_width=True
    )

else:

    st.warning(
        "MediSense AI Hero image not found."
    )



# -----------------------------
# Title
# -----------------------------

st.title(
    "🤖 MediSense Hospital AI Chatbot"
)


st.caption(
    "Your AI healthcare assistant for reports, medicines, symptoms, diet, and general health information."
)


st.divider()



# -----------------------------
# Chat Session
# -----------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []



# -----------------------------
# Language
# -----------------------------

language = st.selectbox(
    "🌐 Select Language",
    [
        "English",
        "Hindi",
        "Telugu",
        "Kannada",
        "Tamil"
    ]
)



# -----------------------------
# Quick Questions
# -----------------------------

st.subheader(
    "💡 Quick Health Questions"
)


c1, c2, c3 = st.columns(3)


with c1:

    if st.button(
        "📄 Explain My Report"
    ):

        st.session_state["quick_question"] = (
            "Explain my medical report in simple words."
        )



with c2:

    if st.button(
        "💊 Explain Medicines"
    ):

        st.session_state["quick_question"] = (
            "Explain my prescription medicines."
        )



with c3:

    if st.button(
        "🥗 Diet Recommendation"
    ):

        st.session_state["quick_question"] = (
            "Suggest a healthy diet plan."
        )



st.divider()



# -----------------------------
# Display Chat History
# -----------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(
            msg["content"]
        )



# -----------------------------
# Chat Input
# -----------------------------

default_prompt = st.session_state.pop(
    "quick_question",
    ""
)


prompt = st.chat_input(
    "Ask MediSense Hospital AI..."
)


if default_prompt:

    prompt = default_prompt



# -----------------------------
# Send Message
# -----------------------------

if prompt:


    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    with st.chat_message("user"):

        st.markdown(prompt)



    with st.chat_message("assistant"):


        with st.spinner(
            "MediSense AI is analyzing..."
        ):


            payload = {

                "message": prompt,

                "language": language,

                "report_id": st.session_state.get(
                    "report_id"
                )

            }


            try:

                response = requests.post(

                    "http://127.0.0.1:5000/chat",

                    json=payload,

                    headers=headers

                )


                if response.status_code == 200:


                    answer = response.json().get(
                        "response",
                        "No response received."
                    )


                else:

                    answer = (
                        "Unable to process your request."
                    )



            except Exception:


                answer = (
                    "Backend server is not available."
                )



            st.markdown(answer)



    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )



st.divider()



# -----------------------------
# Controls
# -----------------------------

c1, c2 = st.columns(2)



with c1:


    if st.button(
        "🗑 Clear Chat"
    ):

        st.session_state.messages = []

        st.rerun()



with c2:


    if st.button(
        "🎤 Voice Assistant"
    ):

        st.info(
            "🎤 Voice Assistant feature will be added soon."
        )



st.divider()



# -----------------------------
# Medical Disclaimer
# -----------------------------

st.warning(
"""
⚠️ Medical Disclaimer

MediSense Hospital AI provides educational and informational assistance only.

It does not replace professional medical diagnosis, treatment, or consultation.

Always consult a qualified healthcare professional for medical decisions.
"""
)