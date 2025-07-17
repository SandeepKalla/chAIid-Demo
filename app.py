
from random import randint
import streamlit as st
from PIL import Image
import time

# Page Config
st.set_page_config(page_title="chAIid – Smart BabyCare Assistant", layout="centered")

# Custom Styles
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #E6F4F1;
    color: #1F2937;
}

h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    color: #0D47A1;
}

.stButton > button {
    background-color: #2BBBAD;
    color: white;
    font-weight: bold;
    border-radius: 6px;
    padding: 0.5rem 1rem;
    font-size: 16px;
    margin-top: 5px;
}

.stTextInput > div > input {
    border-radius: 5px;
    padding: 10px;
    font-size: 15px;
}

img {
    border-radius: 10px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("chAIid – Smart BabyCare Assistant")
st.header("🔒 Mobile Verification (Demo)")

# OTP Verification
phone = st.text_input("Enter your mobile number (for demo only)")

if st.button("Send OTP"):
    otp = str(randint(100000, 999999))
    st.session_state['mock_otp'] = otp
    st.success(f"OTP sent to {phone} ✅ (mock mode)")
    st.caption(f"(In demo, OTP is: {otp})")

entered_otp = st.text_input("Enter the OTP you received")

if st.button("Verify OTP"):
    if entered_otp == st.session_state.get('mock_otp'):
        st.success("OTP Verified Successfully 🎉")
        st.markdown("---")
        st.subheader("Welcome to chAIid")
        st.success("✅ Access granted to smart baby care features.")

        # --- Feature 1: Vaccine Info ---
        st.markdown("### 💉 Vaccination Schedule")
        baby_age = st.slider("Select baby age in months", 0, 24, 3)
        if baby_age <= 6:
            st.info("Recommended: BCG, OPV, HepB, DTP, Hib, Rotavirus")
        elif baby_age <= 12:
            st.info("Recommended: MMR, IPV, Vitamin A")
        else:
            st.info("Recommended: Booster shots (DTP, MMR), Typhoid")

        # --- Feature 2: Rash Detection Mock ---
        st.markdown("### 📸 Rash Detection (Mock)")
        rash_img = st.file_uploader("Upload baby's rash image (for demo)", type=["jpg", "jpeg", "png"])
        if rash_img:
            image = Image.open(rash_img)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            with st.spinner("Analyzing rash..."):
                time.sleep(2)
                st.success("🟢 Analysis Result: No major concern. Common rash (mock demo).")

        # --- Feature 3: AI Q&A ---
        st.markdown("### 🤖 Ask AI a BabyCare Question")
        q = st.text_input("Type your question:")
        if q:
            with st.spinner("Thinking..."):
                time.sleep(1.5)
                st.success("🧠 AI Answer (demo): Make sure to burp the baby after feeding to avoid gas issues.")

    else:
        st.error("Incorrect OTP. Please try again.")
