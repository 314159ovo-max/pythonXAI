print([])#這是一個空的list
print([1,2,3])#這是一個有三個元素的list
print([1,2,3,"a","b","c"])#這是一個有六個list
print([1,2,3,["a","b","c"]])#這是一個有四個元素的list
print([1,True,"a",1.23])#這是一個元素的lite

#list 讀取元素,元素的index從0開始
L=[1,2,3,"a","b","c"]
print(L[0])#1
print(L[1])#2
print(L[2])#3
print(L[3])#"a"

L=[1,2,3,"a","b","c"]
#就是取index 0到最後,每次取2個元素,所以是[1,3,'b']
print(L[::2])
#就是取index 1到3的元素,不包含index4,所以是[1,3,'b']
print(L[1:4])
#就是取index 1到3的元素,不包含index4,並且每次取2個元素,所以是[2,'a']
print(L[1:4:2])
#跟range一樣的用法,只是符號不同


#list的append
L=[1,2,3]
L.append(4)#把4加到L的最後面
print(L)

#list的移除元素方式有兩種
#1.使用remove,可以移除指定元素
L=["a","b","c","d","a"]
L.remove("a")
#移除第一個"a"
#代表remove會從頭開始找,找到第一個符合的元素就會移除
#如果想移除所有符合的元素,可以使用迴圈

for i in range(1,10):
    if i == "a":
    
        L.remove(i)

#2.使用pop,可以移除指定的index的元素
L=["a","b","c","d","a"]
L.pop(0)#移除index0的元素
#代表pop會移除指定的index的元素
#如果不指定index,則會移除最後一個元素
L.pop()#移除最後一個元素
print(L)

#sort:將List中的元素進行排序,預設始由小到大(升序排列)
#注意:這個方法會直接修改原本的List,不會生產新的List
L=[1,3,2,4,5]
L.sort()
print(L)

#list 走訪元素
#可以透過取得index的方式來找到list的資料
#也可以直接把list當作一個範圍來取得資料
#這兩種方式都可以,但是看使用的環境是否會需要index來定要用哪一種方式
L=[1,2,3,"a""b""c"]
for i in range(0, len(L),2):
    print(L[i])
for i in L:
    print(i)