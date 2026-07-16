import streamlit as st
import random

# --- 1. 網頁標題與介紹 ---
st.title("🎈 猜數字遊戲")
st.write("這是一個 1 到 100 的猜數字遊戲。請在下方輸入你猜的數字！")

# --- 2. 初始化遊戲狀態 (利用 session_state 記住這一局的資料) ---
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)  # 隨機生成 1~100 的答案
    st.session_state.min_val = 1                      # 目前範圍最小值
    st.session_state.max_val = 100                    # 目前範圍最大值
    st.session_state.game_over = False                # 記錄這局是否結束了

# --- 3. 顯示目前的猜測範圍 ---
st.subheader(f"目前範圍： {st.session_state.min_val} ~ {st.session_state.max_val}")

# --- 4. 遊戲主要邏輯 ---
if not st.session_state.game_over:
    # 讓使用者輸入數字，限制範圍在 1 ~ 100 之間
    guess = st.number_input(
        "請輸入你猜的數字：", 
        min_value=1, 
        max_value=100, 
        value=st.session_state.min_val,
        step=1
    )

    # 提交按鈕
    if st.button("我猜！", key="guess_btn"):
        # 檢查輸入的數字是否在當前的有效範圍內
        if guess < st.session_state.min_val or guess > st.session_state.max_val:
            st.warning(f"請輸入當前範圍內 ({st.session_state.min_val} ~ {st.session_state.max_val}) 的數字喔！")
        
        elif guess < st.session_state.answer:
            st.error("太小了！再試試看。")
            # 更新範圍：最小值變成 guess + 1
            if guess >= st.session_state.min_val:
                st.session_state.min_val = guess + 1
            st.rerun() # 重新整理頁面以更新畫面上的範圍

        elif guess > st.session_state.answer:
            st.error("太大了！再試試看。")
            # 更新範圍：最大值變成 guess - 1
            if guess <= st.session_state.max_val:
                st.session_state.max_val = guess - 1
            st.rerun() # 重新整理頁面以更新畫面上的範圍

        else:
            # 猜中了！
            st.success(f"恭喜你！猜對了！答案就是 {st.session_state.answer} 🎉")
            st.balloons()  # 噴出氣球特效！
            st.session_state.game_over = True
else:
    st.info(f"遊戲已結束！答案是 {st.session_state.answer}。")