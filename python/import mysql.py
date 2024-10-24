# import mysql.connector
# print("mysql.connector has been installed successfully.")
# from datetime import datetime

# # 連接到 MySQL 資料庫
# conn = mysql.connector.connect(
#     host='10.96.196.36',
#     user='NPSPO_User',
#     password='Gaming@NPD',
#     database='stan_test'
# )
# cursor = conn.cursor()

# # Speedtest 結果數據
# data = {
#     "id": "312b6ceb-1d62-442b-861f-5afce40599c9",
#     "timestamp": datetime.utcnow(),
#     "ping_jitter": 1.333,
#     "ping_latency": 4.019,
#     "ping_low": 3.961,
#     "ping_high": 6.614,
#     "download_bandwidth": 2001524,
#     "download_bytes": 30743504,
#     "download_elapsed": 15004,
#     "download_latency_iqm": 221.150,
#     "download_latency_low": 5.367,
#     "download_latency_high": 677.479,
#     "download_latency_jitter": 70.992,
#     "upload_bandwidth": 1884830,
#     "upload_bytes": 26691834,
#     "upload_elapsed": 14991,
#     "upload_latency_iqm": 874.181,
#     "upload_latency_low": 5.135,
#     "upload_latency_high": 2444.526,
#     "upload_latency_jitter": 107.735,
#     "isp": "New Century InfoComm Tech Co.",
#     "internal_ip": "10.96.153.0",
#     "external_ip": "118.163.80.132",
#     "mac_addr": "14:5A:FC:90:8A:27",
#     "vpn": False,
#     "server_id": 3967,
#     "server_host": "tpv3-1.speedtest.idv.tw",
#     "server_port": 8080,
#     "server_name": "Chief Telecom",
#     "server_location": "Taipei",
#     "server_country": "Taiwan",
#     "server_ip": "210.61.132.17",
#     "result_url": "https://www.speedtest.net/result/c/312b6ceb-1d62-442b-861f-5afce40599c9"
# }

# # 插入數據
# query = """
# INSERT INTO speedtest_results (
#     id, timestamp, ping_jitter, ping_latency, ping_low, ping_high, 
#     download_bandwidth, download_bytes, download_elapsed, 
#     download_latency_iqm, download_latency_low, download_latency_high, 
#     download_latency_jitter, upload_bandwidth, upload_bytes, 
#     upload_elapsed, upload_latency_iqm, upload_latency_low, 
#     upload_latency_high, upload_latency_jitter, isp, internal_ip, 
#     external_ip, mac_addr, vpn, server_id, server_host, server_port, 
#     server_name, server_location, server_country, server_ip, result_url
# ) VALUES (
#     %(id)s, %(timestamp)s, %(ping_jitter)s, %(ping_latency)s, %(ping_low)s, %(ping_high)s, 
#     %(download_bandwidth)s, %(download_bytes)s, %(download_elapsed)s, 
#     %(download_latency_iqm)s, %(download_latency_low)s, %(download_latency_high)s, 
#     %(download_latency_jitter)s, %(upload_bandwidth)s, %(upload_bytes)s, 
#     %(upload_elapsed)s, %(upload_latency_iqm)s, %(upload_latency_low)s, 
#     %(upload_latency_high)s, %(upload_latency_jitter)s, %(isp)s, %(internal_ip)s, 
#     %(external_ip)s, %(mac_addr)s, %(vpn)s, %(server_id)s, %(server_host)s, %(server_port)s, 
#     %(server_name)s, %(server_location)s, %(server_country)s, %(server_ip)s, %(result_url)s
# )
# """
# cursor.execute(query, data)
# conn.commit()

# # 關閉連接
# cursor.close()
# conn.close()



# import pandas as pd 

# # 讀取 csv 檔案

# df = pd.read_csv(r"C:\Users\stan_liao\Desktop\VS Code Python\csv\mapping_keypart_cpu_20241007.csv", sep='|', on_bad_lines='skip')
# df.columns = ['ID', 'Processor', 'NR', 'Brand', 'Generation', 'Core Type', 'Core Model', 'Model', 'Cores Config', 'Date', 'Schedule', 'Other Info']

# print(df.head())  # 查看前五行
# print(df.columns)  # 查看欄位名稱
# print(len(df.columns))  # 確認欄位數量


# # from sqlalchemy import create_engine

# # engine = create_engine('mysql+pymysql://NPSPO_User:Gaming@NPD@10.96.196.36:3306/stan01')

# # df.to_sql('new_table', con=engine, if_exists='replace', index=False)
# # print("資料成功寫入")


# import mysql.connector

# # 连接到数据库
# connection = mysql.connector.connect(
#     host='10.96.196.36',
#     user='NPSPO_User',
#     password='Gaming@NPD',
#     database='stan01'
# )

# cursor = connection.cursor()

# # 创建表的 SQL 语句
# create_table_query = '''
# CREATE TABLE example_table (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# '''

# # 执行 SQL 语句
# cursor.execute(create_table_query)

# # 提交更改并关闭连接
# connection.commit()
# cursor.close()
# connection.close()


# import pandas as pd
# import mysql.connector
# from mysql.connector import Error

# # 读取 CSV 文件
# df = pd.read_csv(r"C:\Users\stan_liao\Desktop\VS Code Python\csv\mapping_keypart_cpu_20241007.csv", sep='|', on_bad_lines='skip')
# df.columns = ['ID', 'Processor', 'NR', 'Brand', 'Generation', 'Core Type', 'Core Model', 'Model', 'Cores Config', 'Date', 'Schedule', 'Other Info']

# # 打印原始数据以便调试
# print("原始数据：")
# print(df)

# # 检查并处理 NaN 值
# df = df.where(pd.notnull(df), None)  # 替换 NaN 值为 None

# # 检查是否仍有 NaN 值
# if df.isnull().values.any():
#     print("注意：DataFrame 中仍有 NaN 值，处理后如下：")
#     print(df)

# # 创建 MySQL 连接
# conn = None
# try:
#     conn = mysql.connector.connect(
#         host="10.96.196.36",  # 服务器 IP
#         user="NPSPO_User",  # 用户名
#         password="Gaming@NPD",  # 密码
#         database="stan01"  # 数据库名称
#     )

#     if conn.is_connected():
#         print("已成功连接到 MySQL 数据库")

#         # 创建游标对象
#         cursor = conn.cursor()

#         # 创建新表的 SQL 语句
#         create_table_query = '''
#         CREATE TABLE IF NOT EXISTS cpu_mapping (
#             ID INT PRIMARY KEY,
#             Processor VARCHAR(255) NOT NULL,
#             NR VARCHAR(50),
#             Brand VARCHAR(50),
#             Generation VARCHAR(50),
#             Core_Type VARCHAR(50),
#             Core_Model VARCHAR(50),
#             Model VARCHAR(50),
#             Cores_Config VARCHAR(50),
#             Date DATE,
#             Schedule VARCHAR(100),
#             Other_Info VARCHAR(255)
#         );
#         '''

#         # 执行创建表的 SQL 语句
#         cursor.execute(create_table_query)

#         # 将 DataFrame 数据插入到 MySQL 表中
#         for i, row in df.iterrows():
#             # 打印每一行数据及其类型
#             print(f"插入行 {i}: {row} (类型: {[type(v) for v in row]})")  # 打印当前行数据和类型
            
#             # 生成插入 SQL 语句
#             insert_query = '''
#             INSERT INTO cpu_mapping (ID, Processor, NR, Brand, Generation, Core_Type, Core_Model, Model, Cores_Config, Date, Schedule, Other_Info)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             '''
#             # 将行数据转换为元组，并检查是否有 None 值
#             row_data = tuple(row)
#             if None in row_data:
#                 print(f"警告：行 {i} 中含有 None 值，将跳过该行。")
#                 continue
            
#             cursor.execute(insert_query, row_data)

#         # 提交更改
#         conn.commit()
#         print("数据成功插入到 cpu_mapping 表中")

# except Error as e:
#     print(f"数据库错误: {e}")

# finally:
#     # 确保连接在程序结束时正确关闭
#     if conn is not None and conn.is_connected():
#         cursor.close()
#         conn.close()
#         print("数据库连接已关闭")


import pandas as pd
import mysql.connector

# 讀取CSV文件
csv_file_path = 'C:\Users\stan_liao\Desktop\VS Code Python\csv\mapping_keypart_cpu_20241007.csv'
data = pd.read_csv(csv_file_path)
# 連接到 MySQL 數據庫 
connection = mysql.connector.connect(
    host='10.96.196.36',
    user='NPSPO_User',
    password='Gaming@NPD',
    database='stan01' 
)

# 将数据写入 MySQL 数据库
data.to_sql(name='cpu_mapping', con=connection, if_exists='replace', index=False)  # 替换为你的表名

# 关闭连接
connection.close()

import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# 读取 CSV 文件
# 使用原始字符串格式或将反斜杠替换为正斜杠
csv_file_path = r'C:\Users\stan_liao\Desktop\VS Code Python\csv\mapping_keypart_cpu_20241007.csv'  # 使用原始字符串格式
# 或者
# csv_file_path = 'C:/Users/stan_liao/Desktop/VS Code Python/csv/mapping_keypart_cpu_20241007.csv'  # 使用正斜杠

data = pd.read_csv(csv_file_path)

# 连接到 MySQL 数据库
# 创建 SQLAlchemy 引擎
engine = create_engine('mysql+mysqlconnector://NPSPO_User:Gaming%40NPD@10.96.196.36:3306/stan01')

# 将数据写入 MySQL 数据库
data.to_sql(name='cpu_mapping', con=engine, if_exists='replace', index=False)  # 替换为你的表名

# 如果你使用 mysql.connector 直接操作
connection = mysql.connector.connect(
    host='10.96.196.36',
    user='NPSPO_User',
    password='Gaming@NPD',
    database='stan01'  # 替换为你想要导入数据的数据库名称
)

# 在这里可以执行其他 SQL 操作

# 关闭连接
connection.close()



import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# 读取 CSV 文件
csv_file_path = r'C:\Users\stan_liao\Desktop\VS Code Python\csv\mapping_keypart_cpu_20241007.csv'
try:
    # 尝试读取 CSV 文件，处理错误行
    data = pd.read_csv(csv_file_path, on_bad_lines='skip')  # 跳过出错的行
except Exception as e:
    print(f"读取 CSV 文件时出错: {e}")
    data = None  # 确保 data 在出错时被设置为 None

if data is not None:
    # 调整列名，确保每个列名不超过 64 个字符
    data.columns = [col[:64] for col in data.columns]

    # 连接到 MySQL 数据库
    engine = create_engine('mysql+mysqlconnector://NPSPO_User:Gaming%40NPD@10.96.196.36:3306/stan01')

    # 将数据写入 MySQL 数据库
    try:
        data.to_sql(name='cpu_mapping', con=engine, if_exists='replace', index=False)
    except Exception as e:
        print(f"将数据写入 MySQL 时出错: {e}")

    # 关闭连接
    connection = mysql.connector.connect(
        host='10.96.196.36',
        user='NPSPO_User',
        password='Gaming@NPD',
        database='stan01'
    )
    connection.close()


import pandas as pd
from sqlalchemy import create_engine

# 读取 CSV 文件
csv_file_path = r'C:\Users\stan_liao\Desktop\VS Code Python\csv\mapping_keypart_cpu_20241007.csv'
try:
    # 尝试读取 CSV 文件，处理错误行
    data = pd.read_csv(csv_file_path, on_bad_lines='skip')  # 跳过出错的行
except Exception as e:
    print(f"读取 CSV 文件时出错: {e}")
    data = None  # 确保 data 在出错时被设置为 None

if data is not None:
    # 打印数据的前几行以确认
    print("读取的数据：")
    print(data.head())

    # 连接到 MySQL 数据库
    engine = create_engine('mysql+mysqlconnector://NPSPO_User:Gaming%40NPD@10.96.196.36:3306/stan01')

    # 将数据写入 MySQL 数据库
    try:
        # 确保列名不超过 64 个字符
        data.columns = [col[:64] for col in data.columns]

        # 将数据写入数据库
        data.to_sql(name='cpu_mapping', con=engine, if_exists='replace', index=False)
        print("数据成功写入 MySQL 数据库。")
    except Exception as e:
        print(f"将数据写入 MySQL 时出错: {e}")
else:
    print("没有有效的数据可供写入。")


import mysql.connector

# 连接到 MySQL 数据库
conn = mysql.connector.connect(
    host='10.96.196.36',
    port=3306,
    user='NPSPO_User',
    password='Gaming@NPD',
    database='stan01',
    allow_local_infile=True  # 启用 LOCAL INFILE
)

cursor = conn.cursor()

# 设置 LOCAL INFILE
cursor.execute("SET GLOBAL local_infile = 1;")

# SQL 语句
load_data_sql = """
    LOAD DATA LOCAL INFILE 'C:/Users/stan_liao/Downloads/mapping_keypart_cpu_20241007.csv'
    INTO TABLE cpu_mapping_new
    FIELDS TERMINATED BY '|'
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    (cpuitemid, processor, cpu_vendor, cpu_platform, cpu_generation, cpu_segment, cpu_model, cpu_core, controller_short);
"""

try:
    # 执行 SQL 语句
    cursor.execute(load_data_sql)
    conn.commit()
    print("CSV 文件已成功导入。")
except Exception as e:
    print(f"导入时发生错误: {e}")
finally:
    cursor.close()
    conn.close()


import pandas as pd

# 讀取 CSV 文件
file_path = 'C:/Users/stan_liao/Downloads/mapping_keypart_cpu_20241007.csv'
df = pd.read_csv(file_path, delimiter='|', header=None)

# 刪除原本 cpu_vendor 欄位中的資料（假設 cpu_vendor 是第三欄，索引為 2）
df[2] = None  # 將第三欄的資料設為 None 或空值

# 從第四欄 (索引為 3) 開始，將後面的所有資料往前移動一欄
for i in range(3, df.shape[1]):
    df[i-1] = df[i]  # 將 i 欄的資料移動到 i-1 欄

# 移除最後一列空值欄位
df = df.drop(columns=[df.shape[1] - 1])

# 設置新的欄位名稱
df.columns = ['cpuitemid', 'processor', 'cpu_vendor', 'cpu_platform', 'cpu_generation', 
              'cpu_segment', 'cpu_model', 'cpu_core', 'controller_short']

# 檢查修改後的 DataFrame
print(df.head())

# 將處理後的資料寫入新的 CSV 文件
output_file = 'C:/Users/stan_liao/Downloads/mapping_keypart_cpu_cleaned.csv'
df.to_csv(output_file, sep='|', index=False, header=False)


import pymysql

# 建立與 MySQL 的連線
connection = pymysql.connect(
    host='10.96.196.36',
    user='NPSPO_User',
    password='Gaming@NPD',
    database='stan01'
)

try:
    with connection.cursor() as cursor:
        # 更新 controller_short 欄位為 cpu_model 最後一段資料
        update_query = """
        UPDATE cpu_mapping_new
        SET controller_short = SUBSTRING_INDEX(cpu_model, '|', -1); 
        """
        cursor.execute(update_query)
        
    # 提交更改
    connection.commit()

finally:
    connection.close()




import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('C:\Users\stan_liao\Downloads\mapping_keypart_cpu_20241007 (1).csv')

# 处理器型号列表，保持原始顺序
new_processors = [
    "i5-12450H",
    "i5-12500H",
    "i7-12650H",
    "i7-12700H",
    "i9-12900H",
    "i9-12950HX",
    "i5-13420H",
    "i5-13450HX",
    "i5-13500H",
    "i5-13500HX",
    "i7-13620H",
    "i7-13650HX",
    "i7-13700H",
    "i7-13700HX",
    "i9-13900H",
    "i9-13980HX",
    "A10-9600P",
    "A12-9700P",
    "A6-9220",
    "A9-9420",
    "A9-9425",
    "E2-9000",
    "3020e",
    "A10-9620P",
    "A12-9720P",
    "A4-9125",
    "A6-7310",
    "A6-9225",
    "ATHLON 300U",
    "ATHLON 3150U",
    "ATHLON 3050U",
    "A6-9200",
    "A6-9210",
    "A9-9400",
    "A9-9410",
    "E2-9010",
    "E1-2100",
    "E1-2500",
    "A4-1200",
    "E1-6010",
    "E1-7010",
    "E2-6110",
    "E2-7110",
    "E2-7015",
    "R9",
    "FX-9800P",
    "R5",
    "R7",
    "A10-7400P",
    "A10-8700P",
    "A10-9630P",
    "A12-9730P",
    "A4-6210",
    "A4-7210",
    "A8-7200P",
    "A8-7410",
    "FX-7500",
    "FX-7600P",
    "FX-8800P",
    "FX-9830P",
    "A4-5000",
    "A4-5100",
    "A6-5200",
    "E2-3800",
    "R5-6600H",
    "R9-6980HS",
    "R3-2200U",
    "R3-2300U",
    "R3-3200U",
    "R3-3250U",
    "R3-4300U",
    "R3-5300U",
    "R3-7320U",
    "R5-2500U",
    "R5-3500U",
    "R5-3550H",
    "R5-4500U",
    "R5-4600H",
    "R5-4600HS",
    "R5-5500U",
    "R5-5600H",
    "R5-5600U",
    "R5-5625U",
    "R5-6600H",
    "R5-6600U",
    "R5-7430U",
    "R5-7520U",
    "R5-7530U",
    "R5-7535HS",
    "R5-7535H",
    "R5-7535U",
    "R5-7540U",
    "R5-7640HS",
    "R7-2700U",
    "R7-3700U",
    "R7-3750H",
    "R7-4700U",
    "R7-4800H",
    "R7-5800H",
    "R7-5800U",
    "R7-5825U",
    "R7-6800H",
    "R7-7435H",
    "R7-7735HS",
    "R7-7840H",
    "R7-8840HS",
    "R9-4900H",
    "R9-5900HS",
    "R9-6900HX",
    "R9-7940H",
    "R9-8945H",
    "AI R9 365",
    "CORE ULTRA 5",
    "CORE ULTRA 7",
    "CORE ULTRA 9",
    "i5-1334U",
    "CORE i5",
    "CORE i7",
    "CORE i9",
    "i5-4310U",
    "i7-4510U",
    "i7-12850HX",
    "E8000",
    "Z2560+i5-4200U",
    "Z2560+i7-4500U",
    "Z2560",
    "Z8350",
    "2957U",
    "4305U",
    "N3000",
    "N3060",
    "N3160",
    "N3350",
    "N4000",
    "N4020",
    "N4100",
    "N4120",
    "N4500",
    "N5100",
    "CORE 3 100U",
    "CORE 5 120U",
    "CORE 7 150U",
    "5Y10",
    "5Y70",
    "CORE ULTRA 5 125H",
    "CORE ULTRA 5 125U",
    "i3-1005G1",
    "i3-10110U",
    "i3-1115G4",
    "i3-1220P",
    "i3-1315U",
    "i3-4005U",
    "i3-4030U",
    "i3-5005U",
    "i3-6100U",
    "i3-7020U",
    "i5-10200H",
    "i5-10210U",
    "i5-10300H",
    "i5-11300H",
    "i5-1240P",
    "i5-12500H",
    "i5-1335U",
    "i5-1340P",
    "i5-13500H",
    "i5-4210U",
    "i5-5200U",
    "i5-6198DU",
    "i5-6200U",
    "i5-6300HQ",
    "i5-7200U",
    "i5-7300HQ",
    "i7-7700HQ",
    "i7-10510U",
    "i7-10610U",
    "i7-10710U",
    "i7-10750H",
    "i7-10810U",
    "i7-11370H",
    "i7-11600H",
    "i7-1250U",
    "i7-1260P",
    "i7-12700H",
    "i9-10980HK",
    "i9-11900H",
    "i9-12900H",
    "i9-13900H",
    "i9-14900HX",
    "M3-6Y30",
    "M3-7Y30",
    "M3-8100Y",
    "M5-6Y54",
    "M7-6Y75",
    "1017U",
    "1007U",
    "N2815",
    "N2820",
    "N2830",
    "N2840",
    "N3050",
    "i7-4650U",
    "i3-2350M",
    "i3-2365M",
    "i3-2367M",
    "i3-2370M",
    "i3-3110M",
    "i5-3210M",
    "i5-3230M",
    "i5-3317U",
    "i5-4200H",
    "i7-3517U",
    "PENTIUM 8505",
    "N3700",
    "N4200",
    "N5000",
    "Z3775",
    "Z3735D",
    "Z3735F",
    "Z3740",
    "N2910",
    "N2920",
    "N2930",
    "N2940",
    "N3150"
]

# 创建一个映射字典，以获取处理器的排序顺序
order_dict = {model: index for index, model in enumerate(new_processors)}

# 添加一个新列表示处理器型号的顺序
df['order'] = df['cpu_model'].map(order_dict)

# 按照新列排序 DataFrame
df_sorted = df.sort_values('order')

# 删除顺序列
df_sorted = df_sorted.drop(columns='order')

# 将排序后的 DataFrame 写入新 CSV 文件
df_sorted.to_csv('sorted_cpu_mapping.csv', index=False)


import pandas as pd


# 读取 CSV 文件，使用 '|' 作为分隔符，并且没有列名
# 读取 CSV 文件，指定分隔符为 '|'
df = pd.read_csv(r'C:\Users\stan_liao\Downloads\mapping_keypart_cpu_20241007 (1).csv', sep='|', header=None)

# 处理器型号列表，保持原始顺序
new_processors = [
    "i5-12450H",
    "i5-12500H",
    "i7-12650H",
    "i7-12700H",
    "i9-12900H",
    "i9-12950HX",
    "i5-13420H",
    "i5-13450HX",
    "i5-13500H",
    "i5-13500HX",
    "i7-13620H",
    "i7-13650HX",
    "i7-13700H",
    "i7-13700HX",
    "i9-13900H",
    "i9-13980HX",
    "A10-9600P",
    "A12-9700P",
    "A6-9220",
    "A9-9420",
    "A9-9425",
    "E2-9000",
    "3020e",
    "A10-9620P",
    "A12-9720P",
    "A4-9125",
    "A6-7310",
    "A6-9225",
    "ATHLON 300U",
    "ATHLON 3150U",
    "ATHLON 3050U",
    "A6-9200",
    "A6-9210",
    "A9-9400",
    "A9-9410",
    "E2-9010",
    "E1-2100",
    "E1-2500",
    "A4-1200",
    "E1-6010",
    "E1-7010",
    "E2-6110",
    "E2-7110",
    "E2-7015",
    "R9",
    "FX-9800P",
    "R5",
    "R7",
    "A10-7400P",
    "A10-8700P",
    "A10-9630P",
    "A12-9730P",
    "A4-6210",
    "A4-7210",
    "A8-7200P",
    "A8-7410",
    "FX-7500",
    "FX-7600P",
    "FX-8800P",
    "FX-9830P",
    "A4-5000",
    "A4-5100",
    "A6-5200",
    "E2-3800",
    "R5-6600H",
    "R9-6980HS",
    "R3-2200U",
    "R3-2300U",
    "R3-3200U",
    "R3-3250U",
    "R3-4300U",
    "R3-5300U",
    "R3-7320U",
    "R5-2500U",
    "R5-3500U",
    "R5-3550H",
    "R5-4500U",
    "R5-4600H",
    "R5-4600HS",
    "R5-5500U",
    "R5-5600H",
    "R5-5600U",
    "R5-5625U",
    "R5-6600H",
    "R5-6600U",
    "R5-7430U",
    "R5-7520U",
    "R5-7530U",
    "R5-7535HS",
    "R5-7535H",
    "R5-7535U",
    "R5-7540U",
    "R5-7640HS",
    "R7-2700U",
    "R7-3700U",
    "R7-3750H",
    "R7-4700U",
    "R7-4800H",
    "R7-5800H",
    "R7-5800U",
    "R7-5825U",
    "R7-6800H",
    "R7-7435H",
    "R7-7735HS",
    "R7-7840H",
    "R7-8840HS",
    "R9-4900H",
    "R9-5900HS",
    "R9-6900HX",
    "R9-7940H",
    "R9-8945H",
    "AI R9 365",
    "CORE ULTRA 5",
    "CORE ULTRA 7",
    "CORE ULTRA 9",
    "i5-1334U",
    "CORE i5",
    "CORE i7",
    "CORE i9",
    "i5-4310U",
    "i7-4510U",
    "i7-12850HX",
    "E8000",
    "Z2560+i5-4200U",
    "Z2560+i7-4500U",
    "Z2560",
    "Z8350",
    "2957U",
    "4305U",
    "N3000",
    "N3060",
    "N3160",
    "N3350",
    "N4000",
    "N4020",
    "N4100",
    "N4120",
    "N4500",
    "N5100",
    "CORE 3 100U",
    "CORE 5 120U",
    "CORE 7 150U",
    "5Y10",
    "5Y70",
    "CORE ULTRA 5 125H",
    "CORE ULTRA 5 125U",
    "i3-1005G1",
    "i3-10110U",
    "i3-1115G4",
    "i3-1220P",
    "i3-1315U",
    "i3-4005U",
    "i3-4030U",
    "i3-5005U",
    "i3-6100U",
    "i3-7020U",
    "i5-10200H",
    "i5-10210U",
    "i5-10300H",
    "i5-11300H",
    "i5-1240P",
    "i5-12500H",
    "i5-1335U",
    "i5-1340P",
    "i5-13500H",
    "i5-4210U",
    "i5-5200U",
    "i5-6198DU",
    "i5-6200U",
    "i5-6300HQ",
    "i5-7200U",
    "i5-7300HQ",
    "i7-7700HQ",
    "i7-10510U",
    "i7-10610U",
    "i7-10710U",
    "i7-10750H",
    "i7-10810U",
    "i7-11370H",
    "i7-11600H",
    "i7-1250U",
    "i7-1260P",
    "i7-12700H",
    "i9-10980HK",
    "i9-11900H",
    "i9-12900H",
    "i9-13900H",
    "i9-14900HX",
    "M3-6Y30",
    "M3-7Y30",
    "M3-8100Y",
    "M5-6Y54",
    "M7-6Y75",
    "1017U",
    "1007U",
    "N2815",
    "N2820",
    "N2830",
    "N2840",
    "N3050",
    "i7-4650U",
    "i3-2350M",
    "i3-2365M",
    "i3-2367M",
    "i3-2370M",
    "i3-3110M",
    "i5-3210M",
    "i5-3230M",
    "i5-3317U",
    "i5-4200H",
    "i7-3517U",
    "PENTIUM 8505",
    "N3700",
    "N4200",
    "N5000",
    "Z3775",
    "Z3735D",
    "Z3735F",
    "Z3740",
    "N2910",
    "N2920",
    "N2930",
    "N2940",
    "N3150"
]

# 生成一个与 DataFrame 行数相同的替换列表
replacements = (new_processors * (len(df) // len(new_processors) + 1))[:len(df)]

# 替换最后一列的内容为处理器型号
df.iloc[:, -1] = replacements

# 将修改后的 DataFrame 写入新的 CSV 文件
df.to_csv(r'C:\Users\stan_liao\Downloads\sorted_output.csv', index=False, sep='|', header=False)

print("处理器型号替换成功，已保存至 sorted_output.csv。")