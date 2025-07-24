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

# --- Inject Custom CSS ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(160deg, #e0e7ff, #c084fc);
        }
        .mobile-frame {
            max-width: 375px;
            margin: 3rem auto;
            padding: 2rem 1.5rem;
            background-color: #f3e8ff;
            border-radius: 2rem;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            border: 1px solid #d1d5db;
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
            margin-bottom: 1.5rem;
            color: #4b5563;
        }
        .btn {
            width: 100%;
            background-color: #6d28d9;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.75rem;
            font-size: 1rem;
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Init DB ---
init_db()

# --- Session state for login ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# --- Main UI ---
with st.container():
    st.markdown('<div class="mobile-frame">', unsafe_allow_html=True)

    if not st.session_state.logged_in:
        # Login Screen
        st.markdown('<div class="logo-text">WELLS FARGO</div>', unsafe_allow_html=True)
        st.markdown('<div class="greeting">Good morning 👋</div>', unsafe_allow_html=True)

        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")

        if st.button("Sign On"):
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                log_action(username, "Login")
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials. Please try again.")
    else:
        # Dashboard
        st.markdown(f'<div class="logo-text">Welcome, {st.session_state.username}!</div>', unsafe_allow_html=True)
        st.markdown('<div class="greeting">How may I help you today?</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Check Balance"):
                log_action(st.session_state.username, "Check Balance")
                st.info("Balance: ₹1,20,000")

            if st.button("Pay Bills"):
                log_action(st.session_state.username, "Pay Bills")
                st.success("Bill payment screen loading...")

        with col2:
            if st.button("Transfer Funds"):
                log_action(st.session_state.username, "Transfer Funds")
                st.success("Transfer screen loading...")

            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
