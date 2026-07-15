import streamlit as st #匯入streamlit模組並重新命名為st
#st.number_input()可以讓使用者輸入數字,設定step=1可以讓使用者只輸入整數
#min_value=0可以設定最小值為0,max_value=100可以設定最大值為100
number=st.number_input("請輸入一個數字:",step=1, min_value=0,max_value=100)
#st.markdown()可在網頁使用markdown語法顯示文字
st.markdown(f"你輸入的數字是:{number}")

st.markdown(" ")
st.markdown("### 練習")

number=st.number_input("請輸入你的分數:",step=1,min_value=0,max_value=100)

if number<=59:
    st.write("F")
elif 60<=number<=69:
    st.write("D")
elif 70<=number<=79:
    st.write("C")
elif 80<=number<=89:
    st.write("B")
elif 90<=number:
    st.write("A")

st.button("按我一下",key="button1")
if st.button("按我一下",key="balloons"):
    st.balloons()
if st.button("按我一下",key="snow"):
    st.snow()
st.markdown("---")
