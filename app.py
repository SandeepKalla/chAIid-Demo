import streamlit as st
import random

# App setup
st.set_page_config(page_title="chAIid - BabyCare", layout="centered")
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #E6F4F1;
    }
    .stButton>button {
        background-color: #2BBBAD;
        color: white;
        font-weight: bold;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("chAIid – Smart BabyCare Assistant")

# 1. OTP Verification (Mock)
st.header("🔐 Mobile Verification (Demo)")
phone = st.text_input("Enter your mobile number (for demo only)")

if st.button("Send OTP"):
    otp = str(random.randint(100000, 999999))
    st.session_state["mock_otp"] = otp
    st.success(f"OTP sent to {phone} ✅ (Demo Mode)")
    st.caption(f"(Your demo OTP is: {otp})")

entered_otp = st.text_input("Enter the OTP you received")

if st.button("Verify OTP"):
    if entered_otp == st.session_state.get("mock_otp"):
        st.session_state["authenticated"] = True
        st.success("OTP Verified Successfully 🎉")
    else:
        st.error("Incorrect OTP. Please try again.")

# 2. Main App Access Post-Verification
if st.session_state.get("authenticated"):
    st.markdown("---")
    st.header("Welcome to chAIid")
    st.write("✅ Access granted to smart baby care features.")
    # Placeholder for the rest of your app UI/components
