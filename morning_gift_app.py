# morning_gift_app.py
import streamlit as st
import time

st.set_page_config(page_title="Món quà buổi sáng", page_icon="🎁", layout="centered")

# --- trạng thái ---
if "opened" not in st.session_state:
    st.session_state.opened = False
if "typed" not in st.session_state:
    st.session_state.typed = False

# --- giao diện chính ---
st.markdown("<h1 style='text-align:center; color:#d35400;'>🎁 Món quà buổi sáng 🎁</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Nhấn nút bên dưới để mở quà</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if not st.session_state.opened:
        if st.button("Mở quà 🎁", key="open_button"):
            st.session_state.opened = True
            st.session_state.typed = False
            st.rerun()

    else:
        st.markdown("<h3 style='text-align:center; color:#2c3e50;'>Chúc bà buổi sáng vui vẻ 🌞</h3>", unsafe_allow_html=True)
        # vùng typing
        placeholder = st.empty()

        # văn bản sẽ typing
        text = (
            "Chúc bà buổi sáng vui vẻ,\n"
            "nhớ cười lên nha vì mở đầu ngày mới\n"
            "không thể thiếu sự rực rỡ của mặt trời được."
        )

        # nếu chưa typing lần nào thì hiển thị từng ký tự
        if not st.session_state.typed:
            shown = ""
            # gõ từng ký tự chậm để giống hiệu ứng typing
            for ch in text:
                shown += ch
                # dùng HTML để canh giữa & chỉnh cỡ chữ
                placeholder.markdown(f"<div style='font-size:18px; text-align:center; color:#222;'>{shown.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
                time.sleep(0.06)  # tốc độ: 0.06s/ký tự → bạn chỉnh nhỏ hơn để nhanh hơn
            st.session_state.typed = True
        else:
            # nếu đã typing rồi (refresh) thì hiện nguyên đoạn luôn
            placeholder.markdown(f"<div style='font-size:18px; text-align:center; color:#222;'>{text.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)

        # thêm nút để đóng lại (quay về màn 1)
        def reset():
            st.session_state.opened = False
            st.session_state.typed = False
            st.rerun()


        st.markdown("<div style='text-align:center; margin-top:12px;'><button style='padding:6px 12px;'>Đóng lại</button></div>", unsafe_allow_html=True)
        # Cách an toàn để reset dùng Streamlit button (hiện dưới)
        if st.button("Đóng lại"):
            reset()
