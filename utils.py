import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f5;
    }
    .login-container, .dashboard-container {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
        max-width: 800px;
        margin: 2rem auto;
    }
    .login-container h1, .dashboard-container h1 {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 0.5rem;
        color: #2c3e50;
    }
    .login-container p, .dashboard-container p {
        color: #7f8c8d;
        margin-bottom: 1.5rem;
    }
    .login-container form {
        display: flex;
        flex-direction: column;
    }
    .login-container label {
        margin-bottom: 0.5rem;
        color: #34495e;
    }
    .login-container input {
        margin-bottom: 1rem;
        padding: 0.5rem;
        border: 1px solid #bdc3c7;
        border-radius: 4px;
    }
    .remember-forgot {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    .forgot-password {
        color: #3498db;
        text-decoration: none;
    }
    .button-group {
        display: flex;
        flex-direction: row;
        gap: 0.5rem;
    }
    .button-group button, .logout-btn {
        flex: 1;
        background-color: #2c3e50;
        color: white;
        border: none;
        padding: 0.5rem;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s;
        font-size: 14px;
        height: 40px;
        line-height: 20px;
    }
    .button-group button:hover, .logout-btn:hover {
        background-color: #34495e;
    }
    .register-btn {
        background-color: #3498db !important;
    }
    .register-btn:hover {
        background-color: #2980b9 !important;
    }
    .welcome-title {
        font-size: 28px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .dashboard-subtitle {
        font-size: 18px;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
    .dashboard-content {
        margin-bottom: 2rem;
    }
    .logout-btn {
        background-color: #e74c3c !important;
    }
    .logout-btn:hover {
        background-color: #c0392b !important;
    }
    </style>
    """, unsafe_allow_html=True)