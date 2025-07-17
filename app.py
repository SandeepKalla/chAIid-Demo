import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import random
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("FAST2SMS_API_KEY")

# Custom styles for font and theme
st.set_page_config(page_title="chAIid – Baby Care Assistant", layout="centered")

custom_css = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
body, div, input, button, textarea {
    font-family: 'Roboto', sans-serif;
}
body {
    background-color: #E6F4F1;
}
h1, h2, h3 {
    color: #004e89;
}
.stButton > button {
    background-color: #2BBBAD;
    color: white;
    font-weight: bold;
    border-radius: 5px;
}
</style>
'''
st.markdown(custom_css, unsafe_allow_html=True)

st.title("chAIid – AI Baby Care Assistant")

# OTP Section
st.header("Phone Verification via OTP")
if 'otp_sent' not in st.session_state:
    st.session_state['otp_sent'] = False
if 'generated_otp' not in st.session_state:
    st.session_state['generated_otp'] = None

phone = st.text_input("Enter your 10-digit mobile number")
if st.button("Send OTP"):
    if len(phone) == 10 and phone.isdigit():
        otp = random.randint(100000, 999999)
        st.session_state['generated_otp'] = str(otp)
        st.session_state['otp_sent'] = True

        url = "https://www.fast2sms.com/dev/bulkV2"
        payload = {
            "authorization": API_KEY,
            "message": f"Your chAIid OTP is {otp}",
            "language": "english",
            "route": "q",
            "numbers": phone
        }
        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, params=payload, headers=headers)

        if response.status_code == 200:
            st.success(f"OTP sent to +91-{phone}")
        else:
            st.error("Failed to send OTP. Please check your Fast2SMS credentials.")
    else:
        st.error("Please enter a valid 10-digit mobile number.")

# OTP Verification
if st.session_state['otp_sent']:
    entered_otp = st.text_input("Enter the OTP you received", type="password")
    if st.button("Verify OTP"):
        if entered_otp == st.session_state['generated_otp']:
            st.success("OTP verified successfully!")
        else:
            st.error("Invalid OTP. Please try again.")

st.caption("Note: This is a real SMS OTP demo using Fast2SMS. Your number will receive live messages.")
