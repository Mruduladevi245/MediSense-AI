import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import os


st.set_page_config(
    page_title="MediSense Hospital Health Analytics",
    page_icon="📊",
    layout="wide"
)


# -----------------------------
# Authentication
# -----------------------------

if "token" not in st.session_state:

    st.warning("Please login first.")

    st.switch_page(
        "pages/Login.py"
    )



# -----------------------------
# Header Image
# -----------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)


IMAGE_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "images",
    "medisense-ai-analytics.jpg.png"
)


if os.path.exists(IMAGE_PATH):

    st.image(
        IMAGE_PATH,
        use_container_width=True
    )

else:

    st.warning(
        "Health analytics image not found."
    )



# -----------------------------
# Title
# -----------------------------

st.title(
    "📊 MediSense Hospital Health Analytics"
)


st.caption(
    "AI-powered health insights, trends, and personalized monitoring."
)


st.divider()



# -----------------------------
# Health Summary Cards
# -----------------------------

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "❤️ Health Score",
        "86%",
        "+5%"
    )


with c2:

    st.metric(
        "🩸 Blood Pressure",
        "120/80",
        "Stable"
    )


with c3:

    st.metric(
        "⚖ Weight",
        "64 kg",
        "-2 kg"
    )


with c4:

    st.metric(
        "💧 Water Intake",
        "2.5 L",
        "Good"
    )



st.divider()



# -----------------------------
# Health Trend Chart
# -----------------------------

col1, col2 = st.columns(2)



with col1:

    st.subheader(
        "📈 Health Score Trend"
    )


    fig = go.Figure()


    fig.add_trace(

        go.Scatter(

            x=[
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun"
            ],

            y=[
                70,
                74,
                76,
                80,
                83,
                86
            ],

            mode="lines+markers",

            name="Health Score"

        )

    )


    fig.update_layout(
        height=350
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



with col2:

    st.subheader(
        "🥗 Nutrition Analysis"
    )


    nutrition = {

        "Protein":35,

        "Carbs":40,

        "Fats":25

    }


    fig2 = px.pie(

        values=list(nutrition.values()),

        names=list(nutrition.keys()),

        title="Daily Nutrition Balance"

    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )



st.divider()



# -----------------------------
# Health Parameters
# -----------------------------

st.subheader(
    "🩺 Health Parameters"
)


parameters = [

    {
        "Parameter":"Blood Sugar",
        "Value":"98 mg/dL",
        "Status":"Normal"
    },

    {
        "Parameter":"Cholesterol",
        "Value":"180 mg/dL",
        "Status":"Normal"
    },

    {
        "Parameter":"BMI",
        "Value":"25",
        "Status":"Monitor"
    },

    {
        "Parameter":"Vitamin D",
        "Value":"22 ng/mL",
        "Status":"Low"
    }

]


st.dataframe(
    parameters,
    use_container_width=True
)



st.divider()



# -----------------------------
# AI Insights
# -----------------------------

st.subheader(
    "🤖 MediSense AI Health Insights"
)


st.success(
"""
✅ Your heart health indicators are stable.
"""
)


st.info(
"""
💧 Maintain proper hydration and balanced nutrition.
"""
)


st.warning(
"""
⚠ Vitamin D level may need improvement.
"""
)


st.success(
"""
🏃 Regular physical activity is improving your health score.
"""
)



st.divider()



# -----------------------------
# Recommendations
# -----------------------------

st.subheader(
    "🌱 Personalized Recommendations"
)


recommendations = [

    "Walk at least 30 minutes daily",

    "Include more protein-rich foods",

    "Maintain consistent sleep schedule",

    "Monitor blood pressure regularly",

    "Upload new reports for updated AI analysis"

]


for item in recommendations:

    st.write(
        "✅",
        item
    )



st.divider()



# -----------------------------
# Disclaimer
# -----------------------------

st.warning(
"""
⚠️ Medical Disclaimer

MediSense Hospital Health Analytics provides AI-based insights for awareness only.
It does not replace professional medical diagnosis or treatment.
"""
)