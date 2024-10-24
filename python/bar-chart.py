# X軸為數字，連續性
# X軸為數字串，離散性

# 使用bar方法
# 根據資料點畫出條圖

# 資料點(x,height)飯例如下:
# (1,4)(3,6)(4,2)


# 資料點(x,height)飯例如下:
# ("T,4")("A,6")("O",2)


# 預期的圖表:

# 程式碼:
# plt.bar([1,3,4],[4,6,2])
# plt.bar(["T","A","O"], [4,6,2])

# 樣式的調整跟軸線標題

# 圖表樣式

# 使用width參數設定寬度
# 使用color參數設定顏色

plt.bar(
    ["T", "A", "O"],
    [4,6,2],
width=0.5,
color="red"
)

# 軸線的標題

# xlabeke和ylabel方法
# 設定軸線標題

# 程式碼:

plt.bar(["T","A","O"],[4,6,2])
plt.xlabel("X軸的標題")
plt.ylabel("Y軸的標題")


# 演練目標
# 熟悉條圖的操作

# 繪製X軸為數字、字串型態的長條圖，觀察差異

# 調整長條圖的樣式和軸線標題

import matplotlib.pyplot as plt
plt.rc("font", family="Microsoft JhengHei")

'''
    # X軸為數字
    # X=[3,4,1]
    # height=[8,5,2]
'''
plt.bar([3,4,1], [8,5,2])
plt.show()
"""
    X軸為字串，調整寬度和顏色，加上標示
        x=["B","A","C"]
        height=[8,10,16]
"""

plt.bar(["B", "A", "C"],[8,10,16], width=0.5,color="red")
plt.bar(["B", "A", "C"],[8,10,16], width=0.5,color="#81D8D0")
plt.xlabel("測試的 X 軸標題")
plt.ylabel("測試的 Y 軸標題")
plt.show()


# 載入CSV格式的檔案資料，繪製長條圖並加上適當的標示
import csv 
file=open(r"C:\Users\stan_liao\Desktop\VS Code Python\csv\bar-chart-data.csv", encoding="utf-8")
reader=csv.reader(file)
header=next(reader) # 讀取第一列 ["花費項目", "金額"]
print(header)
x=[] # 預期 ["飲食", "房租", "娛樂", "交通", "衣裝"]
height=[]# 預期 [10000,12000,5000,3000,1000]
for row in reader:
    print(row)
    x.append(row[0])
    height.append(int(row[1]))
print(x)
print(height)
plt.bar(x,height,width=0.6,color="green")
plt.xlabel(header[0])
plt.ylabel(header[1])
plt.show()