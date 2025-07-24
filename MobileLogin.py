import streamlit as st

# Set page config
st.set_page_config(page_title="Mobile App", layout="centered")

# Inject custom CSS for the mobile container
st.markdown("""
    <style>
        .mobile-wrapper {
            max-width: 375px;
            margin: 50px auto;
            background-color: #f3e8ff;
            padding: 30px 20px;
            border-radius: 25px;
            border: 6px solid #bfa2ff;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        .logo {
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: #5e17eb;
        }
        .greeting {
            text-align: center;
            font-size: 16px;
            margin-bottom: 25px;
        }
        .field-label {
            margin-top: 10px;
            font-size: 14px;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# Simulate login state
if "signed_in" not in st.session_state:
    st.session_state.signed_in = False

# Render everything inside a container
with st.container():
    st.markdown('<div class="mobile-wrapper">', unsafe_allow_html=True)

    # Logo and greeting
    st.markdown('<div class="logo">WELLS FARGO</div>', unsafe_allow_html=True)
    st.markdown('<div class="greeting">Good morning 👋</div>', unsafe_allow_html=True)

    if not st.session_state.signed_in:
        # Input fields and login button
        st.markdown('<div class="field-label">Username</div>', unsafe_allow_html=True)
        username = st.text_input("", key="username_input")

        st.markdown('<div class="field-label">Password</div>', unsafe_allow_html=True)
        password = st.text_input("", type="password", key="password_input")

        if st.button("Sign On", use_container_width=True):
            if username.strip() and password.strip():
                st.session_state.signed_in = True
            else:
                st.warning("Please enter both username and password.")
    else:
        st.success("✅ Signed in successfully!")
        st.markdown("### Dashboard")
        st.metric("Balance", "$5,200")
        st.metric("Transactions", "7 this week")

        if st.button("Logout", use_container_width=True):
            st.session_state.signed_in = False

    st.markdown('</div>', unsafe_allow_html=True)
