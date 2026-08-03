import streamlit as st
import requests
from PIL import Image
import time
import os


st.set_page_config(
    page_title="MediSense Hospital Medicine Scanner",
    page_icon="💊",
    layout="wide"
)


# ------------------------------------
# Image Helper
# ------------------------------------

def get_image(filename):

    path = os.path.join(
        "assets",
        "images",
        filename
    )

    if os.path.exists(path):
        return path

    if os.path.exists(path + ".png"):
        return path + ".png"

    return None



# ------------------------------------
# Authentication
# ------------------------------------

if "token" not in st.session_state:

    st.warning("Please login first.")

    st.switch_page(
        "pages/Login.py"
    )


token = st.session_state["token"]


headers = {
    "Authorization": f"Bearer {token}"
}



# ------------------------------------
# Header Image
# ------------------------------------

medicine_banner = get_image(
    "medisense-medicine-management.jpg"
)


if medicine_banner:

    st.image(
        medicine_banner,
        use_container_width=True
    )



# ------------------------------------
# Title
# ------------------------------------

st.title(
    "💊 MediSense Hospital AI Medicine Scanner"
)


st.caption(
    "Upload medicine images and get AI-powered medicine information."
)



st.write(
"""
The AI scanner identifies:

✅ Medicine Name  
✅ Generic Name  
✅ Uses  
✅ Dosage Information  
✅ Side Effects  
✅ Precautions  
✅ Storage Instructions  
✅ Food Interactions
"""
)


st.divider()



# ------------------------------------
# Upload Medicine Image
# ------------------------------------

uploaded_file = st.file_uploader(

    "📷 Upload Medicine Strip / Bottle / Box Image",

    type=[
        "jpg",
        "jpeg",
        "png"
    ]

)



if uploaded_file:


    image = Image.open(
        uploaded_file
    )


    col1, col2 = st.columns(
        [2,1]
    )


    with col1:

        st.image(
            image,
            caption="Uploaded Medicine Image",
            use_container_width=True
        )


    with col2:

        st.subheader(
            "📄 Image Details"
        )

        st.write(
            f"**Name:** {uploaded_file.name}"
        )

        st.write(
            f"**Size:** {round(uploaded_file.size/1024,2)} KB"
        )

        st.write(
            f"**Type:** {uploaded_file.type}"
        )



st.divider()



# ------------------------------------
# Scan Medicine
# ------------------------------------

if uploaded_file:


    if st.button(
        "🔍 Scan Medicine with AI",
        use_container_width=True
    ):


        progress = st.progress(0)

        status = st.empty()



        steps = [

            "🔎 Detecting Medicine Image...",

            "📝 Running OCR Extraction...",

            "🧠 AI Analyzing Medicine...",

            "📄 Generating Medicine Report..."

        ]



        for i in range(100):

            time.sleep(0.02)

            progress.progress(
                i + 1
            )


            if i < 25:

                status.info(
                    steps[0]
                )

            elif i < 50:

                status.info(
                    steps[1]
                )

            elif i < 75:

                status.info(
                    steps[2]
                )

            else:

                status.success(
                    steps[3]
                )



        files = {

            "file":
            (
                uploaded_file.name,

                uploaded_file.getvalue(),

                uploaded_file.type

            )

        }



        try:


            response = requests.post(

                "http://127.0.0.1:5000/scan-medicine",

                files=files,

                headers=headers

            )



            if response.status_code == 200:


                st.session_state["medicine"] = (
                    response.json()
                )


                st.success(
                    "✅ Medicine Identified Successfully"
                )



            else:


                st.error(
                    "Medicine scanning failed"
                )



        except Exception as e:


            st.error(
                f"Backend Error: {e}"
            )




# ------------------------------------
# Display Result
# ------------------------------------

medicine = st.session_state.get(
    "medicine"
)



if medicine:


    st.divider()


    st.header(
        "💊 Medicine Information"
    )



    col1,col2 = st.columns(2)



    with col1:

        st.metric(

            "Medicine Name",

            medicine.get(
                "name",
                "-"
            )

        )



    with col2:

        st.metric(

            "Generic Name",

            medicine.get(
                "generic_name",
                "-"
            )

        )



    st.divider()



    st.subheader(
        "🩺 Uses"
    )

    st.success(
        medicine.get(
            "uses",
            "Not Available"
        )
    )



    st.subheader(
        "💊 Dosage"
    )

    st.info(
        medicine.get(
            "dosage",
            "Consult Doctor"
        )
    )



    st.subheader(
        "⚠ Side Effects"
    )


    for item in medicine.get(
        "side_effects",
        []
    ):

        st.warning(
            item
        )



    st.subheader(
        "🚫 Precautions"
    )


    for item in medicine.get(
        "precautions",
        []
    ):

        st.write(
            "✅",
            item
        )



    st.subheader(
        "📦 Storage"
    )


    st.info(
        medicine.get(
            "storage",
            "-"
        )
    )



    st.subheader(
        "🍽 Food Interaction"
    )


    st.write(
        medicine.get(
            "food",
            "-"
        )
    )



    st.subheader(
        "🤖 AI Summary"
    )


    st.success(
        medicine.get(
            "summary",
            "-"
        )
    )



    st.divider()



    col1,col2 = st.columns(2)



    with col1:

        if st.button(
            "⏰ Add Medicine Reminder"
        ):

            st.switch_page(
                "pages/Medicine_Reminders.py"
            )



    with col2:

        if st.button(
            "💬 Ask AI Chatbot"
        ):

            st.switch_page(
                "pages/AI_Chatbot.py"
            )



st.warning(
"""
⚠️ Medical Disclaimer

MediSense Hospital AI Medicine Scanner provides information only.
Always follow your doctor's prescription before taking medicines.
"""
)