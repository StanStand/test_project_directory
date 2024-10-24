# 折線圖
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [2, 4, 1, 5])
plt.show()

# 圖表中的中文

# 設定支援中文的字形
plt.rc("font", family="Microsoft JhengHei")
# 使用rc方法，設定執行環境:
plt.rc("font", family="")

# 程式碼:字形的名稱

 
# 標籤與圖例

# 使用label參數設定標籤
# 使用legend方法，產生圖利

# 資料點(X,Y)範例

# 第一組(2, 4)(3, 6)(4, 8)
# 第二組(2, 2)(3, 3)(4, 4)

# 程式碼 
plt.plot(
    [2,3,4],
    [[4,2],[6,4],[8,4]],
    label=['第一組']["第二組"] 
)

# 設定完標籤後，呼叫legend產生圖例
plt.legend()

# 軸線的標題
plt.plot([2, 3, 4],[4, 6, 8])
plt.xlabel("x軸的標題")
plt.ylabel("y軸的標題")

# 演練目標
# 繪製一組資料的折線圖
# 繪製兩組資料點的折線圖，並且加上適當的標示。
# 載入CSV格式的檔案資料，繪製折線圖並加上適當的標示

import matplotlib.pyplot as plt
plt.rc("font", family="Microsoft JhengHei")

# 一組資料點
(1,2), (2,4), (3,6)

plt.plot([1,2,3], [2,4,6])
plt.show()

# 兩組資料點
(1,2), (2,4), (3,6)
(1,1), (2,2), (3,3)

plt.plot([1, 2, 3], [[2,1], [4,2], [6,3]], label=["第一組標籤", "第二組標籤"]) # 設定每一組資料和對應的標籤
plt.legend() # 產生圖例
plt.xlabel("x軸的文字說明")
plt.ylabel("y軸的文字說明")
plt.show()

# 從CSV格式的檔案載入資料，並繪製折線圖
import csv 
file = open(r"C:\Users\stan_liao\Desktop\VS Code Python\csv\data.csv", encoding="utf-8")
reader = csv.reader(file)
header = next(reader) # 讀取第一列
print("標頭", header)
x=[] # 預期 [2010,2011,2012]
y=[] # 預期 [[40000, 30000], [42000, 60000], [45000, 50000]]
for row in reader:
    print("每列的資料", row)
    x.append(int(row[0]))
    y.append([int(row[1]), int(row[2])])

plt.plot(x,y, label=["小王", "小美"])
plt.plot(x,y, label=header[1:3])
plt.legend()
plt.xlabel(header[0])
plt.ylabel("薪資")
plt.show()


# 使用 Pandas 簡化代碼的方式
import pandas as pd
import matplotlib.pyplot as plt

# 使用 Pandas 讀取 CSV 檔案
df = pd.read_csv(r"C:\Users\stan_liao\Desktop\VS Code Python\csv\data.csv", encoding="utf-8")

# 檢查標頭和資料
print("標頭", df.columns)
print(df)

# 繪製折線圖
df.plot(x='年度', y=['小王', '小美'], kind='line', marker='o')

# 添加標籤和標題
plt.xlabel('年度')
plt.ylabel('薪資')
plt.title('小王與小美的年度薪資變化')
plt.legend(title='人員')
plt.show()

# 圓餅圖
# 使用pie方法
# 根據一個維度的資料點畫出圓餅圖

# 標籤圖表跟圖例

# 使用label參數設定標籤
# 使用legend方法，產生圖例

# 資料點x範圍如下:
20,30,40

# 程式碼
plt.pie(
        [20,30,40]
        labels=["第一塊","第二塊","第三塊"],
        labeldistance=0.5
)
# 設定標籤後，呼叫legend產生圖例
plt.legend()

# 標籤的位置
# 使用labeldistance參數設定標籤位置
# 0代表原心，1代表原周
# 圖表的標題

# 使用title方法設定圖表標題
plt.pie([20,30,40])
plt.title("這是一個圓餅圖")

# 演練目標
# 繪製一組資料點的圓餅圖，並且加上適當的百分比標示
# 載入CSV格式的檔案資料，繪製圓餅圖並加上適當的標示

