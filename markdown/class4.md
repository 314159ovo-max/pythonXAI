# Python 筆記：字典（Dictionary，dict）

## 一、什麼是字典（dict）？

字典就像一本電話簿。

電話簿裡：

- **名字**可以找到**電話號碼**
- Python 的字典也是一樣，用 **Key（鍵）** 找到 **Value（值）**。

### 範例

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

代表：

| Key（鍵） | Value（值） |
| --------- | ----------- |
| a         | 1           |
| b         | 2           |
| c         | 3           |

---

# 二、字典的特色

✅ Key（鍵）

- 每個 Key 都不能重複。
- 可以是文字（string）、數字（int、float）等不能改變的資料。

✅ Value（值）

- 可以重複。
- 可以放任何資料，例如數字、文字、串列(list)、甚至另一個字典(dict)。

✅ 字典沒有順序

- 所以**不能用編號(index)**去拿資料。

例如：

```python
d[0]    # 錯誤！
```

要用 Key：

```python
d["a"]   # 1
```

---

# 三、取得所有 Key（鍵）

```python
print(d.keys())
```

結果：

```
dict_keys(['a', 'b', 'c'])
```

也可以一個一個印出來：

```python
for key in d.keys():
    print(key)
```

輸出：

```
a
b
c
```

---

# 四、取得所有 Value（值）

```python
print(d.values())
```

結果：

```
dict_values([1, 2, 3])
```

一個一個印：

```python
for value in d.values():
    print(value)
```

輸出：

```
1
2
3
```

---

# 五、同時取得 Key 和 Value

```python
print(d.items())
```

結果：

```
dict_items([('a',1),('b',2),('c',3)])
```

用迴圈：

```python
for key, value in d.items():
    print(key, value)
```

輸出：

```
a 1
b 2
c 3
```

---

# 六、新增資料

加入新的 Key 和 Value：

```python
d["d"] = 4
```

結果：

```python
{
    "a":1,
    "b":2,
    "c":3,
    "d":4
}
```

---

# 七、修改資料

如果 Key 已經存在，就會修改內容。

```python
d["a"] = 5
```

結果：

```python
{
    "a":5,
    "b":2,
    "c":3,
    "d":4
}
```

---

# 八、刪除資料（pop）

```python
d.pop("a")
```

會刪除：

```
a : 5
```

並回傳：

```
5
```

如果沒有這個 Key：

```python
d.pop("e", "Not found")
```

結果：

```
Not found
```

如果沒有預設值：

```python
d.pop("e")
```

程式會發生錯誤。

---

# 九、檢查 Key 是否存在

使用 **in**

```python
print("a" in d)
```

結果：

```
True
```

```python
print("e" in d)
```

結果：

```
False
```

📌 注意：

`in` 在字典只能檢查 **Key**，不能檢查 Value。

---

# 十、巢狀字典（字典裡放字典）

例如成績系統：

```python
grade = {
    "小明": {
        "國文":[90,80,70],
        "數學":[85,75,65],
        "英文":[95,85,75]
    }
}
```

就像一個大抽屜裡還有很多小抽屜。

---

## 取得某位同學的成績

取得小明數學成績：

```python
grade["小明"]["數學"]
```

結果：

```
[85,75,65]
```

---

取得第一次英文成績：

```python
grade["小美"]["英文"][0]
```

結果：

```
93
```

因為：

```
英文
↓
[93,83,73]
 ↑
第0個
```

---

取得第二次國文成績：

```python
grade["小華"]["國文"][1]
```

結果：

```
76
```

---

# 十一、計算平均成績

## 每位同學的國文平均

```python
avg = sum(chinese) / len(chinese)
```

意思：

```
總分 ÷ 次數 = 平均
```

例如：

```
90 + 80 + 70 = 240

240 ÷ 3 = 80
```

---

## 每位同學的總平均

先把所有科目的成績全部加起來：

```python
total += sum(scores)
```

最後：

```python
avg = total / (科目數 × 每科考試次數)
```

就能得到總平均。

---

# 十二、整理全校成績

建立一個新的字典：

```python
avg_grade = {
    "國文": [],
    "數學": [],
    "英文": []
}
```

把每位同學的成績都放進去：

```
國文
↓

[
90,80,70,
88,78,68,
86,76,66
]
```

之後就能算出：

- 全校國文平均
- 全校數學平均
- 全校英文平均

---

# 十三、取得字典有幾個 Key

使用：

```python
len(avg_grade)
```

結果：

```
3
```

因為有：

```
國文
數學
英文
```

共三個 Key。

---

# 十四、今天學到的重要函式

| 指令       | 功能                  |
| ---------- | --------------------- |
| `keys()`   | 取得所有 Key          |
| `values()` | 取得所有 Value        |
| `items()`  | 同時取得 Key 和 Value |
| `pop()`    | 刪除資料並回傳 Value  |
| `len()`    | 計算 Key 的數量       |
| `sum()`    | 加總所有數字          |
| `in`       | 檢查 Key 是否存在     |

---

# 十五、今天一定要記住的重點 ⭐

1. **字典是用 Key 找 Value。**
2. **字典不能用 index（編號）取資料。**
3. **新增和修改都是用 `dict[key] = value`。**
4. **`keys()` 可以取得所有 Key。**
5. **`values()` 可以取得所有 Value。**
6. **`items()` 可以同時取得 Key 和 Value。**
7. **`pop()` 可以刪除資料。**
8. **`in` 只能檢查 Key，不是 Value。**
9. **字典裡可以再放字典，形成巢狀結構。**
10. **`sum()` 和 `len()` 常常一起用來計算平均數。**

---

# 小挑戰

假設：

```python
fruit = {
    "蘋果": 30,
    "香蕉": 25,
    "葡萄": 80
}
```

請試著完成：

1. 印出所有水果名稱。
2. 印出所有價格。
3. 新增 `"橘子": 40`。
4. 修改 `"香蕉"` 的價格為 35。
5. 刪除 `"葡萄"`。
6. 檢查 `"蘋果"` 是否存在。
7. 印出目前共有幾種水果。

---

# 🌟 Python + Streamlit 圖片與購物平台筆記

## 一、什麼是 Streamlit？

**Streamlit** 是一個可以快速做出網頁介面的 Python 工具。

只要寫 Python，就可以做出有：

- 🖼️ 圖片
- 🔘 按鈕
- 📝 輸入框
- 📋 選單
- 📢 訊息

等功能。

程式一開始會先匯入需要的工具：

```python
import streamlit as st
import os
```

### ✨ 指令說明

### `import streamlit as st`

把 Streamlit 載入進來，以後都可以用 **st** 來呼叫它。

例如：

```python
st.title("我的網頁")
```

---

### `import os`

載入 **os**（作業系統工具）。

可以幫助我們：

- 找資料夾
- 找檔案
- 檢查檔案有沒有存在

---

# 二、顯示標題

```python
st.title("圖片元件")
```

### 功能

在網頁最上面顯示一個大標題。

例如：

```
圖片元件
```

---

# 三、顯示圖片

```python
st.image("image/apple.png", width=300)
```

### 功能

把圖片放到網頁上。

### 參數

- `"image/apple.png"` → 圖片位置
- `width=300` → 圖片寬度 300 像素

---

# 四、取得資料夾內所有圖片

```python
image_folder = "image"
```

把資料夾名稱存起來。

例如：

```
image
```

---

```python
image_files = os.listdir(image_folder)
```

### 功能

把資料夾裡所有檔案找出來。

例如：

```
apple.png
banana.png
orange.png
bg.png
```

---

```python
st.write(image_files)
```

### 功能

把內容顯示在網頁。

---

# 五、數字輸入框

```python
st.number_input(...)
```

例如：

```python
image_size = st.number_input(
    "圖片大小",
    min_value=50,
    max_value=500,
    step=50,
    value=100
)
```

### 功能

讓使用者輸入數字。

### 參數

- `min_value`：最小值
- `max_value`：最大值
- `step`：每次增加多少
- `value`：預設值

---

# 六、for 迴圈

```python
for image_file in image_files:
```

### 功能

把清單裡每個東西都做一次。

例如：

```
apple.png
banana.png
orange.png
bg.png
```

程式就會跑四次。

---

# 七、依照輸入大小顯示圖片

```python
st.image(
    f"{image_folder}/{image_file}",
    width=image_size
)
```

### 功能

每張圖片都用使用者輸入的大小顯示。

---

# 八、讓圖片自動填滿畫面

```python
st.image(
    "...",
    use_container_width=True
)
```

### 功能

圖片會自動調整成適合畫面的大小。

不用自己設定寬度。

---

# 九、成功訊息

```python
st.success("購買成功！")
```

### 功能

顯示綠色成功訊息。

例如：

✅ 購買成功！

---

# 十、session_state（記住資料）

```python
st.session_state
```

### 功能

幫程式記住資料。

例如：

商品剩幾個。

如果沒有它，每次按按鈕都會重新變回原本的數量。

---

初始化：

```python
if "inventory" not in st.session_state:
```

意思是：

如果第一次開啟程式，就建立庫存。

---

```python
st.session_state.inventory = {
    "Apple":10,
    "Banana":10
}
```

建立商品和數量。

例如：

```
Apple 10
Banana 10
Orange 10
```

---

# 十一、商品資料

```python
products = [
    {
        "id":"Apple",
        "name":"Apple",
        "image":"image/apple.png",
        "price":10
    }
]
```

每個商品都有：

- 商品代號
- 商品名稱
- 圖片
- 價格

---

# 十二、建立多欄版面

```python
cols = st.columns(num_columns)
```

### 功能

把畫面分成很多欄。

例如：

```
🍎   🍌   🍊   🥭
```

可以一排放很多商品。

---

# 十三、enumerate()

```python
for index, prod in enumerate(products):
```

### 功能

同時取得：

- 第幾個商品
- 商品資料

例如：

```
第0個 Apple
第1個 Banana
第2個 Orange
```

---

# 十四、餘數運算 %

```python
col_idx = index % num_columns
```

### 功能

決定商品要放在哪一欄。

例如：

4 欄時：

```
0→第1欄
1→第2欄
2→第3欄
3→第4欄
4→第1欄
```

這樣商品就會平均排列。

---

# 十五、檢查圖片是否存在

```python
os.path.exists(...)
```

### 功能

檢查圖片有沒有找到。

有：

顯示圖片。

沒有：

```python
st.warning(...)
```

跳出黃色提醒。

---

# 十六、小標題

```python
st.subheader("Apple")
```

### 功能

顯示比較小的標題。

---

# 十七、顯示文字

```python
st.write(...)
```

### 功能

在畫面上顯示文字。

例如：

```
價格：10 元
```

---

# 十八、按鈕

```python
st.button("購買")
```

### 功能

建立按鈕。

按下去會執行程式。

例如：

```
[購買]
```

---

# 十九、判斷式 if

```python
if ...
```

### 功能

如果條件成立，就執行。

例如：

```
如果還有庫存
    就購買
```

否則：

```
沒有庫存
```

---

# 二十、減少庫存

```python
st.session_state.inventory[...] -= 1
```

### 功能

商品數量減少 1。

例如：

```
10
↓
9
```

---

# 二十一、Toast 提醒

```python
st.toast(...)
```

### 功能

畫面角落跳出小提醒。

例如：

🎉 成功購買！

---

# 二十二、重新整理畫面

```python
st.rerun()
```

### 功能

重新執行整個程式。

畫面就會更新最新庫存。

---

# 二十三、錯誤訊息

```python
st.error(...)
```

### 功能

顯示紅色錯誤訊息。

例如：

❌ 商品已售完！

---

# 二十四、分隔線

```python
st.markdown("---")
```

### 功能

畫一條水平線，把畫面分成不同區域。

---

# 二十五、下拉選單

```python
st.selectbox(...)
```

### 功能

讓使用者選擇一個商品。

例如：

```
▼ Apple
```

---

# 二十六、增加庫存

```python
st.session_state.inventory[...] += add_quantity
```

### 功能

把商品數量增加。

例如：

```
10
+
5
=
15
```

---

# 二十七、顯示所有庫存

```python
for key, val in st.session_state.inventory.items():
```

### 功能

把每個商品和數量都顯示出來。

例如：

```
Apple：8 個
Banana：10 個
Orange：5 個
```

---

# 📚 今天學到的重要指令整理

| 指令                     | 功能                         |
| ------------------------ | ---------------------------- |
| `import streamlit as st` | 載入 Streamlit 工具          |
| `import os`              | 操作檔案與資料夾             |
| `st.title()`             | 顯示大標題                   |
| `st.subheader()`         | 顯示小標題                   |
| `st.write()`             | 顯示文字                     |
| `st.image()`             | 顯示圖片                     |
| `st.number_input()`      | 輸入數字                     |
| `st.selectbox()`         | 下拉式選單                   |
| `st.button()`            | 建立按鈕                     |
| `st.success()`           | 成功訊息                     |
| `st.warning()`           | 警告訊息                     |
| `st.error()`             | 錯誤訊息                     |
| `st.toast()`             | 跳出小提醒                   |
| `st.columns()`           | 建立多欄畫面                 |
| `st.markdown("---")`     | 分隔線                       |
| `st.rerun()`             | 重新整理畫面                 |
| `st.session_state`       | 記住資料（例如庫存）         |
| `os.listdir()`           | 取得資料夾內所有檔案         |
| `os.path.exists()`       | 檢查檔案是否存在             |
| `for`                    | 重複執行程式                 |
| `if`                     | 判斷條件                     |
| `enumerate()`            | 同時取得編號和資料           |
| `%`                      | 餘數運算，常用來平均分配位置 |

## 🎯 本次課程重點

這次課程學會了如何使用 **Streamlit** 製作簡單的網頁，包含顯示圖片、輸入數字、建立按鈕、顯示成功或錯誤訊息，以及使用下拉選單與多欄版面。也學會利用 `os` 讀取資料夾中的圖片，使用 `for` 和 `if` 控制程式流程，並透過 `st.session_state` 記住商品庫存，完成一個可以購買商品、增加庫存並即時更新畫面的簡易購物平台。
