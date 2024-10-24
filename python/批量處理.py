# 1. 使用批量處理
# 分批轉移：將資料分成小批量進行轉移，而不是一次性轉移整個資料表。這可以減少記憶體使用量並避免超時。

import pyodbc
import mysql.connector

mssql_conn = None

# MSSQL 連接
mssql_conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_mssql_server;DATABASE=your_db;UID=your_username;PWD=your_password")

mssql_cursor = mssql_conn.cursor()

batch_size = 1000  # 每次處理的批量大小
offset = 0

while True:
    # 從 MSSQL 中選取一批資料
    mssql_cursor.execute(f"SELECT * FROM your_table ORDER BY id OFFSET {offset} ROWS FETCH NEXT {batch_size} ROWS ONLY")
    batch_data = mssql_cursor.fetchall()
    
    if not batch_data:
        break  # 沒有更多資料，結束循環
    
    # 將批量資料插入到 MySQL
    mysql_cursor.executemany(insert_query, batch_data)
    mysql_conn.commit()
    
    offset += batch_size




# 分批處理範例

import pyodbc
import mysql.connector

# MSSQL 連接
mssql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_mssql_server;DATABASE=your_db;UID=your_username;PWD=your_password')
mssql_cursor = mssql_conn.cursor()

# MySQL 連接
mysql_conn = mysql.connector.connect(
    host="10.96.196.36",
    user="NPSPO_User",
    password="Gaming@NPD",
    database="your_mysql_db"
)
mysql_cursor = mysql_conn.cursor()

# 增量查詢
last_sync_time = get_last_sync_time()  # 獲取上次同步的時間
mssql_cursor.execute(f"SELECT * FROM your_table WHERE last_modified > '{last_sync_time}'")

# 批量插入
batch_size = 1000
while True:
    batch_data = mssql_cursor.fetchmany(batch_size)
    if not batch_data:
        break

    insert_query = "INSERT INTO your_table (id, name, value) VALUES (%s, %s, %s)"
    mysql_cursor.executemany(insert_query, batch_data)
    mysql_conn.commit()

# 更新最後同步時間
update_last_sync_time()

# 關閉連接
mysql_cursor.close()
mysql_conn.close()
mssql_cursor.close()
mssql_conn.close()

