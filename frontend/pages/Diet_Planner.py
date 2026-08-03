import streamlit as st
import os


st.set_page_config(
    page_title="Diet Planner",
    page_icon="🥗",
    layout="wide"
)


# -----------------------------
# Image Path Fix
# -----------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

IMAGE_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "images",
    "medisense-patient-care.jpg.png"
)


# -----------------------------
# Header Image
# -----------------------------

if os.path.exists(IMAGE_PATH):

    st.image(
        IMAGE_PATH,
        use_container_width=True
    )

else:

    st.warning(
        "Diet planner image not found."
    )


# -----------------------------
# Page Content
# -----------------------------

st.title(
    "🥗 AI Diet Planner"
)


st.caption(
    "Personalized nutrition recommendations powered by MediSense AI"
)


st.divider()


col1, col2, col3 = st.columns(3)


with col1:

    st.success(
        """
        🍎 Healthy Diet Plans

        - Weight management
        - Diabetes-friendly meals
        - Heart healthy diet
        """
    )


with col2:

    st.info(
        """
        🥗 Nutrition Tracking

        - Calories
        - Protein
        - Vitamins
        - Minerals
        """
    )


with col3:

    st.warning(
        """
        💧 Lifestyle Advice

        - Water intake
        - Sleep
        - Daily habits
        """
    )


st.divider()


st.subheader(
    "Generate Your Diet Plan"
)


age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=20
)


weight = st.number_input(
    "Weight (kg)",
    min_value=1,
    value=60
)


height = st.number_input(
    "Height (cm)",
    min_value=50,
    value=160
)


goal = st.selectbox(
    "Health Goal",
    [
        "Weight Loss",
        "Weight Gain",
        "Maintain Weight",
        "Muscle Building"
    ]
)


if st.button(
    "Generate Diet Plan"
):

    bmi = weight / ((height/100)**2)


    st.success(
        "Your AI Diet Plan is Ready!"
    )


    st.write(
        f"""
        ### Health Details

        BMI: {round(bmi,2)}

        Goal: {goal}


        ### Recommended Meals

        🌅 Breakfast:
        - Oats / Eggs / Fruits

        🍛 Lunch:
        - Rice/Chapati + Vegetables + Protein

        🌙 Dinner:
        - Light meal with vegetables

        🥤 Hydration:
        - Drink 2-3 litres water daily
        """
    )


st.divider()


st.caption(
    "MediSense AI 🏥 | Smart Healthcare Assistant"
)