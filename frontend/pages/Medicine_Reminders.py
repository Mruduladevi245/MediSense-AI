import streamlit as st
import os
import requests


st.set_page_config(
    page_title="Medicine Reminders",
    page_icon="💊",
    layout="wide"
)


# =====================================
# Image Helper
# =====================================

def get_image(filename):

    image_path = os.path.join(
        "assets",
        "images",
        filename
    )

    if os.path.exists(image_path):
        return image_path

    return None



# =====================================
# Authentication
# =====================================

if "token" not in st.session_state:

    st.warning(
        "Please login first."
    )

    st.switch_page(
        "pages/Login.py"
    )


token = st.session_state["token"]


headers = {
    "Authorization": f"Bearer {token}"
}



# =====================================
# Header Image
# =====================================

medicine_img = get_image(
    "medisense-medicine-management.jpg.png"
)


if medicine_img:

    st.image(
        medicine_img,
        use_container_width=True
    )



# =====================================
# Page Title
# =====================================

st.title(
    "💊 MediSense Medicine Reminder"
)


st.caption(
    "Smart medicine tracking and reminder management system."
)


st.divider()



# =====================================
# Add Medicine Reminder
# =====================================

st.subheader(
    "➕ Add Medicine Reminder"
)


col1, col2 = st.columns(2)


with col1:

    medicine_name = st.text_input(
        "💊 Medicine Name"
    )


with col2:

    reminder_time = st.time_input(
        "⏰ Reminder Time"
    )



if st.button(
    "💾 Save Reminder",
    use_container_width=True
):

    if medicine_name == "":

        st.error(
            "Please enter medicine name."
        )

    else:

        data = {

            "medicine": medicine_name,

            "time": str(reminder_time)

        }


        try:

            response = requests.post(

                "http://127.0.0.1:5000/reminders",

                json=data,

                headers=headers

            )


            if response.status_code in [200,201]:

                st.success(
                    "✅ Reminder saved successfully!"
                )

            else:

                st.error(
                    "Failed to save reminder."
                )


        except Exception as e:

            st.error(
                f"Backend Error: {e}"
            )



st.divider()



# =====================================
# Medicine Schedule
# =====================================

st.subheader(
    "📋 My Medicine Schedule"
)



try:

    response = requests.get(

        "http://127.0.0.1:5000/reminders",

        headers=headers

    )


    if response.status_code == 200:


        reminders = response.json()



        if reminders:


            for reminder in reminders:


                st.success(
                    f"""
💊 Medicine : {reminder.get('medicine')}

⏰ Time : {reminder.get('time')}
"""
                )


        else:


            st.info(
                "No medicine reminders available."
            )


    else:

        st.warning(
            "Unable to load reminders."
        )



except Exception:


    st.warning(
        "Backend server is not running."
    )



st.divider()



# =====================================
# Health Tips
# =====================================

st.subheader(
    "🌿 Medicine Safety Tips"
)


tips = [

    "Take medicines at the prescribed time.",

    "Do not skip doses without doctor's advice.",

    "Maintain a regular medicine schedule.",

    "Keep medicines stored safely."

]


for tip in tips:

    st.write(
        "✅",
        tip
    )



st.divider()



st.warning(
"""
⚠️ Medical Disclaimer

MediSense Medicine Reminder only helps track medicine schedules.
Always follow your doctor's prescription and medical advice.
"""
)