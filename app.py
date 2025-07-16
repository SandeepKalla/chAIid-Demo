
import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import random

st.set_page_config(page_title="chAIid Demo", layout="centered")

st.title("🤖 chAIid – AI Baby Care Assistant (Demo)")
st.markdown("This prototype simulates core features of the chAIid app for rural parenting support.")

# 1. Baby Profile Setup
st.header("👶 Baby Profile Setup")
with st.form("baby_form"):
    name = st.text_input("Baby's Name")
    dob = st.date_input("Date of Birth")
    ward = st.text_input("Ward/Locality")
    phone = st.text_input("Parent Phone Number (for SMS alert simulation)")
    submitted = st.form_submit_button("Save Profile")
    if submitted:
        st.success(f"Profile for {name} saved. SMS alerts will be sent to {phone} (simulated).")
        next_vaccine = dob + timedelta(days=45)
        st.info(f"Next Vaccine Due Date (DPT1/OPV): {next_vaccine.strftime('%Y-%m-%d')}")

# 2. AI Chatbot (Mocked)
st.header("💬 Ask chAIid a Baby Care Question")
user_question = st.text_input("Ask your question (e.g., 'My baby has a cold')")
if user_question:
    st.subheader("chAIid Says:")
    st.write("Based on your input, here's a general suggestion:")
    if "fever" in user_question.lower():
        st.write("Monitor the baby's temperature. Keep them hydrated. If fever exceeds 100.4°F, visit the nearest PHC.")
    elif "food" in user_question.lower():
        st.write("For babies above 6 months, soft foods like mashed banana, boiled potato, or khichdi are good.")
    else:
        st.write("Thank you for your question. Please monitor the baby and consult a local health worker if needed.")

# 3. Rash Detection (Mocked)
st.header("📷 Upload a Rash Photo (Mock Detector)")
uploaded_file = st.file_uploader("Upload an image of the rash", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Analyzing...")
    condition = random.choice(["Heat Rash", "Mild Eczema", "Normal Skin Condition"])
    st.success(f"Prediction: {condition}")
    st.caption("Note: This is a demo. Always consult a healthcare provider.")

# 4. Hospital Finder (Mock)
st.header("🏥 Find Nearby Hospitals")
ward_choice = st.selectbox("Select your ward", ["Ward 1", "Ward 2", "Ward 3"])
hospitals = {
    "Ward 1": [("Govt PHC A", "1.2 km", "Free"), ("City Hospital X", "2.4 km", "₹250")],
    "Ward 2": [("Anganwadi Center B", "0.8 km", "Free"), ("Private Clinic Y", "1.6 km", "₹300")],
    "Ward 3": [("PHC C", "1.0 km", "Free"), ("Hospital Z", "3.1 km", "₹200")]
}
st.subheader("Nearby Facilities:")
for name, dist, cost in hospitals[ward_choice]:
    st.markdown(f"- **{name}** – {dist}, Cost: {cost}")
