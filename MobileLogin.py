import streamlit as st
from datetime import datetime

# Dummy user credentials
USER_CREDENTIALS = {
    "user1": "pass123",
    "admin": "admin@123"
}

# Streamlit page setup
st.set_page_config(page_title="Mobile App", layout="centered")

# Inject custom styles for mobile look
st.markdown("""
    <style>
    body {
        background: linear-gradient(160deg, #e0e7ff, #c084fc);
    }
    .mobile-frame {
        max-width: 375px;
        margin: 3rem auto;
        padding: 2rem 1.5rem;
        background-color: white;
        border-radius: 2rem;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
        border: 1px solid #d1d5db;
    }
    .logo-text {
        font-size: 1.4rem;
        font-weight: bold;
        color: #6d28d9;
        text-align: center;
        margin-bottom: 0.5rem;
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
    .menu-btn {
        background-color: #ede9fe;
        color: #4c1d95;
        border: 1px solid #c4b5fd;
        width: 100%;
        padding: 0.75rem;
        border-radius: 10px;
        font-weight: 500;
        font-size: 1rem;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Login Screen
def show_login():
    with st.container():
        st.markdown('<div class="mobile-frame">', unsafe_allow_html=True)

        st.markdown('<div class="logo-text">WELLS FARGO</div>', unsafe_allow_html=True)
        st.markdown('<div class="greeting">Good morning 👋</div>', unsafe_allow_html=True)

        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", placeholder="Enter your password", type="password")

        if st.button("Sign On", type="primary"):
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")

        st.markdown('</div>', unsafe_allow_html=True)

# Dashboard Screen
def show_dashboard():
    with st.container():
        st.markdown('<div class="mobile-frame">', unsafe_allow_html=True)

        st.markdown(f'<div class="logo-text">WELLS FARGO</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="greeting">Hi {st.session_state.username.title()}, how can I help you today?</div>', unsafe_allow_html=True)

        # Action buttons
        st.markdown('<button class="menu-btn">📋 Account Summary</button>', unsafe_allow_html=True)
        st.markdown('<button class="menu-btn">💸 Transfer Funds</button>', unsafe_allow_html=True)
        st.markdown('<button class="menu-btn">🧾 View Transactions</button>', unsafe_allow_html=True)
        st.markdown('<button class="menu-btn">⚙️ Settings</button>', unsafe_allow_html=True)

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.experimental_rerun()

        st.markdown('</div>', unsafe_allow_html=True)

# Show appropriate screen
if st.session_state.logged_in:
    show_dashboard()
else:
    show_login()
