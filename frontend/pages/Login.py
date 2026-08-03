import streamlit as st
import requests


st.set_page_config(
    page_title="MediSense Hospital Login",
    page_icon="🏥",
    layout="centered"
)


# -----------------------------
# Header Image
# -----------------------------

st.image(
    "assets/images/medisense-hospital-lobby.jpg.png",
    use_container_width=True
)


# -----------------------------
# Title
# -----------------------------

st.title(
    "🏥 MediSense Hospital Login"
)

st.caption(
    "Access your AI-powered healthcare dashboard"
)

st.divider()


# -----------------------------
# Login Form
# -----------------------------

email = st.text_input(
    "📧 Email"
)


password = st.text_input(
    "🔑 Password",
    type="password"
)


if st.button(
    "🔐 Login",
    use_container_width=True
):

    if not email or not password:
        st.warning("Please enter email and password.")

    else:

        data = {
            "email": email,
            "password": password
        }


        try:

            response = requests.post(
                "http://127.0.0.1:5000/login",
                json=data
            )


            if response.status_code == 200:

                result = response.json()

                token = result.get(
                    "token",
                    ""
                )


                st.session_state["token"] = token


                st.success(
                    "✅ Login Successful"
                )


                st.switch_page(
                    "pages/Dashboard.py"
                )


            else:

                st.error(
                    response.json().get(
                        "message",
                        "Invalid login credentials"
                    )
                )


        except Exception as e:

            st.error(
                f"Backend connection error: {e}"
            )


st.divider()


# -----------------------------
# Register Navigation
# -----------------------------

st.write(
    "Don't have an account?"
)


if st.button(
    "📝 Create New Account",
    use_container_width=True
):

    st.switch_page(
        "pages/Register.py"
    )


st.divider()


st.info(
"""
🏥 **MediSense Hospital**

AI-powered healthcare platform for:

✅ Medical Report Analysis  
✅ Prescription Reading  
✅ Medicine Scanner  
✅ Health Analytics  
✅ AI Healthcare Assistant
"""
)