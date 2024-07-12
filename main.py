import streamlit as st
from login import login_page
from register import register_page
from dashboard import dashboard_page
from utils import load_css

def main():
    load_css()

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if 'page' not in st.session_state:
        st.session_state.page = 'login'

    if st.session_state.logged_in:
        dashboard_page()
    elif st.session_state.page == 'login':
        login_page()
    elif st.session_state.page == 'register':
        register_page()

if __name__ == "__main__":
    main()