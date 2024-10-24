import matplotlib.pyplot as plt
# 設定字形為Windows內建的微軟正黑體，支援中文顯示
plt.rc("font", family="Microsoft JhengHei")
# 繪製一組資料點的散布圖，設定樣式
'''
 一組資料點
(2,4), (4,3), (3,6)
'''
plt.scatter([2, 4, 3],[4, 3, 6], c="red", s=100)
plt.scatter([2, 4, 3],[4, 3, 6], c="#888888", s=100) # 可用色碼調色
plt.show()
# 繪製兩組資料點的散佈圖，加上標籤圖例
'''
 兩組資料點
 第一組 (2,4), (4,3), (3,6)
 第二組 (1,2), (3,5), (4,4)
'''

plt.scatter([2, 4, 3], [4, 3, 6], label="標籤一")
plt.scatter([1, 3, 4], [2, 5, 4], label="標籤二")
plt.legend()
plt.show()

#載入CSV檔案格式的資料，繪製適當的散佈圖加標示
import csv
file=open(r"C:\Users\stan_liao\Desktop\VS Code Python\csv\scatter-chart-data.csv", encoding="utf-8")
reader=csv.reader(file)
next(reader) # 讀取第一列 (跳過)
data={
    "男":{"x":[], "y":[]},
    "女":{"x":[], "y":[]}
}
for row in reader:
    print(row)
    gender=row[0]
    data[gender]["x"].append(int(row[1]))
    data[gender]["y"].append(int(row[2]))

print(data)

plt.scatter(data["男"]["x"], data["男"]["y"], label="男生")
plt.scatter(data["女"]["x"], data["女"]["y"], label="女生")
plt.legend()
plt.show()