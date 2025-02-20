import streamlit as st
import requests

# Base API URL
API_URL = "http://127.0.0.1:8000"

# 🚀 Initialize Streamlit App
st.title("💬 Assistant Chatbot Interface")
st.sidebar.header("🔧 Chatbot Settings")

# ✅ User Initialization Section
st.sidebar.subheader("👤 Initialize User")
user_id = st.sidebar.text_input("User ID", value="user123")
user_name = st.sidebar.text_input("User Name", value="John Doe")

if st.sidebar.button("Initialize User"):
    payload = {"user_id": user_id, "user_name": user_name}
    response = requests.post(f"{API_URL}/initialize_user/", json=payload)
    
    if response.status_code == 200:
        st.sidebar.success(response.json()["message"])
    else:
        st.sidebar.error(f"Error: {response.json()}")

# ✅ Set User Language
st.sidebar.subheader("🌍 Set Language")
language_options = {
    "English": "en",
    "Hindi": "hi",
    "Gujarati": "gu",
    "Tamil": "ta",
    "Telugu": "te",
    "Bengali": "bn"
}
selected_language = st.sidebar.selectbox("Choose Language", list(language_options.keys()))

if st.sidebar.button("Set Language"):
    payload = {"user_id": user_id, "language": language_options[selected_language]}
    response = requests.post(f"{API_URL}/set_language/", json=payload)

    if response.status_code == 200:
        st.sidebar.success(f"Language set to {selected_language}")
    else:
        st.sidebar.error(f"Error: {response.json()}")

# ✅ Query Knowledge Base
st.subheader("🧠 Ask a Question to Knowledge Base")
query_text = st.text_area("Enter your query")

if st.button("🔍 Get Knowledge Response"):
    if query_text.strip():
        payload = {"user_id": user_id, "query_text": query_text}
        response = requests.post(f"{API_URL}/query_knowledge/", json=payload)

        if response.status_code == 200:
            knowledge_response = response.json()["response"]
            st.success(f"**Knowledge Base Response:**\n{knowledge_response}")
        else:
            st.error(f"Error: {response.json()}")
    else:
        st.warning("⚠️ Please enter a valid query!")

# ✅ Generate LLM Response
st.subheader("🤖 Get AI-generated Response")
prompt_text = st.text_area("Enter a prompt for LLM")

if st.button("⚡ Generate AI Response"):
    if prompt_text.strip():
        payload = {"user_id": user_id, "prompt": prompt_text}
        response = requests.post(f"{API_URL}/generate_llm_response/", json=payload)

        if response.status_code == 200:
            llm_response = response.json()["generated_text"]
            st.success(f"**LLM Response:**\n{llm_response}")
        else:
            st.error(f"Error: {response.json()}")
    else:
        st.warning("⚠️ Please enter a valid prompt!")

# ✅ Retrieve User History
st.subheader("📜 View Chat History")

if st.button("📂 Load Chat History"):
    response = requests.get(f"{API_URL}/get_user_history/{user_id}")

    if response.status_code == 200:
        chat_history = response.json()["history"]
        if chat_history:
            for item in chat_history:
                st.info(f"🕒 {item['timestamp']}\n**User:** {item['query']}\n**Bot:** {item['response']}")
        else:
            st.warning("⚠️ No history available.")
    else:
        st.error(f"Error: {response.json()}")

# ✅ Translate Text
st.subheader("🌍 Translate Text")
translate_text = st.text_area("Enter text to translate")
target_lang = st.selectbox("Select Target Language", list(language_options.keys()))

if st.button("🌎 Translate"):
    if translate_text.strip():
        payload = {"text": translate_text, "target_language": language_options[target_lang]}
        response = requests.post(f"{API_URL}/translate_text/", json=payload)

        if response.status_code == 200:
            translated_text = response.json()["translated_text"]
            st.success(f"**Translated Text:**\n{translated_text}")
        else:
            st.error(f"Error: {response.json()}")
    else:
        st.warning("⚠️ Please enter some text to translate!")
