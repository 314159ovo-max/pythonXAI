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
