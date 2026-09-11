import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="AI Chatbot with Memory", page_icon="🤖")
st.title("🤖 Custom AI Chatbot with Memory ")
st.markdown("    developed by: ANNUM NISAR    ")


api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if not api_key:
    st.info("Please enter your Gemini API Key in the sidebar to start.", icon="🔑")
    st.stop()


client = genai.Client(api_key=api_key)


if "messages" not in st.session_state:
    st.session_state.messages = []


MAX_HISTORY = 10  


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_prompt := st.chat_input("Type your message here..."):
    
    if not user_prompt.strip():
        st.warning("Please type a valid message.")
        st.stop()

    
    with st.chat_message("user"):
        st.markdown(user_prompt)

    
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    
    if len(st.session_state.messages) > MAX_HISTORY:
        st.session_state.messages = st.session_state.messages[-MAX_HISTORY:]

    
    formatted_contents = [
        types.Content(
            role=msg["role"],
            parts=[types.Part.from_text(text=msg["content"])]
        )
        for msg in st.session_state.messages
    ]

    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=formatted_contents
                )
                bot_reply = response.text
                st.markdown(bot_reply)

                
                st.session_state.messages.append({"role": "model", "content": bot_reply})
            except Exception as e:
                st.error(f"Error: {e}")