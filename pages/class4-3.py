import streamlit as st
import os

# 1. 初始化商品數據（使用 st.session_state 保持點擊按鈕時的數據狀態）
if 'inventory' not in st.session_state:
    st.session_state.inventory = {
        'Apple': 10,
        'Banana': 10,
        'BG': 10,
        'Orange': 10
    }

# 2. 標題與動態欄位輸入（放最上面）
st.title("購物平台")

# 欄位數輸入（預設為 4 欄，可自由調整）
num_columns = st.number_input("請輸入商品展示欄位數", min_value=1, max_value=4, value=4, step=1)

# 商品的基本資訊定義（圖片路徑已修改為指向 image 資料夾）
products = [
    {"id": "Apple", "name": "Apple", "image": "image/apple.png", "price": 10},
    {"id": "Banana", "name": "Banana", "image": "image/banana.png", "price": 10},
    {"id": "BG", "name": "BG", "image": "image/bg.png", "price": 10},
    {"id": "Orange", "name": "Orange", "image": "image/orange.png", "price": 10},
]

# 3. 商品展示區域（根據輸入的欄位數動態生成欄位，並置於欄位樹下面）
cols = st.columns(num_columns)

for index, prod in enumerate(products):
    # 使用餘數運算動態分配商品到對應的欄位中
    col_idx = index % num_columns
    with cols[col_idx]:
        # 顯示圖片
        if os.path.exists(prod["image"]):
            st.image(prod["image"], use_container_width=True)
        else:
            # 若找不到圖片則顯示灰底 placeholder
            st.warning(f"找不到 {prod['image']}")
            
        # 商品名字
        st.subheader(prod["name"])
        # 價格
        st.write(f"價格: ${prod['price']} 元")
        # 存貨
        current_stock = st.session_state.inventory[prod["id"]]
        st.write(f"存貨: {current_stock} 個")
        
        # 購買按鈕（量減少）
        if st.button(f"購買 {prod['name']}", key=f"buy_{prod['id']}"):
            if st.session_state.inventory[prod["id"]] > 0:
                st.session_state.inventory[prod["id"]] -= 1
                st.toast(f"成功購買 1 個 {prod['name']}！")
                st.rerun()  # 立即重新整理畫面更新庫存
            else:
                st.error(f"{prod['name']} 已經沒有存貨了！")

st.markdown("---")

# 4. 新增商品庫存（小標題）
st.subheader("新增商品庫存")

# 選擇商品和增加商品數量
add_prod_select = st.selectbox("選擇商品", options=[prod["name"] for prod in products])
add_quantity = st.number_input("請輸入要增加的數量", min_value=1, value=5, step=1)

# 增加商品（按鈕）
if st.button("增加商品"):
    st.session_state.inventory[add_prod_select] += add_quantity
    st.success(f"已成功為 {add_prod_select} 增加 {add_quantity} 個庫存！")
    st.rerun()

st.markdown("---")

# 5. 目前商品的數量（底部概覽列表）
st.subheader("目前商品的數量")
for key, val in st.session_state.inventory.items():
    st.write(f"• **{key}** 目前庫存數量: `{val}` 個")