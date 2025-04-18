import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title("🤖 Chatbot Interface")

# Sidebar controls
st.sidebar.title("🔧 Controls")
sidebar_input = st.sidebar.text_input("Enter the URL:")

if st.sidebar.button("Extract and Load"):
    try:
        sidebar_input_encoded = requests.utils.quote(sidebar_input)
        response = requests.get(f"http://localhost:8000/extract_vector_load?url={sidebar_input_encoded}")
        if response.status_code == 200:
            st.sidebar.success("Data loaded to vector DB successfully")
        else:
            st.sidebar.error("Failed to load the data")
    except Exception as e:
        st.sidebar.error(f"Error: {e}")

if st.sidebar.button("Clear Cache"):
    try:
        response = requests.post("http://localhost:8000/clear_cache")
        if response.status_code == 200:
            st.sidebar.success("Cache cleared!")
            st.session_state.messages = []
        else:
            st.sidebar.error("Failed to clear cache.")
    except Exception as e:
        st.sidebar.error(f"Error: {e}")

# Initialize chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input via chat input
if prompt := st.chat_input("Say something..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        prompt_encoded = requests.utils.quote(prompt)
        response = requests.post(f"http://localhost:8000/query_to_ask?q={prompt_encoded}")
        data = response.json()
        print(data)
        reply = data.get("response", "No reply")
        cached = data.get("cached", False)

        tag = "💡 *CACHED FROM REDIS*" if cached else "✅ *RESPONSE BY LLM*"
        with st.chat_message("assistant"):
            st.markdown(f"{reply}\n\n{tag}")

        st.session_state.messages.append({"role": "assistant", "content": f"{reply}\n\n{tag}"})
    except Exception as e:
        error_msg = f"Error: {e}"
        with st.chat_message("assistant"):
            st.markdown(error_msg)
        st.session_state.messages.append({"role": "assistant", "content": error_msg})
