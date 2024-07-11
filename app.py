import streamlit as st
import streamlit.components.v1 as components
from user_management import check_credentials, register_user

def load_css():
    with open("style.css") as f:
        return f'<style>{f.read()}</style>'

# ... (previous code remains the same)

def login_register_page():
    css = load_css()
    
    login_html = f"""
    {css}
    <div class="login-container">
        <div class="login-box">
            <div class="login-form">
                <h3>Login</h3>
                <form id="login-form">
                    <input type="email" id="email" placeholder="Email" required>
                    <input type="password" id="password" placeholder="Password" required>
                    <div class="remember-me">
                        <input type="checkbox" id="remember-me">
                        <label for="remember-me">Remember me</label>
                    </div>
                    <div class="forgot-password"><a href="#">Forgot Password?</a></div>
                    <button type="submit">Login</button>
                </form>
                <p class="register-link">Don't have an account? <a href="#" onclick="showRegister()">Register here</a></p>
            </div>
            <div class="image-container"></div>
        </div>
    </div>
    <script>
    // ... (JavaScript remains the same)
    </script>
    """
    
    components.html(login_html, height=900)
    
    # Handle messages from JavaScript
    if st.session_state.get('js_message'):
        message = st.session_state.js_message
        if message['action'] == 'login':
            if check_credentials(message['email'], message['password']):
                st.success("Logged in successfully!")
                if message['remember']:
                    st.session_state.remember_email = message['email']
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid email or password")
        elif message['action'] == 'show_register':
            st.session_state.show_register = True
            st.rerun()
        
        st.session_state.js_message = None

    # Registration form
    if st.session_state.get('show_register', False):
        with st.form("register_form"):
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            phone = st.text_input("Phone Number")
            email = st.text_input("Email Address")
            password = st.text_input("Choose a password", type="password")
            register_submit = st.form_submit_button("Register")

            if register_submit:
                if register_user(password, first_name, last_name, phone, email):
                    st.success("Registration successful! Please login now.")
                    st.session_state.show_register = False
                    st.rerun()
                else:
                    st.error("Registration failed. Email may already be registered or there was an error with the registration service.")

def main_page():
    st.title("Welcome to the Main Page")
    st.write("This is the content of your main application.")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Handle messages from JavaScript
    components.html(
        """
        <script>
        window.addEventListener('message', function(e) {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: e.data}, '*');
        });
        </script>
        """,
        height=0,
    )

    if not st.session_state.logged_in:
        login_register_page()
    else:
        main_page()

if __name__ == "__main__":
    main()