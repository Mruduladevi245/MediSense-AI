import streamlit as st
import os


st.set_page_config(
    page_title="MediSense Hospital",
    page_icon="🏥",
    layout="wide"
)


# =====================================
# Image Path Helper
# =====================================

def load_image(image_name):

    image_path = os.path.join(
        "assets",
        "images",
        image_name
    )

    if os.path.exists(image_path):
        return image_path

    return None



# =====================================
# Hero Section
# =====================================

hero_image = load_image(
    "medisense-ai-hero-banner.jpg.png"
)


if hero_image:

    st.image(
        hero_image,
        use_container_width=True
    )


st.title(
    "🏥 MediSense Hospital"
)


st.subheader(
    "AI Powered Intelligent Healthcare Assistant"
)


st.write(
"""
Welcome to **MediSense Hospital** — an AI-driven healthcare platform that helps
patients understand medical reports, manage prescriptions, monitor health,
and receive personalized healthcare insights.
"""
)


st.divider()



# =====================================
# Login/Register
# =====================================

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "🔐 Login",
        use_container_width=True
    ):

        st.switch_page(
            "pages/Login.py"
        )



with col2:

    if st.button(
        "📝 Register",
        use_container_width=True
    ):

        st.switch_page(
            "pages/Register.py"
        )



st.divider()



# =====================================
# Features
# =====================================

st.header(
    "🚀 MediSense Hospital Features"
)



feature1, feature2, feature3 = st.columns(3)


with feature1:

    st.info(
"""
📄 AI Medical Report Analysis

Upload reports and get AI explanations.
"""
    )


with feature2:

    st.info(
"""
💊 Smart Prescription Reader

Understand medicines and dosage details.
"""
    )


with feature3:

    st.info(
"""
🤖 AI Healthcare Chatbot

Ask health questions anytime.
"""
    )



feature4, feature5, feature6 = st.columns(3)


with feature4:

    st.info(
"""
📊 Health Analytics

Track health trends and insights.
"""
    )


with feature5:

    st.info(
"""
🥗 AI Diet Planner

Personalized nutrition guidance.
"""
    )


with feature6:

    st.info(
"""
🏃 Fitness Planner

Manage exercise goals.
"""
    )



st.divider()



# =====================================
# Hospital Images
# =====================================

st.header(
    "🏥 MediSense Hospital Healthcare"
)


img1, img2 = st.columns(2)



with img1:

    lobby = load_image(
        "medisense-hospital-lobby.jpg.png"
    )

    if lobby:

        st.image(
            lobby,
            caption="Modern MediSense Hospital Facility",
            use_container_width=True
        )

    else:

        st.warning(
            "Hospital lobby image not found"
        )



with img2:

    doctors = load_image(
        "medisense-doctors-team.jpg.png"
    )


    if doctors:

        st.image(
            doctors,
            caption="AI Healthcare Team",
            use_container_width=True
        )

    else:

        st.warning(
            "Doctor team image not found"
        )



st.divider()



# =====================================
# Why MediSense
# =====================================

st.header(
    "🌟 Why Choose MediSense Hospital?"
)


st.success(
"""
✅ AI-powered medical assistance

✅ Secure health record management

✅ Easy medical report understanding

✅ Smart medicine reminders

✅ Personalized health recommendations

✅ Emergency health support
"""
)



st.divider()



# =====================================
# Footer
# =====================================

st.caption(
"🏥 MediSense Hospital | Built with ❤️ using Streamlit + Flask + Gemini AI"
)