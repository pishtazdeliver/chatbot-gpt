import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

client = openai.OpenAI()

# باقی کد مثل قبل
# هنگام ارسال پیام:
client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=st.session_state.messages
)

reply = response.choices[0].message.content
