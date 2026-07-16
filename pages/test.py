import streamlit as st
import time

if st.button("重新整理", key="button1"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理整個頁面

st.title("點餐機")

if "a" not in st.session_state:
    st.session_state.a = [] 



col1,col2=st.columns(2)
with col1:
    b=st.text_input("請輸入餐點")
    
    
with col2:
    st.write("##")
    if st.button("加入",key="button2"):
        st.session_state.a.append(b)
        st.rerun()
st.title("購物籃")

for idx, item in enumerate(st.session_state.a):
    item_col, del_col = st.columns([4, 1])
    with item_col:
        st.write(f"{item}")

    with del_col:
        if st.button("刪除", key=f"button3-{idx}"):
            st.session_state.a.pop(idx)
        

            st.rerun()


 