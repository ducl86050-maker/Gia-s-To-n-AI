import streamlit as st
import google.generativeai as genai

st.title("🤖 Chào mừng em đến với gia sư Toán Soleil!! (⁀ᗢ⁀) ")

# Kiểm tra Secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # Dòng này phải nằm sát lề trái, thẳng hàng với dòng if
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    st.error("Chưa cấu hình API Key trong Secrets!")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("hãy để chị giải quyết thắc mắc của em nhé! (´｡• ω •｡`) ♡"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Lỗi: {e}")