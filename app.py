import streamlit as st
import openai

st.set_page_config(page_title="🤖 چت‌بات هوش مصنوعی")
st.title("🤖 چت‌بات هوش مصنوعی")
st.markdown("با من حرف بزن!")

# دریافت API Key از تنظیمات محرمانه Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ذخیره تاریخچه گفتگو
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "تو یک دستیار فارسی‌زبان هستی و به صورت دوستانه پاسخ می‌دهی."}
    ]

# نمایش گفتگوهای قبلی
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# پاسخ به ورودی کاربر
if prompt := st.chat_input("متن خود را وارد کنید..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.spinner("در حال پاسخ دادن..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message["content"]

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
