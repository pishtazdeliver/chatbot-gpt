import streamlit as st
import openai

st.set_page_config(page_title="🤖 چت‌بات هوش مصنوعی")

st.title("🤖 چت‌بات هوش مصنوعی")
st.markdown("با من حرف بزن!")

# قرار دادن کلید API
openai.api_key = "کلید API خودت را اینجا بگذار"

# ذخیره تاریخچه گفتگو
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "تو یک دستیار فارسی‌زبان هستی و به صورت دوستانه پاسخ می‌دهی."}
    ]

# نمایش تاریخچه گفتگو در صفحه
for msg in st.session_state.messages[1:]:  # اولی system است، نمایش نده
    st.chat_message(msg["role"]).markdown(msg["content"])

# وقتی کاربر پیامی می‌فرستد
if prompt := st.chat_input("متن خود را وارد کنید..."):
    # اضافه کردن پیام کاربر به تاریخچه
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # ارسال پیام به OpenAI
    with st.spinner("در حال پاسخ دادن..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message["content"]

    # نمایش و ذخیره پاسخ
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
