import streamlit as st
from user_management import check_credentials, register_user

def login_register_page():
    st.title("Login or Register")
    
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = "Login"

    if 'registration_success' not in st.session_state:
        st.session_state.registration_success = False

    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        with st.form("login_form"):
            login_email = st.text_input("Email", key="login_email")
            login_password = st.text_input("Password", type="password", key="login_password")
            col1, col2 = st.columns([1, 3])
            with col1:
                remember_me = st.checkbox("Remember me")
            login_submit = st.form_submit_button("Login")

            if login_submit:
                if check_credentials(login_email, login_password):
                    st.success("Logged in successfully!")
                    if remember_me:
                        st.session_state.remember_email = login_email
                    return True
                else:
                    st.error("Invalid email or password")
    
    with tab2:
        if st.session_state.registration_success:
            st.success("Registration successful!")
            if st.button("Please login now"):
                st.session_state.active_tab = "Login"
                st.rerun()
        else:
            with st.form("register_form"):
                first_name = st.text_input("First Name")
                last_name = st.text_input("Last Name")
                phone = st.text_input("Phone Number")
                email = st.text_input("Email Address")
                password = st.text_input("Choose a password", type="password")
                register_submit = st.form_submit_button("Register")

                if register_submit:
                    if register_user(password, first_name, last_name, phone, email):
                        st.session_state.registration_success = True
                        st.rerun()
                    else:
                        st.error("Registration failed. Email may already be registered or there was an error with the registration service.")
    
    # Force the correct tab to be active
    if st.session_state.active_tab == "Login":
        tab1.empty()
        tab1.checkbox("Login Tab", value=True, key="login_tab", label_visibility="hidden")
    else:
        tab2.empty()
        tab2.checkbox("Register Tab", value=True, key="register_tab", label_visibility="hidden")

    return False

def main_page():
    st.title("Welcome to the Main Page")
    st.write("This is the content of your main application.")

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if 'remember_email' not in st.session_state:
        st.session_state.remember_email = ""

    if not st.session_state.logged_in:
        st.session_state.logged_in = login_register_page()
    else:
        main_page()

if __name__ == "__main__":
    main()