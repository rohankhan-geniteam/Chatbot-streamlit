import streamlit as st

def initialize_session_state():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'current_response' not in st.session_state:
        st.session_state.current_response = ""
    if 'input_counter' not in st.session_state:
        st.session_state.input_counter = 0
    if 'selected_chat' not in st.session_state:
        st.session_state.selected_chat = None
    if 'is_loading' not in st.session_state:
        st.session_state.is_loading = False
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
