import streamlit as st
from PIL import Image

# ---- Page Settings ----
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

# ---- Header Section ----
st.title("💪 Body Mass Index (BMI) Calculator")
st.subheader("Calculate your BMI and check your health category instantly!")

# ---- Sidebar Input Section ----
st.sidebar.header("🧍 Enter Your Information")

name = st.sidebar.text_input("👤 Name", placeholder="e.g. Alex")
height = st.sidebar.number_input("📏 Height (in meters)", min_value=0.5, max_value=6.0, format="%.2f")
weight = st.sidebar.number_input("⚖️ Weight (in kilograms)", min_value=10.0, max_value=300.0, format="%.1f")

# ---- Calculate BMI ----
def calculate_bmi(weight, height):
    if height == 0:
        return 0
    return round(weight / (height ** 2), 2)

# ---- Display Results ----
if st.sidebar.button("🔍 Calculate BMI"):
    if name and height > 0 and weight > 0:
        bmi = calculate_bmi(weight, height)

        st.markdown(f"### 👋 Hello **{name}**, your BMI is:")
        st.markdown(f"<h2 style='color:#4CAF50'>{bmi}</h2>", unsafe_allow_html=True)

        # Categorize BMI
        if bmi < 18.5:
            st.warning("🍃 You're **Underweight** — Consider a nutritious diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a **Normal** weight — Great job!")
        elif 25 <= bmi < 29.9:
            st.info("⚠️ You're **Overweight** — Try to stay active.")
        else:
            st.error("🚨 You're **Obese** — Please consult a health professional.")
        
        st.divider()
        st.caption("💡 *BMI is just a guide. For exact health info, consult a doctor.*")
    else:
        st.error("Please fill in all fields to calculate your BMI.")
else:
    st.info("Enter your details in the sidebar and press **Calculate BMI**.")

# ---- Footer ----
st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>Made with ❤️ by [Muhammad Tahir Hasni]</div>",
    unsafe_allow_html=True
)
