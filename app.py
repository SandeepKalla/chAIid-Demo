
import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import random

# App config with custom theme color
st.set_page_config(
    page_title="chAIid – Baby Care Assistant",
    layout="centered",
    initial_sidebar_state="auto"
)

# Custom styling for fonts and sky-blue healthcare theme
custom_css = '''
<style>
body {
    background-color: #f0f8ff;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3, h4 {
    color: #004e89;
}
.stButton > button {
    background-color: #0096c7;
    color: white;
    font-weight: bold;
    border-radius: 5px;
}
.stTextInput > div > input {
    background-color: #ffffff;
    border: 1px solid #a6dcef;
}
.stSelectbox > div > div {
    background-color: #ffffff;
    border: 1px solid #a6dcef;
}
</style>
'''
st.markdown(custom_css, unsafe_allow_html=True)

st.title("chAIid – AI Baby Care Assistant")
st.subheader("Simulated prototype for rural parenting support")

# 1. Baby Profile Setup
st.header("Baby Profile Setup")
with st.form("baby_form"):
    name = st.text_input("Baby's Name")
    dob = st.date_input("Date of Birth")
    ward = st.text_input("Ward/Locality")
    phone = st.text_input("Parent Phone Number (for SMS alert simulation)")
    submitted = st.form_submit_button("Save Profile")
    if submitted:
        st.success(f"Profile for {name} saved.")
        next_vaccine = dob + timedelta(days=45)
        st.info(f"Next Vaccine Due (e.g., DPT1/OPV): {next_vaccine.strftime('%Y-%m-%d')}")
        st.success(f"SMS sent to {phone}: 'Your baby's next vaccine is due on {next_vaccine.strftime('%Y-%m-%d')}'")

# 2. AI Chatbot (Mocked)
st.header("Ask chAIid a Baby Care Question")
user_question = st.text_input("Type your concern (e.g., 'My baby has a cold')")
if user_question:
    st.subheader("AI Suggestion:")
    if "fever" in user_question.lower():
        st.write("Monitor the baby's temperature. Keep them hydrated. If fever exceeds 100.4°F, visit the nearest PHC.")
    elif "food" in user_question.lower():
        st.write("For babies above 6 months, soft foods like mashed banana, boiled potato, or khichdi are good.")
    else:
        st.write("Thank you for your question. Please monitor the baby and consult a local health worker if symptoms persist.")

# 3. Rash Detection Placeholder (OpenAI/Model Integration Area)
st.header("Upload a Rash Photo for Analysis (Prototype)")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Analyzing image...")

    # MOCK: Replace with actual model inference / OpenAI call if needed
    condition = random.choice(["Heat Rash", "Eczema", "Diaper Rash", "Normal Skin"])
    st.success(f"Detected Condition: {condition}")
    st.caption("Note: This is a simulated result. Consult a healthcare provider for a real diagnosis.")

# 4. Hospital Finder (Mocked)
st.header("Find Nearby Hospitals")
ward_choice = st.selectbox("Select your ward", ["Ward 1", "Ward 2", "Ward 3"])
hospitals = {
    "Ward 1": [("Govt PHC A", "1.2 km", "Free"), ("City Hospital X", "2.4 km", "₹250")],
    "Ward 2": [("Anganwadi Center B", "0.8 km", "Free"), ("Private Clinic Y", "1.6 km", "₹300")],
    "Ward 3": [("PHC C", "1.0 km", "Free"), ("Hospital Z", "3.1 km", "₹200")]
}
st.subheader("Nearby Health Facilities:")
for name, dist, cost in hospitals[ward_choice]:
    st.markdown(f"- **{name}** – {dist}, Cost: {cost}")
