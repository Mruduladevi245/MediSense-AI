import streamlit as st
import requests
import time
from pathlib import Path


st.set_page_config(
    page_title="MediSense Hospital AI Report Analysis",
    page_icon="🧠",
    layout="wide"
)


# ---------------------------------
# Authentication
# ---------------------------------

if "token" not in st.session_state:

    st.warning("Please login first.")

    st.switch_page(
        "pages/Login.py"
    )


token = st.session_state["token"]


headers = {
    "Authorization": f"Bearer {token}"
}



# ---------------------------------
# Check Uploaded Report
# ---------------------------------

report_id = st.session_state.get(
    "report_id"
)


if not report_id:

    st.error(
        "No uploaded medical report found."
    )

    st.switch_page(
        "pages/Upload_Report.py"
    )



# ---------------------------------
# Header Image
# ---------------------------------

image_path = (
    Path(__file__).parent.parent
    / "assets"
    / "images"
    / "medisense-xray-diagnosis.jpg.png"
)


if image_path.exists():

    st.image(
        str(image_path),
        use_container_width=True
    )

else:

    st.warning(
        "Medical image not found."
    )



# ---------------------------------
# Title
# ---------------------------------

st.title(
    "🧠 MediSense Hospital AI Report Analysis"
)


st.caption(
    "AI analyzes your medical reports and explains results in simple language."
)


st.divider()



# ---------------------------------
# Start Analysis
# ---------------------------------

if st.button(
    "🚀 Start AI Medical Analysis",
    use_container_width=True
):

    progress = st.progress(0)

    status = st.empty()


    steps = [

        "📄 Reading Medical Report...",

        "🔍 Extracting Medical Parameters...",

        "🧠 AI Detecting Health Patterns...",

        "🍎 Generating Recommendations..."

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

            status.info(
                steps[3]
            )


    try:

        response = requests.post(

            "http://127.0.0.1:5000/analyze-report",

            json={
                "report_id": report_id
            },

            headers=headers

        )


        if response.status_code == 200:

            st.session_state["analysis"] = response.json()

            st.success(
                "✅ AI Analysis Completed Successfully"
            )


        else:

            st.error(
                response.json().get(
                    "message",
                    "Analysis Failed"
                )
            )


    except Exception:

        st.error(
            "Backend server is not running."
        )



# ---------------------------------
# Show Result
# ---------------------------------

analysis = st.session_state.get(
    "analysis"
)



if analysis:


    st.divider()


    col1, col2 = st.columns(2)


    with col1:

        st.subheader(
            "📄 Medical Summary"
        )


        st.write(

            analysis.get(
                "summary",
                "No summary available"
            )

        )



    with col2:

        st.subheader(
            "🏥 Health Score"
        )


        score = analysis.get(
            "health_score",
            82
        )


        st.metric(
            "Overall Health",
            f"{score}/100"
        )


        st.progress(
            score / 100
        )



    st.divider()



    st.subheader(
        "🔴 Abnormal Values"
    )


    abnormalities = analysis.get(
        "abnormal_values",
        []
    )


    if abnormalities:


        for item in abnormalities:


            st.error(

                f"""
**{item.get('parameter')}**

Value:
{item.get('value')}

Normal Range:
{item.get('normal_range')}
"""

            )


    else:


        st.success(
            "No abnormal values detected."
        )



    st.divider()



    st.subheader(
        "⚠ Health Risks"
    )


    risks = analysis.get(
        "health_risks",
        []
    )


    for risk in risks:

        st.warning(
            risk
        )



    st.subheader(
        "🍎 Diet Recommendations"
    )


    for diet in analysis.get(
        "diet",
        []
    ):

        st.success(
            diet
        )



    st.subheader(
        "🏃 Exercise Recommendations"
    )


    for exercise in analysis.get(
        "exercise",
        []
    ):

        st.info(
            exercise
        )



    st.subheader(
        "💧 Lifestyle Advice"
    )


    for tip in analysis.get(
        "lifestyle",
        []
    ):

        st.write(
            "✅",
            tip
        )



    st.subheader(
        "👨‍⚕ Doctor Advice"
    )


    st.info(

        analysis.get(

            "doctor_advice",

            "Consult your doctor for medical advice."

        )

    )



    st.divider()



    col1, col2 = st.columns(2)



    with col1:

        if st.button(
            "📄 Generate Doctor Summary"
        ):

            st.info(
                "Doctor Summary feature coming soon."
            )



    with col2:

        if st.button(
            "💊 Continue to Prescription"
        ):

            st.switch_page(
                "pages/Prescription.py"
            )