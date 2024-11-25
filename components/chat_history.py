import streamlit as st

def display_chat_history():
    with st.sidebar:
        st.header("💬 Chat History")
        st.markdown("---")

        if st.session_state.chat_history:
            with st.expander("Select a previous chat", expanded=True):
                for idx, chat in enumerate(st.session_state.chat_history):
                    if st.button(f"Chat {idx + 1}", key=f"chat_button_{idx}"):
                        st.session_state.selected_chat = idx

        if st.session_state.selected_chat is not None:
            st.markdown(f"### Selected Chat {st.session_state.selected_chat + 1}")
            chat = st.session_state.chat_history[st.session_state.selected_chat]
            for q, a in chat:
                st.write(f"**You**: {q}")
                st.write(f"**Bot**: {a}")
        else:
            st.info("Select or start a new chat to see history.")
