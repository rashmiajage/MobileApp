import streamlit as st

# Page setup
st.set_page_config(page_title="Mobile Styled App", layout="centered")

# Mobile container style
st.markdown("""
    <style>
        .mobile-container {
            width: 375px;
            margin: 40px auto;
            padding: 30px 20px;
            border: 8px solid #ccc;
            border-radius: 30px;
            background-color: #f3e8ff; /* light purple */
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        .logo {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #5e17eb;
            margin-bottom: 5px;
        }
        .greeting {
            text-align: center;
            font-size: 16px;
            color: #333;
            margin-bottom: 30px;
        }
        .input-field {
            margin-bottom: 20px;
        }
        .button-style {
            background-color: #5e17eb;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            width: 100%;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Session state to switch screens
if "signed_in" not in st.session_state:
    st.session_state.signed_in = False

# Mobile screen content
with st.container():
    st.markdown('<div class="mobile-container">', unsafe_allow_html=True)

    if not st.session_state.signed_in:
        st.markdown('<div class="logo">WELLS FARGO</div>', unsafe_allow_html=True)
        st.markdown('<div class="greeting">Good morning 👋</div>', unsafe_allow_html=True)

        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")

        if st.button("Sign On", use_container_width=True):
            # Dummy login logic
            if username and password:
                st.session_state.signed_in = True
            else:
                st.warning("Please enter both username and password.")
    else:
        st.markdown('<div class="logo">WELLS FARGO</div>', unsafe_allow_html=True)
        st.markdown('<div class="greeting">Welcome to your Dashboard</div>', unsafe_allow_html=True)

        # Dashboard content
        st.success("✅ Account Verified")
        st.metric("Balance", "$5,000")
        st.metric("Recent Transactions", "3")
        st.button("Logout", use_container_width=True, on_click=lambda: st.session_state.update({"signed_in": False}))

    st.markdown('</div>', unsafe_allow_html=True)
