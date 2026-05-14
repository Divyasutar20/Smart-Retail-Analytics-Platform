import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# =========================
# DATABASE CONNECTION
# =========================

engine = create_engine(
    "mysql+pymysql://root:@localhost:3307/smart_retail_db"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
}

.login-container {
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
    margin-top: 50px;
}

.title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #D3D3D3;
    font-size: 18px;
    margin-bottom: 30px;
}

.stTextInput > div > div > input {
    background-color: rgba(255,255,255,0.1);
    color: white;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.2);
}

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #00C6FF, #0072FF);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
}

.stButton>button:hover {
    transform: scale(1.02);
    transition: 0.3s;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOGIN FUNCTION
# =========================

def login():

    col1, col2, col3 = st.columns([1, 1.2, 1])

    with col2:

        st.markdown("""
        <div class='login-container'>
        <div class='title'>🧠 Smart Retail Analytics</div>
        <div class='subtitle'>
        AI-Powered Business Intelligence Platform
        </div>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input(
            "👤 Username"
        )

        password = st.text_input(
            "🔑 Password",
            type="password"
        )

        if st.button("🚀 Login"):

            query = f"""
            SELECT * FROM users
            WHERE username='{username}'
            AND password='{password}'
            """

            user = pd.read_sql(
                query,
                engine
            )

            if not user.empty:

                st.session_state["logged_in"] = True

                st.success(
                    "✅ Login Successful"
                )

                st.rerun()

            else:

                st.error(
                    "❌ Invalid Username or Password"
                )

        st.markdown("""
        <br>
        <center style='color:white;'>
        Developed by Divya Jitendra Sutar 🚀
        </center>
        """, unsafe_allow_html=True)