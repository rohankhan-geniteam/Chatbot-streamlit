import streamlit as st
from components.chat_history import display_chat_history
from components.message_display import display_message
from utils.state import initialize_session_state
from utils.api import get_chatbot_response

def chat_interface():
    # Set the title of the web page (tab title)
    st.set_page_config(page_title="Chatbot")
    
    initialize_session_state()
    display_chat_history()
    st.title("🤖 Chatbot")
    st.markdown("Type your message below and get an instant response!")

    chat_window = st.container()
    with chat_window:
        display_message()

    st.markdown("---")
    col1, col2 = st.columns([4, 1])

    with col1:
        st.session_state.user_input = st.text_input(
            "Type your message here:",
            st.session_state.user_input,
            key="chat_input",
            placeholder="Type your message and press Send...",
        )

    with col2:
        st.markdown("""<style>.stButton { margin-top: 12px; color: black; }</style>""", unsafe_allow_html=True)

        if st.button("Send", key="send_button", use_container_width=False):
            if st.session_state.user_input.strip():
                st.session_state.is_loading = True
                bot_response = get_chatbot_response(st.session_state.user_input)
                st.session_state.is_loading = False

                if st.session_state.selected_chat is None:
                    st.session_state.chat_history.append([])
                    st.session_state.selected_chat = len(st.session_state.chat_history) - 1
                st.session_state.chat_history[st.session_state.selected_chat].append(
                    (st.session_state.user_input, bot_response)
                )
                st.rerun()

                st.session_state.user_input.replace("")

                st.session_state.input_counter += 1

    if st.session_state.is_loading:
        with st.spinner("🤖 Bot is thinking..."):
            pass
