import streamlit as st
import time

if st.button("重新整理", key="button1"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理整個頁面

st.title("點餐機")

if "a" not in st.session_state:
    st.session_state.a = [] 



col1,col2=st.columns([4,1])
with col1:
    b=st.text_input("請輸入餐點")
    
    
with col2:
    if st.button("加入",key="button2"):
        st.session_state.a.append(b)

st.title("購物籃")


for a in st.session_state.a:
    st.write(a)



 