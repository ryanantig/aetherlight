import streamlit as st
import requests
import json

def login_page():
    with st.container():
        st.markdown("""
        <div class="login-container">
            <h1>Login to Adhub XD</h1>
            <p>Welcome back! Please login to your account.</p>
            <form id="login-form">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="your-email@example.com" required>
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Your Password" required>
                <div class="remember-forgot">
                    <label><input type="checkbox"> Remember me</label>
                    <a href="#" class="forgot-password">Forgot Password</a>
                </div>
                <div class="button-group">
                    <button type="submit" class="login-btn">Log In</button>
                    <button type="button" class="register-btn" id="register-btn">Register</button>
                </div>
            </form>
        </div>
        """, unsafe_allow_html=True)

    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False

    if st.session_state.form_submitted:
        email = st.session_state.email
        password = st.session_state.password
        login_data = {"email": email, "password": password}
        try:
            response = requests.post("https://f9global.app.n8n.cloud/webhook/user-login", json=login_data)
            response.raise_for_status()
            
            user_data = response.json()
            
            if isinstance(user_data, list) and len(user_data) > 0:
                user_data = user_data[0]
            
            if user_data.get('status') == 'success':
                st.session_state.user_first_name = user_data.get('First Name', '')
                st.session_state.user_last_name = user_data.get('Last Name', '')
                st.session_state.logged_in = True
                st.session_state.page = 'dashboard'
                st.experimental_rerun()
            else:
                st.error("Login failed. Please check your credentials.")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {str(e)}")
        except json.JSONDecodeError:
            st.error("Error decoding the server response. Please try again later.")
        
        st.session_state.form_submitted = False

    if st.session_state.get('page') == 'register':
        st.experimental_rerun()

    st.markdown("""
    <script>
    const form = document.getElementById('login-form');
    const registerBtn = document.getElementById('register-btn');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'email', value: email}, '*');
        window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'password', value: password}, '*');
        window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'form_submitted', value: true}, '*');
    });

    registerBtn.addEventListener('click', () => {
        window.parent.postMessage({type: 'streamlit:setSessionState', key: 'page', value: 'register'}, '*');
    });
    </script>
    """, unsafe_allow_html=True)