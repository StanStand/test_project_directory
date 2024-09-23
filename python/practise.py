# # 匯入 pyodbc 模組
# import pyodbc

# # 設定連接參數
# server = 'APZA001GOD'        # 替換為你的 SQL Server 位址
# database = 'ArmouryCrate_New_hive'    # 替換為你的資料庫名稱
# username = 'ASUS\Stan_Liao'        # 替換為你的使用者名稱
# password = ''       # 例如：'your_password'

# # 建立與 SQL Server 的連接
# conn = pyodbc.connect(
#     f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
# )

# # 建立 cursor 對象，用來執行 SQL 查詢
# cursor = conn.cursor()

# # 執行 SQL 查詢
# cursor.execute("SELECT * FROM your_table")  # 替換為你要查詢的資料表名稱

# # 遍歷並打印查詢結果
# for row in cursor:
#     print(row)  # 打印每一行的結果

# # 關閉連接
# conn.close()

# import pyodbc

# # 定義變數
# server = 'APZA001GOD'  # 例如：'localhost' 或 '10.96.196.36'
# database = 'ArmouryCrate_New_hive'  # 例如：'MyDatabase'

# # 建立連接字串
# connection_string = (
#     f'DRIVER={{ODBC Driver 17 for SQL Server}};'
#     f'SERVER={server};'
#     f'DATABASE={database};'
#     f'Trusted_Connection=yes;'
# )

# # 連接到 SQL Server
# try:
#     conn = pyodbc.connect(connection_string)
#     print("連接成功")
# except pyodbc.Error as e:
#     print(f"連接失敗: {e}")

# # 使用連接進行其他操作...



import pyodbc

# 定義伺服器與資料庫變數
server = 'APZA001GOD'  # 指定要連接的 SQL Server 伺服器
database = 'ArmouryCrate_New_hive'  # 指定要連接的資料庫名稱

# 建立連接字串
# ODBC 驅動為 'ODBC Driver 17 for SQL Server'，使用受信任連接
connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'  # ODBC 驅動程序
    f'SERVER={server};'  # 伺服器地址
    f'DATABASE={database};'  # 資料庫名稱
    f'Trusted_Connection=yes;'  # 使用 Windows 驗證進行受信任的連接
)

# 初始化連接變數
conn = None
try:
    # 嘗試連接到 SQL Server 資料庫
    conn = pyodbc.connect(connection_string)
    print("連接成功")  # 成功連接後打印訊息

    # 創建游標對象，用來執行 SQL 查詢
    cursor = conn.cursor()

    # 執行 SQL 查詢，從系統表 INFORMATION_SCHEMA.TABLES 中獲取所有 BASE TABLE 的名稱
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
    
    # 使用 fetchall() 取得查詢結果中的所有表格名稱
    tables = cursor.fetchall()

    # 打印資料庫中的所有表格名稱
    print("資料庫中的表:")
    for table in tables:
        print(table.TABLE_NAME)  # 每個表格名稱使用 table.TABLE_NAME 打印出來

    # 讓使用者輸入要查看數據的表格名稱
    table_name = input("請輸入要查看數據的表名: ")

    # 執行 SQL 查詢，選取指定表格中的所有數據
    cursor.execute(f'SELECT * FROM {table_name}')  

    # 獲取查詢的結果，使用 fetchall() 取得表中的所有數據
    rows = cursor.fetchall()

    # 打印查詢結果
    print(f"表 {table_name} 的數據:")
    for row in rows:
        print(row)  # 每一行數據都會打印出來

except pyodbc.Error as e:
    # 如果連接或 SQL 查詢過程中發生錯誤，會打印錯誤訊息
    print(f"連接失敗: {e}")

finally:
    # 確保無論如何都會關閉資料庫連接
    if conn:
        conn.close()  # 關閉連接以釋放資源




# 連線網址

import urllib.request as request

with request.urlopen(網址) as response:
        data = response.read() # 使用 json 模块解析 JSON 数据
print(data)  # 美化输出 JSON 数据

# 網路連線
import urllib.resquest as request
src="https://www.google.com"
with request.urlopen(src) as response:
    data=response.read().decode("utf-8") # 取得網站的原始碼 (HTML CSS JS)
print(data)


# 公開資料
# https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire
# 確認資料格式 JSON CSV或其他格式
# 解讀JSON格式

import urllib.request as request
import json

# 台北開放資料平台 API 的 URL
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"

# 發送請求並接收回應
with request.urlopen(src) as response:
    data = json.load(response)  # 使用 json 模块解析 JSON 数据

# 將公司名稱列表出來
clist = data["result"]["results"]
for company in clist:
    print(company["公司名稱"])

#     print(json.dumps(data, indent=4, ensure_ascii=False))  # 美化输出 JSON 数据
# except Exception as e:
#     print(e)

import urllib.request as request
import json

# 目標資料來源網址
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"

# 開啟網址並讀取內容
with request.urlopen(src) as response:
    data = json.load(response)  # 使用 json 模組解析 JSON 資料

# 將公司名稱列出來
clist = data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:

    for company in clist:
        file.write(company["公司名稱"]+"\n")
    # print(company["公司名稱"])  # 列出公司名稱


import pandas as pd
import mysql.connector
import os

# CSV 文件路徑
file_path = r'C:\Users\stan_liao\Desktop\sample_data.csv'

# 讀取 CSV 文件
if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path)
        print("CSV 加載成功：")
        print(df.head())  # 檢查數據前幾行
    except Exception as e:
        print(f"讀取 CSV 文件失敗: {e}")
else:
    print(f"文件路徑錯誤：{file_path}")

# 連接到 MySQL 資料庫
try:
    conn = mysql.connector.connect(
        host="10.96.196.36",
        user="NPSPO_User",
        password="Gaming@NPD",
        database="stan01"
    )
    cursor = conn.cursor()
    print("MySQL 連接成功")
except Exception as e:
    print(f"MySQL 連接失敗: {e}")

# 確認 df 是否被成功讀取
if 'df' in locals():
    try:
        # 確保資料表存在
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS your_table (
            column1 INT,
            column2 VARCHAR(255)
        )
        """)

        for i, row in df.iterrows():
            cursor.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", (row['col1'], row['col2']))
        conn.commit()
        print("數據插入成功")
    except Exception as e:
        print(f"插入數據失敗: {e}")
    finally:
        cursor.close()
        conn.close()









# 匯入相關模組
import pyodbc
import urllib.request as request
import json
import pandas as pd
import mysql.connector
import os

# 連接到 SQL Server
server = 'APZA001GOD'
database = 'ArmouryCrate_New_hive'

connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

try:
    # 嘗試連接到 SQL Server 資料庫
    conn = pyodbc.connect(connection_string)
    print("連接成功")
    
    cursor = conn.cursor()

    # 查詢資料庫中的所有表格
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
    tables = cursor.fetchall()
    print("資料庫中的表:")
    for table in tables:
        print(table.TABLE_NAME)

    # 選取指定表格的數據
    table_name = input("請輸入要查看數據的表名: ")
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()

    print(f"表 {table_name} 的數據:")
    for row in rows:
        print(row)

except pyodbc.Error as e:
    print(f"連接失敗: {e}")
finally:
    if conn:
        conn.close()

# 台北開放資料平台 API
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)

# 將公司名稱列表寫入檔案
clist = data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"] + "\n")

# 讀取 CSV 文件
file_path = r'C:\Users\stan_liao\Desktop\sample_data.csv'
if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path)
        print("CSV 加載成功：")
        print(df.head())
    except Exception as e:
        print(f"讀取 CSV 文件失敗: {e}")
else:
    print(f"文件路徑錯誤：{file_path}")

# 連接到 MySQL 資料庫
try:
    conn = mysql.connector.connect(
        host="10.96.196.36",
        user="NPSPO_User",
        password="Gaming@NPD",
        database="stan01"
    )
    cursor = conn.cursor()
    print("MySQL 連接成功")
except Exception as e:
    print(f"MySQL 連接失敗: {e}")

# 插入 CSV 資料到 MySQL
if 'df' in locals():
    try:
        # 確保資料表存在
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS your_table (
            column1 INT,
            column2 VARCHAR(255)
        )
        """)

        for i, row in df.iterrows():
            cursor.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", (row['col1'], row['col2']))
        conn.commit()
        print("數據插入成功")
    except Exception as e:
        print(f"插入數據失敗: {e}")
    finally:
        cursor.close()
        conn.close()
