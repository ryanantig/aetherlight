import streamlit as st

def dashboard_page():
    with st.container():
        st.markdown(f"""
        <div class="dashboard-container">
            <h1 class="welcome-title">Welcome, {st.session_state.user_first_name} {st.session_state.user_last_name}!</h1>
            <p class="dashboard-subtitle">This is your personalized dashboard.</p>
            <div class="dashboard-content">
                <p>Here you can add various widgets, charts, and information for the user.</p>
            </div>
            <button class="logout-btn" id="logout-btn">Logout</button>
        </div>
        """, unsafe_allow_html=True)

    if 'logout_clicked' not in st.session_state:
        st.session_state.logout_clicked = False

    if st.session_state.logout_clicked:
        st.session_state.logged_in = False
        st.session_state.user_first_name = None
        st.session_state.user_last_name = None
        st.session_state.page = "login"
        st.session_state.logout_clicked = False
        st.experimental_rerun()

    st.markdown("""
    <script>
    const logoutBtn = document.getElementById('logout-btn');

    logoutBtn.addEventListener('click', () => {
        window.parent.postMessage({type: 'streamlit:setComponentValue', key: 'logout_clicked', value: true}, '*');
    });
    </script>
    """, unsafe_allow_html=True)