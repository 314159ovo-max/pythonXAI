import streamlit as st
with st.expander("Class 1 課堂筆記"):
    st.write(
        """
---
# Python 筆記 🐍

## 1. 什麼是 Python？

Python 是一種**程式語言**，可以讓電腦照著我們寫的指令做事情。
---

# 2. 顯示文字：`print()`

`print()` 可以把內容顯示在畫面上。

```python
print("Hello World!")
```

畫面會顯示：

```
Hello World!
```

也可以印出自己的名字：

```python
print("Tiffany")
```

---

## 換行：`\n`

`\n` 可以讓文字換到下一行。

```python
print("不要低頭\n雙下巴會出來")
```

結果：

```
不要低頭
雙下巴會出來
```

---

# 3. 註解（給自己看的提醒）

註解不會被電腦執行，只是幫助自己記錄。

### 單行註解

```python
# 這是一行註解
```

### 多行註解

```python
\"""
第一行
第二行
第三行
\"""
```

💡 小技巧：

按 **Ctrl + /**（有些電腦是 Ctrl + ?）可以快速加上或取消註解。

---

# 4. 資料種類（資料型態）

Python 有很多種資料。

| 型態    | 名稱                 | 範例            |
| ------- | -------------------- | --------------- |
| `int`   | 整數                 | `1`、`10`、`-5` |
| `float` | 小數                 | `3.14`、`1.0`   |
| `str`   | 字串（文字）         | `"apple"`       |
| `bool`  | 布林值（只有對或錯） | `True`、`False` |

例如：

```python
print(1)
print(3.14)
print("apple")
print(True)
```

---

# 5. 變數（小盒子）

變數就像一個**有名字的小盒子**，可以放東西。

```python
a = 10
```

代表：

把 **10 放進名字叫 a 的盒子裡。**

印出來：

```python
print(a)
```

結果：

```
10
```

也可以換成別的東西：

```python
a = "apple"
print(a)
```

結果：

```
apple
```

---

# 6. 數學運算

| 運算   | 符號 | 範例       |
| ------ | ---- | ---------- |
| 加法   | `+`  | `1+1`      |
| 減法   | `-`  | `5-2`      |
| 乘法   | `*`  | `2*3`      |
| 除法   | `/`  | `6/2`      |
| 取商   | `//` | `7//2 = 3` |
| 取餘數 | `%`  | `7%2 = 1`  |
| 次方   | `**` | `2**3 = 8` |

---

## 運算順序

先算：

1. `()`
2. `**`
3. `* / // %`
4. `+ -`

例如：

```python
print((2+3)*4)
```

答案是：

```
20
```

---

# 7. 字串運算

## 字串相加

```python
print("apple" + "pen")
```

結果：

```
applepen
```

---

## 字串重複

```python
print("apple"*3)
```

結果：

```
appleappleapple
```

---

# 8. f 字串（把資料放進句子）

可以把變數放進一句話裡。

```python
name = "Apple"
age = 18

print(f"我是{name}，今年{age}歲。")
```

結果：

```
我是Apple,今年18歲。
```

大括號 `{}` 裡可以放變數。

---

# 9. 字串長度：`len()`

`len()` 可以數一共有幾個字。

```python
print(len("apple"))
```

結果：

```
5
```

因為：

```
a p p l e
1 2 3 4 5
```

---

# 10. 查看資料型態：`type()`

可以知道資料是哪一種。

```python
print(type(1))
```

結果：

```
<class 'int'>
```

其他例子：

```python
type(3.14)
type("apple")
type(True)
```

---

# 11. 型態轉換

有時候可以把資料換成另一種型態。

| 指令      | 功能             |
| --------- | ---------------- |
| `int()`   | 變整數           |
| `float()` | 變小數           |
| `str()`   | 變文字           |
| `bool()`  | 變 True 或 False |

例如：

```python
int(1.9)
```

結果：

```
1
```

```python
float(1)
```

結果：

```
1.0
```

```python
str(123)
```

結果：

```
"123"
```

⚠️ 注意：

```python
int("hello")
```

會出錯！

因為 `"hello"` 不是數字。

---

# 12. 讓使用者輸入：`input()`

可以請使用者輸入資料。

```python
name = input("請輸入名字：")
```

如果要做數學運算，要先變成數字。

例如：

```python
r = float(input("請輸入半徑："))
```

---

# 13. 練習：計算圓面積

公式：

```
圓面積 = 3.14 × 半徑²
```

程式：

```python
r = float(input("請輸入半徑："))
print(f"圓面積為：{3.14*r**2}")
```

---

# 14. 練習：計算平均成績

```python
mid = float(input("請輸入期中成績："))
final = float(input("請輸入期末成績："))

print(f"平均成績：{(mid+final)/2}")
``
"""
    )


with st.expander("Class 2 課堂筆記"):
    st.write(
        """
# Python 基礎筆記

## 一、for 迴圈（重複做事情）

### 什麼是 for 迴圈？

for 迴圈就像叫機器人幫我們一直做同一件事情，不需要一直自己寫。

### 基本寫法

```python
for i in range(5):
    print(i)
```

執行結果：

```
0
1
2
3
4
```

### range() 是什麼？

`range()` 是用來產生一串數字。

> **注意：最後一個數字不會出現！**

例如：

```python
range(5)
```

會產生：

```
0、1、2、3、4
```

---

### range(開始, 結束)

```python
for i in range(1,5):
    print(i)
```

結果：

```
1
2
3
4
```

代表：

* 從 1 開始
* 到 5 前面停止（不包含 5）

---

### range(開始, 結束, 間隔)

```python
for i in range(1,10,2):
    print(i)
```

結果：

```
1
3
5
7
9
```

表示每次增加 2。

---

## 二、迴圈中的變數

```python
for i in range(5):
    a = i * 2

print(a)
```

每次都會重新計算 `a`。

最後一次：

```
i = 4
a = 8
```

所以最後印出：

```
8
```

---

## 三、使用 Streamlit 接收輸入

```python
number = st.number_input("請輸入1~9", step=1, min_value=1, max_value=9)
```

這會出現一個可以輸入數字的小方框。

例如輸入：

```
5
```

再配合：

```python
for i in range(1, number+1):
    st.write(str(i)*i)
```

結果：

```
1
22
333
4444
55555
```

因為：

* 1 印 1 次
* 2 印 2 次
* 3 印 3 次
* …

---

# 四、List（串列）

## 什麼是 List？

List 就像一個收納盒，可以放很多資料。

例如：

```python
L = [1,2,3]
```

裡面放了三個數字。

也可以放不同種類的資料：

```python
L = [1, True, "apple", 3.14]
```

可以放：

* 數字
* 文字
* 布林值（True、False）
* 小數

甚至還可以放另一個 List：

```python
L = [1,2,[3,4]]
```

---

# 五、取得 List 裡面的資料（Index）

每個資料都有自己的位置。

位置從 **0 開始算**。

例如：

```python
L = [1,2,3,"a","b","c"]
```

位置如下：

| 位置(Index) | 內容  |
| --------- | --- |
| 0         | 1   |
| 1         | 2   |
| 2         | 3   |
| 3         | "a" |
| 4         | "b" |
| 5         | "c" |

例如：

```python
print(L[0])
```

結果：

```
1
```

```python
print(L[3])
```

結果：

```
a
```

---

# 六、List 切片（Slice）

可以一次拿很多資料。

## 全部每隔兩個拿一次

```python
L[::2]
```

結果：

```
[1,3,"b"]
```

---

## 拿第1到第3個位置

```python
L[1:4]
```

結果：

```
[2,3,"a"]
```

因為 **4 不包含**。

---

## 每隔兩個拿一次

```python
L[1:4:2]
```

結果：

```
[2,"a"]
```

---

# 七、新增資料（append）

把新東西放到最後面。

```python
L=[1,2,3]
L.append(4)
```

結果：

```
[1,2,3,4]
```

---

# 八、刪除資料

有兩種方法。

## 方法一：remove()

刪除指定的資料。

```python
L=["a","b","c","d","a"]

L.remove("a")
```

結果：

```
["b","c","d","a"]
```

只會刪掉第一個找到的 `"a"`。

---

## 方法二：pop()

依照位置刪除。

```python
L.pop(0)
```

刪掉第一個元素。

如果寫：

```python
L.pop()
```

就會刪掉最後一個元素。

---

# 九、排序（sort）

把數字由小排到大。

```python
L=[3,1,5,2]

L.sort()
```

結果：

```
[1,2,3,5]
```

注意：

`sort()` 會直接改變原本的 List。

---

# 十、走訪 List（讀取每一個資料）

有兩種方法。

## 方法一：用 Index

```python
L=[1,2,3,"a","b","c"]

for i in range(len(L)):
    print(L[i])
```

會依序印出所有資料。

如果改成：

```python
for i in range(0, len(L), 2):
    print(L[i])
```

就會每隔一個印一次。

---

## 方法二：直接讀資料

```python
for item in L:
    print(item)
```

結果：

```
1
2
3
a
b
c
```

這種方法比較簡單，也很常使用。

---

# 本堂課重點整理

✅ `for`：重複做事情。

✅ `range()`：產生一串數字，最後一個數字不包含。

✅ 變數：可以存放資料。

✅ `List`：可以一次存很多資料。

✅ `Index`：資料的位置，從 **0** 開始。

✅ `Slice`：一次取得很多資料。

✅ `append()`：新增資料到最後面。

✅ `remove()`：刪除指定資料（只刪第一個找到的）。

✅ `pop()`：依照位置刪除資料，不寫位置就刪最後一個。

✅ `sort()`：把資料排序（由小到大）。

✅ 走訪 List：

* 用 Index 讀取。
* 或直接用 `for item in List` 讀取。


"""
    )



with st.expander("Class 3 課堂筆記"):
    st.write(
        """


# Python 基礎筆記（國小版）

## Streamlit 介面設計

---

# 一、什麼是 Streamlit？

**Streamlit** 是一個可以把 Python 程式變成網頁的小工具。

我們可以用它做出：

* 按鈕
* 文字
* 輸入框
* 排版
* 小遊戲
* 小工具

就像在蓋一個簡單的小網站。

---

# 二、標題（title）

可以在網頁上放一個大標題。

```python
st.title("欄位元件")
```

畫面會看到：

**欄位元件**

---

# 三、欄位（Columns）

## 什麼是欄位？

欄位就是把畫面切成好幾格。

例如：

```
┌──────────┬──────────┐
│   左邊    │   右邊    │
└──────────┴──────────┘
```

程式：

```python
col1, col2 = st.columns(2)
```

代表：

* col1 是左邊
* col2 是右邊

---

## 在欄位放按鈕

```python
col1.button("按鈕1")
col2.button("按鈕2")
```

畫面：

```
按鈕1      按鈕2
```

---

# 四、調整欄位大小

可以讓左右大小不同。

```python
col1, col2 = st.columns([1,2])
```

表示：

```
┌─────┬──────────┐
│ 小格 │   大格    │
└─────┴──────────┘
```

左邊比較小，右邊比較大。

---

## 三個欄位

```python
col1, col2, col3 = st.columns([1,2,3])
```

畫面大概像：

```
小     中        大
```

第三格最大。

---

# 五、with 的用法

有時候一個欄位裡要放很多東西。

就可以使用：

```python
with col1:
```

例如：

```python
with col1:
    st.button("按鈕1")
    st.write("這是col1")
```

表示：

按鈕和文字都會放在左邊。

---

# 六、按鈕（Button）

建立按鈕：

```python
st.button("按鈕")
```

畫面會出現一個按鈕。

當按下去時，可以做事情。

例如：

```python
if st.button("按鈕"):
    st.write("你好")
```

按下按鈕後，就會顯示：

```
你好
```

---

# 七、氣球效果（Balloons）

如果想讓畫面更有趣：

```python
st.balloons()
```

畫面會飛出很多氣球 🎈🎈🎈

常用來表示：

* 成功
* 恭喜
* 完成任務

---

# 八、使用 for 建立很多欄位

不用一直重複寫程式。

例如：

```python
cols = st.columns(4)
```

表示建立四個欄位。

再搭配：

```python
for i in range(len(cols)):
```

就能自動放四個按鈕。

畫面：

```
按鈕1  按鈕2  按鈕3  按鈕4
```

這樣比較省時間。

---

# 九、不同排列方式

方法一：

```
按鈕1    文字
按鈕2    文字
按鈕3    文字
```

方法二：

```
按鈕1    文字1

按鈕2    文字2

按鈕3    文字3
```

不同寫法，畫面的排列方式也會不同。

---

# 十、文字輸入框（text_input）

可以讓使用者輸入文字。

```python
text = st.text_input("請輸入文字")
```

畫面：

```
請輸入文字：
______________
```

如果輸入：

```
小明
```

可以利用：

```python
st.write(text)
```

顯示：

```
小明
```

---

## 預設文字

可以先放好內容。

```python
st.text_input(
    "請輸入文字",
    value="這是預設文字"
)
```

輸入框一開始就會看到：

```
這是預設文字
```

---

# 十一、變數

變數就像一個盒子，可以放資料。

例如：

```python
ans = 1
```

表示：

```
ans
┌───┐
│ 1 │
└───┘
```

---

# 十二、按鈕加一

例如：

```python
if st.button("加1"):
    ans = ans + 1
```

意思是：

每按一次按鈕，

```
1
↓

2
↓

3
↓

4
```

但是！

如果只是一般變數，

畫面重新整理後，

它又會回到：

```
1
```

---

# 十三、Session State（記憶盒子）

Session State 就像一個**會記住資料的盒子**。

即使畫面重新整理，

資料還會保留下來。

例如：

```python
st.session_state.ans1 = 1
```

之後：

```python
st.session_state.ans1 += 1
```

每按一次按鈕，

數字都會一直增加。

```
1
↓

2
↓

3
↓

4
```

不會重新變回 1。

---

## 為什麼要先判斷？

```python
if "ans1" not in st.session_state:
```

意思是：

「如果還沒有這個盒子，就先建立一個。」

避免程式找不到資料而發生錯誤。

---

# 十四、重新整理畫面（rerun）

有時候程式改變了，

畫面沒有馬上更新。

這時可以使用：

```python
st.rerun()
```

意思是：

**請程式重新執行一次。**

畫面就會更新成最新的內容。

---

# 本堂課重點整理

✅ **st.title()**：建立大標題。

✅ **st.columns()**：把畫面分成很多欄。

✅ **with**：在同一個欄位放很多元件。

✅ **st.button()**：建立按鈕。

✅ **st.balloons()**：顯示氣球動畫。

✅ **for**：快速建立很多按鈕或欄位。

✅ **st.text_input()**：建立文字輸入框。

✅ **變數**：可以存放資料，但重新整理後通常會回到原本的值。

✅ **st.session_state**：像會記住資料的盒子，可以保存資料，不會因重新整理而消失。

✅ **st.rerun()**：讓程式重新執行，更新畫面。

---

# 記憶小技巧 🎈

🏠 **columns** → 把畫面分成很多小房間。

🔘 **button** → 可以按的按鈕。

⌨️ **text_input** → 可以打字的地方。

📦 **變數** → 普通盒子，容易忘記。

🧠 **session_state** → 有記憶力的盒子，會一直記住資料。

🔄 **rerun** → 請程式重新開始跑一次。


"""
    )


with st.expander("Class 4 課堂筆記"):
    st.write(
        """
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


""")
    



with st.expander("Class 5 課堂筆記"):
    st.write(
        """
# 🌟 Python + OpenAI + Streamlit 聊天機器人筆記

---

# 🤖 今天學了什麼？

今天我們學會了：

- 💬 跟 AI 聊天
- 🔑 使用 OpenAI API
- 📝 記住聊天內容
- 🌐 用 Streamlit 做聊天網頁
- 🗑️ 清除聊天紀錄
- 🤖 選擇不同 AI 模型

最後可以做出一個像 ChatGPT 一樣的聊天程式！

---

# 一、載入需要的工具

```python
import openai
from dotenv import load_dotenv
import os
```

## ✨ 指令說明

### `import openai`

載入 OpenAI 工具。

有了它，Python 才能和 AI 對話。

---

### `from dotenv import load_dotenv`

載入 `.env` 檔案的工具。

可以把重要的密碼（API Key）讀進程式。

---

### `import os`

載入作業系統工具。

可以讀取環境變數、資料夾和檔案。

---

# 二、讀取 .env 檔案

```python
load_dotenv()
```

## 功能

把 `.env` 裡面的資料讀進來。

例如：

```
OPENAI_API_KEY=你的金鑰
```

程式就可以使用它。

---

# 三、設定 API 金鑰

```python
openai.api_key = os.getenv("OPENAI_API_KEY")
```

## 功能

把 API 金鑰交給 OpenAI。

API Key 就像：

🔑 AI 世界的通行證。

沒有它，就不能使用 AI。

---

# 四、while 迴圈

```python
while True:
```

## 功能

一直重複執行程式。

除非遇到：

```python
break
```

才會停止。

---

# 五、輸入文字

```python
user_input = input("你:")
```

## 功能

讓使用者在終端機輸入文字。

例如：

```
你：你好
```

---

# 六、判斷是否離開

```python
if user_input.lower() in ["exit","quit"]:
```

## 功能

把英文變成小寫，再檢查是不是：

- exit
- quit

如果是：

```python
break
```

程式就結束。

---

# 七、建立 AI 回應

```python
response = openai.chat.completions.create(...)
```

## 功能

把問題送給 AI。

AI 回答後，再把答案傳回來。

---

# 八、選擇 AI 模型

```python
model="gpt-4o-mini"
```

## 功能

決定要使用哪一種 AI。

今天學到：

- `gpt-4o-mini`（速度快）
- `gpt-4o`（能力更強）
- `gpt-4o-search-preview`（可以搜尋網路）

---

# 九、messages（聊天內容）

```python
messages=[
    {"role":"system","content":"請用繁體中文"},
    {"role":"user","content":user_input},
]
```

## 功能

把聊天內容送給 AI。

每一則訊息都有：

### role（角色）

可以是：

- system（系統）
- user（使用者）
- assistant（AI）

---

### content（內容）

真正說的話。

例如：

```
你好
```

---

# 十、System Message（系統訊息）

```python
{
    "role":"system",
    "content":"請用繁體中文"
}
```

## 功能

告訴 AI：

要怎麼回答。

例如：

- 使用繁體中文
- 當老師
- 當翻譯員
- 當故事作家

---

# 十一、取得 AI 回答

```python
assistant_message =
response.choices[0].message.content
```

## 功能

把 AI 回答的文字拿出來。

---

# 十二、print()

```python
print(f"AI:{assistant_message}")
```

## 功能

把 AI 回答顯示在終端機。

例如：

```
AI：你好！
```

---

# 十三、建立聊天紀錄

```python
messages = [
    {
        "role":"system",
        "content":"請用繁體中文"
    }
]
```

## 功能

建立一個聊天清單。

之後所有對話都放進去。

---

# 十四、append()

```python
messages.append(...)
```

## 功能

把新的資料加到最後面。

例如：

使用者說：

```
你好
```

就加入：

```python
{
 "role":"user",
 "content":"你好"
}
```

---

AI回答：

```
哈囉！
```

再加入：

```python
{
 "role":"assistant",
 "content":"哈囉！"
}
```

---

這樣 AI 就會記得之前聊天內容。

---

# 十五、Streamlit 聊天泡泡

```python
st.chat_message()
```

## 功能

建立聊天泡泡。

例如：

👤 使用者

🤖 AI

---

顯示：

```python
st.chat_message("user")
```

使用者泡泡。

---

```python
st.chat_message("assistant")
```

AI 泡泡。

---

# 十六、write()

```python
.write()
```

## 功能

把文字放進聊天泡泡裡。

例如：

```python
st.chat_message("assistant").write("你好")
```

---

# 十七、avatar（頭像）

```python
avatar="🪄"
```

## 功能

設定聊天角色的小圖示。

例如：

🪄 使用者

✨ AI

---

# 十八、for 迴圈

```python
for message in history:
```

## 功能

把每一筆聊天紀錄都顯示出來。

例如：

```
你好

哈囉

今天天氣？

很好
```

全部都會出現在畫面。

---

# 十九、session_state

```python
st.session_state
```

## 功能

幫程式記住資料。

今天記住的是：

聊天紀錄。

即使重新整理網頁，

聊天也不會消失。

---

初始化：

```python
if "history" not in st.session_state:
```

第一次打開程式時，

建立一個空清單。

---

# 二十、聊天輸入框

```python
st.chat_input()
```

## 功能

建立 ChatGPT 那種輸入框。

例如：

```
請輸入訊息……
```

---

# 二十一、重新整理畫面

```python
st.rerun()
```

## 功能

重新執行程式。

新的聊天就會立刻出現在畫面。

---

# 二十二、st.secrets

```python
st.secrets["OPENAI_API_KEY"]
```

## 功能

在 Streamlit Cloud 裡，

安全保存 API 金鑰。

不用寫在程式裡。

---

# 二十三、文字輸入框

```python
st.text_input()
```

## 功能

建立一個可以輸入文字的地方。

今天拿來修改：

System Message。

---

# 二十四、下拉選單

```python
st.selectbox()
```

## 功能

讓使用者選擇 AI 模型。

例如：

```
▼ GPT-4o-mini
```

---

# 二十五、按鈕

```python
st.button()
```

## 功能

建立按鈕。

今天是：

🗑️ 清除聊天紀錄。

---

# 二十六、清空聊天

```python
st.session_state.history = []
```

## 功能

把聊天紀錄變成空的。

聊天就全部消失了。

---

# 二十七、columns()

```python
st.columns([4,2,1])
```

## 功能

把畫面分成三個區塊。

今天是：

```
系統訊息

AI模型

🗑️
```

排成同一列。

---

# 二十八、建立完整 AI 聊天流程

程式流程如下：

```
使用者輸入問題
        │
        ▼
加入聊天紀錄
        │
        ▼
送給 OpenAI
        │
        ▼
AI產生回答
        │
        ▼
把回答加入聊天紀錄
        │
        ▼
重新整理畫面
```

這樣就能一直聊天，而且 AI 會記得之前說過的內容。

---

# 📚 今天學到的重要指令整理

| 指令                                  | 功能                                |
| ------------------------------------- | ----------------------------------- |
| `import openai`                       | 載入 OpenAI 工具                    |
| `load_dotenv()`                       | 讀取 `.env` 檔案                    |
| `os.getenv()`                         | 取得環境變數                        |
| `openai.api_key`                      | 設定 API 金鑰                       |
| `while True`                          | 無限重複執行                        |
| `input()`                             | 接收使用者輸入                      |
| `print()`                             | 顯示文字                            |
| `if`                                  | 判斷條件                            |
| `break`                               | 離開迴圈                            |
| `messages`                            | 儲存聊天內容                        |
| `role`                                | 訊息角色（system、user、assistant） |
| `content`                             | 訊息內容                            |
| `append()`                            | 新增資料到清單                      |
| `openai.chat.completions.create()`    | 向 AI 發送聊天請求                  |
| `model`                               | 選擇 AI 模型                        |
| `response.choices[0].message.content` | 取得 AI 回答                        |
| `st.chat_message()`                   | 顯示聊天泡泡                        |
| `.write()`                            | 顯示文字                            |
| `avatar`                              | 設定聊天頭像                        |
| `st.chat_input()`                     | 建立聊天輸入框                      |
| `st.session_state`                    | 記住聊天資料                        |
| `st.secrets`                          | 安全儲存 API 金鑰                   |
| `st.text_input()`                     | 建立文字輸入框                      |
| `st.selectbox()`                      | 建立下拉式選單                      |
| `st.button()`                         | 建立按鈕                            |
| `st.columns()`                        | 建立多欄版面                        |
| `st.rerun()`                          | 重新整理畫面                        |

---

# 🎯 本次課程重點

這次課程學會了如何使用 **OpenAI API** 與 AI 對話，並了解 **API 金鑰**、**System Message**、**聊天紀錄（messages）** 和 **AI 模型（model）** 的用途。接著利用 **Streamlit** 製作聊天介面，學會使用聊天泡泡、聊天輸入框、按鈕、下拉選單與多欄排版，並透過 **`st.session_state`** 保存聊天紀錄，讓 AI 能記住之前的對話。最後完成了一個具有**持續對話、模型切換、系統訊息設定與清除聊天紀錄**功能的簡易 AI 聊天機器人。


""")