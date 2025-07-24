import streamlit as st
import sqlite3
from datetime import datetime

# --- Hardcoded credentials ---
USER_CREDENTIALS = {
    "user1": "pass123",
    "admin": "admin@123"
}

# --- DB Initialization ---
def init_db():
    conn = sqlite3.connect("actions.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            action TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

# --- Log user action ---
def log_action(username, action):
    conn = sqlite3.connect("actions.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user_actions (username, action, timestamp) VALUES (?, ?, ?)",
        (username, action, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()

# --- Session state ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# --- Init DB ---
init_db()

# --- Inject CSS ---
st.markdown("""
    <style>
        .mobile-container {
            max-width: 400px;
            margin: 2rem auto;
            background-color: #f3e8ff;
            padding: 2rem 1.5rem;
            border-radius: 2rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            border: 1px solid #e0d4fc;
        }
        .logo-text {
            font-size: 1.5rem;
            font-weight: bold;
            color: #6d28d9;
            text-align: center;
            margin-bottom: 0.25rem;
        }
        .greeting {
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            color: #4b5563;
        }
        .stButton>button {
            background-color: #6d28d9;
            color: white;
            border-radius: 10px;
            width: 100%;
            padding: 0.75rem 0;
            margin-top: 1rem;
        }
        .stTextInput>div>input {
            padding: 0.6rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Main Content Wrapper ---
with st.container():
    st.markdown('<div class="mobile-container">', unsafe_allow_html=True)

    if not st.session_state.logged_in:
        # Login Page
        st.markdown('<div class="logo-text">WELLS FARGO</div>', unsafe_allow_html=True)
        st.markdown('<div class="greeting">Good morning 👋</div>', unsafe_allow_html=True)

        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")

        if st.button("Sign On"):
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                log_action(username, "Login")
                st.rerun()
            else:
                st.error("Invalid username or password.")
    else:
        # Dashboard Page
        st.markdown(f'<div class="logo-text">Welcome, {st.session_state.username}!</div>', unsafe_allow_html=True)
        st.markdown('<div class="greeting">What would you like to do?</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("💰 Check Balance"):
                log_action(st.session_state.username, "Check Balance")
                st.info("Your current balance is ₹1,20,000")
            if st.button("📤 Logout"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.rerun()

        with col2:
            if st.button("💳 Pay Bills"):
                log_action(st.session_state.username, "Pay Bills")
                st.success("Redirecting to bill payment...")
            if st.button("🔁 Transfer"):
                log_action(st.session_state.username, "Transfer Funds")
                st.success("Redirecting to transfer page...")

    st.markdown('</div>', unsafe_allow_html=True)
