import streamlit as st
import requests

def register_page():
    with st.container():
        st.markdown("""
        <div class="login-container">
            <h1>Register to Colorlib</h1>
            <p>Create your account to get full access.</p>
            <form id="register-form">
                <label for="first_name">First Name</label>
                <input type="text" id="first_name" name="first_name" placeholder="John" required>
                <label for="last_name">Last Name</label>
                <input type="text" id="last_name" name="last_name" placeholder="Doe" required>
                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="your-email@example.com" required>
                <label for="phone">Phone</label>
                <input type="tel" id="phone" name="phone" placeholder="+1234567890" required>
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Your Password" required>
                <label for="confirm_password">Confirm Password</label>
                <input type="password" id="confirm_password" name="confirm_password" placeholder="Confirm Your Password" required>
                <div class="button-group">
                    <button type="submit" class="register-btn">Register</button>
                    <button type="button" class="login-btn" id="login-btn">Login</button>
                </div>
            </form>
        </div>
        """, unsafe_allow_html=True)

    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False

    if st.session_state.form_submitted:
        register_data = {
            "first_name": st.session_state.first_name,
            "last_name": st.session_state.last_name,
            "email": st.session_state.email,
            "phone": st.session_state.phone,
            "password": st.session_state.password
        }
        response = requests.post("https://f9global.app.n8n.cloud/webhook/user-registration", json=register_data)
        if response.status_code == 200:
            st.success("Registration successful! Please check your email for verification.")
            st.session_state.show_success = True
            st.session_state.page = "login"
            st.experimental_rerun()
        else:
            st.error("Registration failed. Please try again.")
        
        st.session_state.form_submitted = False

    if st.session_state.get('page') == 'login':
        st.experimental_rerun()

    st.markdown("""
    <script>
    const form = document.getElementById('register-form');
    const loginBtn = document.getElementById('login-btn');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const first_name = document.getElementById('first_name').value;
        const last_name = document.getElementById('last_name').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const password = document.getElementById('password').value;
        const confirm_password = document.getElementById('confirm_password').value;

        if (password !== confirm_password) {
            alert("Passwords do not match!");
            return;
        }

        window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'first_name', value: first_name}, '*');
        window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'last_name', value: last_name}, '*');
        window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'email', value: email}, '*');
        window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'phone', value: phone}, '*');
        window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'password', value: password}, '*');
        window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'form_submitted', value: true}, '*');
    });

    loginBtn.addEventListener('click', () => {
        window.parent.postMessage({type: 'streamlit:setSessionState', key: 'page', value: 'login'}, '*');
    });
    </script>
    """, unsafe_allow_html=True)