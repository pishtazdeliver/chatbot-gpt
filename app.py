import streamlit as st
import openai

st.set_page_config(page_title="🤖 چت‌بات هوش مصنوعی", page_icon="🤖")

openai.api_key = st.secrets["OPENAI_API_KEY"]

# مرحله ورود: فقط یک بار اجرا شود
if "username" not in st.session_state:
    st.session_state.username = None

if st.session_state.username is None:
    with st.form("user_form", clear_on_submit=True):
        st.markdown("### 👤 لطفاً نام خود را وارد کنید")
        username = st.text_input("نام شما:")
        submitted = st.form_submit_button("شروع گفت‌و‌گو")
        if submitted and username:
            st.session_state.username = username

    st.stop()  # منتظر می‌مانیم تا فرم کامل شود

# چت اصلی
st.title(f"🤖 چت‌بات هوش مصنوعی | {st.session_state.username} عزیز، خوش آمدی!")
st.markdown("با من حرف بزن!")

# پیام‌ها
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": f"تو یک دستیار فارسی‌زبان هستی. نام کاربر: {st.session_state.username}"}
    ]

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# چت ورودی
prompt = st.chat_input("متن خود را وارد کنید...")

if prompt:
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
