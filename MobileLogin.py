import streamlit as st
import sqlite3
from datetime import datetime

USER_CREDENTIALS = {
    "user1": "pass123",
    "admin": "admin@123"
}

# Initialize DB
def init_db():
    conn = sqlite3.connect("actions.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            action TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_action(username, action):
    conn = sqlite3.connect("actions.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_actions (username, action, timestamp) VALUES (?, ?, ?)",
                   (username, action, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def show_login():
    st.markdown("### 🔐 Login")
    username = st.text_input("👤 Username", placeholder="Enter your username")
    password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
    
    if st.button("🚀 Login", use_container_width=True):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.experimental_rerun()
        else:
            st.error("❌ Invalid username or password")

def show_dashboard():
    st.markdown(f"### 👋 Hi, {st.session_state.username}")
    st.markdown("#### How may I help you today?")

    st.button("📊 View Reports", use_container_width=True,
              on_click=lambda: handle_click("View Reports"))
    
    st.button("📦 Orders", use_container_width=True,
              on_click=lambda: handle_click("Orders"))
    
    st.button("⚙️ Settings", use_container_width=True,
              on_click=lambda: handle_click("Settings"))
    
    st.button("🚪 Logout", use_container_width=True, on_click=logout)

def handle_click(action_name):
    log_action(st.session_state.username, action_name)
    st.success(f"✅ {action_name} clicked!")

def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.experimental_rerun()

# App Initialization
init_db()
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# Clean layout for mobile
st.set_page_config(page_title="Mobile App", layout="centered")

# Display correct screen
if st.session_state.logged_in:
    show_dashboard()
else:
    show_login()
