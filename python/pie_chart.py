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

import matplotlib.pyplot as plt
# 設定字形為 Windows 內建的微軟正黑體，支持中文顯示
plt.rc("font", family="Microsoft JhengHei")
# 繪製一組資料點的圓餅圖，並且加上適當的百分比標示
x=[10, 15, 25]
total=sum(x) # 算列表中數值的總和sum(列表)
labels=[str(100*data/total)+"%"for data in x]
print(labels)


plt.pie(
    x,
    # labels=[str(100*x[0]/total)+"%", str(100*x[1]/total)+"%", str(100*x[2]/total)+"%"],
    labels=labels,
    labeldistance=0.5
    )
plt.legend()
plt.show()


# 載入CSV格式的檔案資料，繪製圓餅圖並加上適當的標示
import csv
file=open(r"C:\Users\stan_liao\Desktop\VS Code Python\csv\pie_data.csv", encoding="utf-8")
reader=csv.reader(file)
next(reader) # 讀取第一行
x=[]
labels=[]
for row in reader:
    labels.append((row[0]))
    x.append(int(row[1]))
    
plt.pie(x, labels=labels, labeldistance=1.1)
plt.legend()
plt.title("瀏覽器的市場佔有率分佈")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


# 使用 Pandas 讀取 CSV 檔案
df = pd.read_csv(r"C:\Users\stan_liao\Desktop\VS Code Python\csv\pie_data.csv", encoding="utf-8")

# 檢查資料
print(df)

# 繪製圓餅圖
plt.pie(df['市佔率'], labels=df['瀏覽器'], autopct='%1.1f%%', startangle=90)
# 默認值：如果不設置 startangle，圓餅圖的第一個部分會從 3 點鐘的位置開始（即右側）。
# 設定 startangle=90：這表示圓餅圖的第一個部分會從 12 點鐘的位置開始，這樣會讓圖形的顯示看起來更為直觀，尤其是在顯示百分比時，因為 12 點鐘的位置常被視為起點。
# 示例：
# startangle=0：圓餅圖從 3 點鐘開始。
# startangle=90：圓餅圖從 12 點鐘開始。
# startangle=180：圓餅圖從 9 點鐘開始。
# 添加標題
plt.title("瀏覽器的市場佔有率分佈")
plt.axis('equal')  # 使圓餅圖為圓形
plt.show()


