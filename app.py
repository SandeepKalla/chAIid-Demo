from random import randint
import streamlit as st

# Page Configuration
st.set_page_config(page_title="chAIid – Smart BabyCare Assistant", layout="centered")

# Updated Styling with Inter font and healthcare colors
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
</style>
""", unsafe_allow_html=True)

# App Title
st.title("chAIid – Smart BabyCare Assistant")
st.header("🔒 Mobile Verification (Demo)")

# OTP Flow
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

        # Placeholder for more features
        st.markdown("🚧 More features like:")
        st.markdown("- 📅 Vaccine Alerts\n- 🗣️ Voice Support\n- 📸 Rash Detection\n- 📈 Growth Monitoring")
    else:
        st.error("Incorrect OTP. Please try again.")
