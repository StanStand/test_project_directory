# # # while 迴圈

# # while True:
# #     x = input("請輸入一個數字:")
# #     if x == "不玩了":
# #         print("再見!")
# #         break
# # else:
# #     print(x)

# # 數字 = 1
# # while 數字 <=5:
# #     print(數字)
# #     數字 += 1

# 早餐 = ["蛋糕", "三明治", "漢堡", "飯糰"]
# 編號 = 0
# while 編號 < len(早餐):
#     print(早餐[編號])
#     編號 += 1

# 商品價格 = 1000
# A玩家 = input("輸入第一位玩家的暱稱: ")
# B玩家 = input("輸入第二位玩家的暱稱: ")
# 回答次數 = 1
# 總次數 = 3
# while 回答次是 <=總次次數:
#     A作答 = int(input(f"請{A玩家}輸入商品金額"))
#     B作答 = int(input(f"請{B玩家}輸入商品金額"))
#     if A作答 == 商品價格:
#         print(f"{A玩家}猜對了!{A玩家}獲勝! ")
#         break
#     elif B作答 == 商品價格:
#         print(f"{B玩家}猜對了!{B玩家}獲勝! ")
#         break
#     elif abs(商品價格 - A作答) < abs(商品價格 - B作答): # 這個練習暫不考慮兩個玩家出價相同的情形
#         print(f"{A玩家}的答案比較接近價格")
#     else:
#         print(f"{B玩家}的答案比較接近價格")
#     回答次數 += 1
# if abs(商品價格 - A作答) < abs(商品價格 - B作答):
#     print(f"遊戲結束!正確商品價格是{商品價格}，{A玩家}的答案比較接近，{A玩家}獲勝! ")
# else:
#     print(f"遊戲結束!正確商品價格是{商品價格}，{B玩家}的答案比較接近，{B玩家}獲勝! ")
# 回答次數 += 1
# # 1+2+3+....+10

# n=1
# sum=0 #紀錄累加的結果
# while n<=10:
#     sum=sum+n
#     n+=1
# print(sum)

# for 迴圈
# sum=0
# for x in range (1,11):
#     sum=sum+x
# print(sum)

# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     n+=1
# print(n) #印出2

# n=1
# while n<5:
#     print("變數n的資料是:",n)
#     n+=1
# else:
#     print(n) #結束迴圈前，印出5

# for c in "Hello":
#     print("逐一取得字串中的字元",c)
# else:
#     print(c) #結束迴圈前,印出o

# n=0
# while n<5:
#     if n==3:
#         break
#     print(n) #印出迴圈中的n
#     n+=1
# print("最後的 n:", n) # 印出迴圈結束後的 n

# countinue 的簡易範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: # X是偶數
#         continue
#     print(x)
#     n+=1
# print("最後的n:", n)

# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum) # 印出 1+2+...+10的結果



# 綜合範例:找出整數平方根
# 輸入 9. 得到 3
# 輸入 11, 得到【沒有】整數平方根

# n = int(input("請輸入一個正整數: "))
# for i in range(n): # i從 0 ~ n-1
#     if i*i==n:
#         print("整數平方根", i)
#         break # 用break 強制結束迴圈時， 不會執行 else 區塊
# else:
#     print("沒有整數平方根")

# 4 串列

# join 結合
學生 = ["小明", "小華", "小杰", "阿花"]
print("/".join(學生))

# 清單內容修改
學生 = ["小明", "小華", "小杰", "阿花"]
學生[1] = "小美"
print(學生)

# 鎖住清單內容List清單變Tuple元組 (無法更改內容)
學生 = ("小明", "小華", "小杰", "阿花")
學生[1] = "小美"
print(學生)

# 新增清單資料
學生 = ["小明", "小華", "小杰", "阿花"]
學生.append("小美")
學生.extend(["小娜", "小雅"])
print(學生)

# 刪除清單資料
學生 = ["小明", "小華", "小杰", "阿花"]
學生.remove("小華")
學生.pop(1)
print(學生)

# 刪除沒看到的資料 無法看到
學生 = ["小明", "小華", "小杰", "阿花"]
學生.remove("小美")

# 搜尋此名單
學生 = ["小明", "小華", "小杰", "阿花"]
if "小明" in 學生:
    print("小明有在名單中")

# 查出名單中的位置
學生 = ["小明", "小華", "小杰", "阿花"]
print(學生.index("小華"))

# # 字典

# 手機 = {
#     "廠牌" : "蘋果",
#     "型號" : "iPhone 13 Pro",
#     "容量" : "256 GB"
# }
# 手機["顏色"] = ["天空藍"]
# 手機["容量"] = ["512 GB, 256GB"]
# print(手機.get("型號"))
# print(手機)

# # append(x)：在串列末尾添加元素 x。


# list1 = [1, 2, 3]
# list1.append(4)  # list1 變為 [1, 2, 3, 4]
# # extend(iterable)：將一個可迭代物件中的所有元素添加到串列末尾。


# list1 = [1, 2, 3]
# list1.extend([4, 5])  # list1 變為 [1, 2, 3, 4, 5]
# # insert(i, x)：在索引 i 處插入元素 x。


# list1 = [1, 2, 3]
# list1.insert(1, 1.5)  # list1 變為 [1, 1.5, 2, 3]
# #　remove(x)：移除串列中第一次出現的元素 x。


# list1 = [1, 2, 3, 2]
# list1.remove(2)  # list1 變為 [1, 3, 2]
# # pop([i])：移除並返回索引 i 處的元素。如果沒有指定索引，則移除並返回最後一個元素。


# list1 = [1, 2, 3]
# list1.pop()  # 返回 3，list1 變為 [1, 2]
# list1.pop(0)  # 返回 1，list1 變為 [2]
# # clear()：移除串列中的所有元素。


# list1 = [1, 2, 3]
# list1.clear()  # list1 變為 []
# # index(x[, start[, end]])：返回串列中第一次出現元素 x 的索引值。如果指定了起始和結束範圍，則在該範圍內查找。


# list1 = [1, 2, 3, 2]
# list1.index(2)  # 返回 1
# # count(x)：返回元素 x 在串列中出現的次數。


# list1 = [1, 2, 3, 2]
# list1.count(2)  # 返回 2
# # sort(key=None, reverse=False)：對串列中的元素進行排序。可選參數 key 用於自定義排序方式，reverse 為 True 時會降序排序。


# list1 = [3, 1, 2]
# list1.sort()  # list1 變為 [1, 2, 3]
# list1.sort(reverse=True)  # list1 變為 [3, 2, 1]
# # reverse()：反轉串列中的元素順序。


# list1 = [1, 2, 3]
# list1.reverse()  # list1 變為 [3, 2, 1]
# # copy()：返回串列的淺複本。


# list1 = [1, 2, 3]
# list2 = list1.copy()  # list2 變為 [1, 2, 3]

# list1 = [1, 2, 3, 4, 5]
# length = len(list1)  # 返回 5，因為 list1 中有 5 個元素
# print(length)

# #len() 是一個用於計算序列（如串列、元組、字串等）長度的內建函數，而不是串列的內建方法。這個函數返回序列中元素的數量。