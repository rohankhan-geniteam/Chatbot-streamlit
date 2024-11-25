import streamlit as st

def display_message():
    if st.session_state.selected_chat is not None:
        chat = st.session_state.chat_history[st.session_state.selected_chat]
        for idx, (q, a) in enumerate(chat):
            message_color = "background-color: #E1E1E1;" if idx % 2 == 0 else "background-color: #F0F0F0;"
            st.markdown(f"""
                <div style="padding: 10px; border-radius: 8px; {message_color} margin-bottom: 15px;">
                    <strong>You:</strong> {q}
                </div>
                <div style="padding: 10px; border-radius: 8px; background-color: #007BFF; color: white; margin-bottom: 15px;">
                    <strong>Bot:</strong> {a}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Start a new chat by typing a message below.")
