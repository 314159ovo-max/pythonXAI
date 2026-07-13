print("hello world!!!")
print("Tiffany")
print("不要低頭\n雙下巴會出來")
"""
這是多行註解
"""

#這是單行註解
print("hello world!!!")#print是在終端機顯示文字的指令
#ctrl+?可以快速駐解/取消註解
print(1)#int是整數(-1,0,1)
print(1.0)#float是浮點數(1.0,3.14)
print(1.234)#float是浮點數
print("apple")#str是字串("sandy",'1')
print(True)#bool是布林值(True,False)(開頭要大寫)
print(False)#布林值(True,False)

#變數
a=10#新增一個儲存空間並取名為a,"="的功能是將右邊的值10存入左邊的a
print(a)#在終端機顯示A所存在的值
a="apple"#將a的值改為"apple"
print(a)#在終端機顯示A所存的值

#運算子
print(1+1)#加法
print(1-1)#減法
print(2*3)#乘法
print(6/2)#除法
print(7//2)#取商
print(7%2)#取餘數
print(2**3)#次方

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減

#字串運算+-/*
print("apple"+"pen")#字串相加
print("apple"*3)#字串乘法

# 字串格式化
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")  # f-string
# 可以將變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示
print()